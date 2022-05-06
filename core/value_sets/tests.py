from rest_framework.test import APIClient

from core.collections.models import CollectionReference
from core.collections.tests.factories import OrganizationCollectionFactory, ExpansionFactory
from core.common.tests import OCLTestCase
from core.concepts.tests.factories import ConceptFactory
from core.orgs.tests.factories import OrganizationFactory
from core.sources.models import Source
from core.sources.tests.factories import OrganizationSourceFactory, UserSourceFactory
from core.users.tests.factories import UserProfileFactory


class ValueSetTest(OCLTestCase):
    def setUp(self):
        super().setUp()
        self.org = OrganizationFactory()

        self.org_source = OrganizationSourceFactory(organization=self.org, canonical_url='/some/url')
        self.org_source_v1 = OrganizationSourceFactory.build(version='v1', mnemonic=self.org_source.mnemonic,
                                                             organization=self.org_source.parent)
        Source.persist_new_version(self.org_source_v1, self.org_source.created_by)
        self.concept_1 = ConceptFactory(parent=self.org_source)
        self.concept_2 = ConceptFactory(parent=self.org_source)
        self.org_source_v2 = OrganizationSourceFactory.build(version='v2', mnemonic=self.org_source.mnemonic,
                                                             organization=self.org_source.parent)
        Source.persist_new_version(self.org_source_v2, self.org_source.created_by)

        self.user = UserProfileFactory()
        self.user_token = self.user.get_token()
        self.user_source = UserSourceFactory(user=self.user, public_access='None', canonical_url='/some/url')
        self.user_source_v1 = UserSourceFactory.build(version='v1', mnemonic=self.user_source.mnemonic,
                                                      user=self.user_source.parent)
        Source.persist_new_version(self.user_source_v1, self.user_source.created_by)

        self.collection = OrganizationCollectionFactory(
            organization=self.org, mnemonic='c1', canonical_url='http://c1.com', version='HEAD')
        self.collection_v1 = OrganizationCollectionFactory(
            mnemonic='c1', canonical_url='http://c1.com', version='v1', organization=self.collection.organization)
        ExpansionFactory(mnemonic='e1', collection_version=self.collection)
        ExpansionFactory(mnemonic='e2', collection_version=self.collection_v1)

        self.client = APIClient()

    def test_public_can_find_globally_without_compose(self):
        response = self.client.get('/fhir/ValueSet/?url=http://c1.com')
        self.assertEqual(len(response.data['entry']), 1)
        resource = response.data['entry'][0]['resource']
        self.assertEqual(resource['identifier'][0]['value'], '/orgs/' + self.org.mnemonic
                         + '/ValueSet/' + self.collection.mnemonic + '/')
        self.assertEqual(resource['compose'], None)

    def test_public_can_find_globally(self):
        self.collection.add_references([CollectionReference(expression=self.concept_1.uri, collection=self.collection)])
        self.collection.add_references([CollectionReference(expression=self.concept_2.uri, collection=self.collection)])
        self.collection_v1.seed_references()

        response = self.client.get('/fhir/ValueSet/?url=http://c1.com')
        self.assertEqual(len(response.data['entry']), 1)
        resource = response.data['entry'][0]['resource']
        self.assertEqual(resource['identifier'][0]['value'], '/orgs/' + self.org.mnemonic
                         + '/ValueSet/' + self.collection.mnemonic + '/')
        self.assertEqual(len(resource['compose']['include']), 1)
        self.assertEqual(resource['compose']['include'][0]['system'], '/some/url')
        self.assertEqual(resource['compose']['include'][0]['version'], self.org_source_v2.version)
        self.assertEqual(len(resource['compose']['include'][0]['concept']), 2)

    def test_public_can_view(self):
        self.collection.add_references([CollectionReference(expression=self.concept_1.uri, collection=self.collection)])
        self.collection.add_references([CollectionReference(expression=self.concept_2.uri, collection=self.collection)])
        self.collection_v1.seed_references()

        response = self.client.get('/orgs/' + self.org.mnemonic + '/ValueSet/c1/')
        resource = response.data
        self.assertEqual(resource['identifier'][0]['value'], '/orgs/' + self.org.mnemonic
                         + '/ValueSet/' + self.collection.mnemonic + '/')
        self.assertEqual(len(resource['compose']['include']), 1)
        self.assertEqual(resource['compose']['include'][0]['system'], '/some/url')
        self.assertEqual(resource['compose']['include'][0]['version'], self.org_source_v2.version)
        self.assertEqual(len(resource['compose']['include'][0]['concept']), 2)

    def test_can_create_empty(self):
        response = self.client.post(f'/users/{self.user.mnemonic}/ValueSet/',
                                    HTTP_AUTHORIZATION='Token ' + self.user_token, data={'resourceType': 'ValueSet',
                                        'id': 'c2', 'version': 'v1', 'url': 'http://c2.com', 'status': 'draft',
                                        'name': 'collection1', 'description': 'This is a test collection' }
                                    , format='json')
        resource = response.data
        self.assertEqual(resource['version'], 'v1')
        self.assertEqual(resource['identifier'][0]['value'], '/users/' + self.user.mnemonic
                         + '/ValueSet/c2/')
        self.assertEqual(resource['compose'], None)

    def test_can_create_with_compose(self):
        response = self.client.post(f'/users/{self.user.mnemonic}/ValueSet/',
                                    HTTP_AUTHORIZATION='Token ' + self.user_token, data={
                'resourceType': 'ValueSet', 'id': 'c2', 'url': 'http://c2.com', 'status': 'draft',
                'name': 'collection1', 'description': 'This is a test collection', 'compose': {
                    'include': [
                        {
                            'system': '/some/url',
                            'version': self.org_source_v2.version,
                            'concept': [
                                {
                                    'code': self.concept_1.mnemonic
                                }
                            ]
                        }
                    ]
                }}
                                    , format='json')
        resource = response.data
        self.assertEqual(resource['version'], '0.1')
        self.assertEqual(resource['identifier'][0]['value'], '/users/' + self.user.mnemonic
                         + '/ValueSet/c2/')
        self.assertEqual(len(resource['compose']['include']), 1)
        self.assertEqual(resource['compose']['include'][0]['system'], '/some/url')
        self.assertEqual(resource['compose']['include'][0]['version'], self.org_source_v2.version)
        self.assertEqual(len(resource['compose']['include'][0]['concept']), 1)

    def test_can_update_empty(self):
        response = self.client.put(f'/orgs/{self.org.mnemonic}/ValueSet/c1/',
                                    HTTP_AUTHORIZATION='Token ' + self.user_token, data={
                'resourceType': 'ValueSet', 'id': 'c1', 'version': 'v2', 'url': 'http://c2.com', 'status': 'draft',
                'name': 'collection1', 'description': 'This is a test collection' }
                                    , format='json')
        resource = response.data
        self.assertEqual(resource['version'], 'v2')
        self.assertEqual(resource['identifier'][0]['value'], '/orgs/' + self.org.mnemonic
                         + '/ValueSet/c1/')
        self.assertEqual(resource['compose'], None)

    def test_update_with_compose(self):
        self.collection.add_references([CollectionReference(expression=self.concept_1.uri, collection=self.collection)])
        self.collection_v1.seed_references()

        response = self.client.put(f'/orgs/{self.org.mnemonic}/ValueSet/c1/',
                                   HTTP_AUTHORIZATION='Token ' + self.user_token, data={
                'resourceType': 'ValueSet', 'id': 'c1', 'version': 'v2', 'url': 'http://c2.com', 'status': 'draft',
                'name': 'collection1', 'description': 'This is a test collection', 'compose': {
                    'include': [
                        {
                            'system': '/some/url',
                            'version': self.org_source_v2.version,
                            'concept': [
                                {
                                    'code': self.concept_2.mnemonic
                                }
                            ]
                        }
                    ]
                }}
                                   , format='json')
        resource = response.data
        self.assertEqual(resource['version'], 'v2')
        self.assertEqual(resource['identifier'][0]['value'], '/orgs/' + self.org.mnemonic
                         + '/ValueSet/c1/')
        self.assertEqual(len(resource['compose']['include']), 1)
        self.assertEqual(resource['compose']['include'][0]['system'], '/some/url')
        self.assertEqual(resource['compose']['include'][0]['version'], self.org_source_v2.version)
        self.assertEqual(len(resource['compose']['include'][0]['concept']), 2)
        self.assertEqual(resource['compose']['include'][0]['concept'][0]['code'], self.concept_1.mnemonic)
        self.assertEqual(resource['compose']['include'][0]['concept'][1]['code'], self.concept_2.mnemonic)