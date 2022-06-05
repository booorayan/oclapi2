# oclapi2

The new and improved OCL terminology service v2


### Deploy with Ansible

To deploy the api on ec2 instances group with ansible run:
     `git clone https://github.com/booorayan/oclapi2.git`
     
Then:
      `cd ansible`
      
Install ansible and run the ansible playbook with the command below to deploy the api

      ansible-playbook -i inventory.yaml oclapi-playbook.yaml

The API is accessible for testing at:

      http://:80/swagger
      

Ansible runs the configuration commands on a host that is an AWS EC2 instance configured as a member of an auto scaling group. 

Auto scaling of ec2 instances will help improve the scalability of the api in response to requests received.

Further, the instances in the auto scaling group have been configured to be provisioned in different availability zones which improves the availability of the api. The api will be accessible even when one availability zone is unavailable.

The tasks defined in the ansible playbook prepare the ec2 instance by installing required packages and then deploying containers with docker compose.

First, it installs packages required by docker and adds the docker repository to the system.

It then installs Docker and Docker-Compose and adds the user 'ubuntu' to docker group to enable running docker commands without sudo privileges.

Finally, the play copies the docker-compose.prod file to the ec2 instance, renames it, copies the file with environment variables and spins up the api together with other containers using `docker-compose up` command


#### Storage 

For the deployment, the Postgres database and Redis were not containerized. 

The deployment utilizes external storage i.e. AWS Postgres RDS and Elastic cache for redis, which also have the advantage of offering data backup and facilitating disaster recovery. 

Also, with RDS, it is easy to connect ec2 instances in auto scaling groups to the same database.

Isolating the database from other application services enhances database optimization


#### Nginx Proxy

Nginx was employed to proxy http requests for security purposes among other reasons.


#### Security

To ensure security of the api and the instance, strict security group rules were followed.

Only the ports that required inbound access were exposed, limiting the risk of attack from several ports.



#### Dev Setup
1. `sysctl -w vm.max_map_count=262144` #required by Elasticsearch
2. `docker-compose up -d`
3. Go to http://localhost:8000/swagger/ to benefit.

#### Run Checks
(use the `docker exec` command in a service started with `docker-compose up -d`)
1. Pylint (pep8):
   
   `docker exec -it oclapi2_api_1 pylint -j2 core` 

    or

   `docker-compose -f docker-compose.yml -f docker-compose.ci.yml run --rm api pylint -j0 core`
2. Coverage

   `docker exec -it oclapi2_api_1 bash coverage.sh`

   or

   `docker-compose -f docker-compose.yml -f docker-compose.ci.yml run --rm api bash coverage.sh`
3. Tests

    `docker exec -it oclapi2_api_1  python manage.py test --keepdb -v3` 

    or

    `docker exec -it oclapi2_api_1  python manage.py test --keepdb -v3 -- core.sources.tests.tests.SourceTest` 

    or

    `docker-compose -f docker-compose.yml -f docker-compose.ci.yml run --rm api python manage.py test --keepdb -v3`

### DB migrations
After modifying model you need to create migration files. Run:

`docker-compose run --rm api python manage.py makemigrations`

Make sure to commit newly created migration files.

### Debugging

In order to debug tests or api you can use PDB. Set a breakpoint in code with:

`import pdb; pdb.set_trace()`

Run tests with:

`docker-compose run --rm api python manage.py test core.code_systems --keepdb -v3`

Run api with:

`docker-compose run --rm --service-ports api`

### Release

Every build is a candidate for release.

In order to release please trigger the release build step in [our CI](https://ci.openmrs.org/browse/OCL-OCLAPI2/latest). Please note
that the maintenance version will be automatically increased after a successful release. It is desired only, if you are releasing the latest build and
should be turned off by setting the increaseMaintenanceRelease variable to false on the Run stage "Release" popup in other cases.

A deployment release will be automatically created and pushed to the staging environment.

#### Major/minor version increase

In order to increase major/minor version you need to set the new version in [core/\_\_init\_\_.py](core/__init__.py). Alongside you need to login to our CI and update the next release version on a deployment plan [here](https://ci.openmrs.org/deploy/config/configureDeploymentProjectVersioning.action?id=205619201) with the same value.

### Deployment

In order to deploy please trigger the deployment [here](https://ci.openmrs.org/deploy/viewDeploymentProjectEnvironments.action?id=205619201).
Please use an existing deployment release.
