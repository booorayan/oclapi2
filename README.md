# oclapi2

The new and improved OCL terminology service v2


## Deploy oclapi2 with Ansible

To deploy the api on ec2 instances group with ansible run:
     `git clone https://github.com/booorayan/oclapi2.git`
     
Then:
      `cd ansible`
      
Install ansible and run the ansible playbook with the command below to deploy the api

      ansible-playbook -i inventory.yaml oclapi-playbook.yaml

The API is accessible for testing at:

      http://oclapi2-elb-463422178.us-east-1.elb.amazonaws.com/swagger
      

Ansible runs the configuration commands on a host that is an AWS EC2 instance `54.196.68.110` configured as a member of an auto scaling group. 

The tasks defined in the ansible playbook prepare the ec2 instance by installing required packages and then deploying containers with docker compose.

First, it installs packages required by docker and adds the docker repository to the system.

It then installs Docker and Docker-Compose and adds the user 'ubuntu' to docker group to enable running docker commands without sudo privileges.

Finally, the play copies the docker-compose.prod file to the ec2 instance, renames it, copies the file with environment variables and spins up the api together with celery, flower and es containers using the command `docker-compose up` 

The docker-compose file used for the deployment is the `docker-compose.prod.yml` file

#### Scalability and Availability

Auto scaling of ec2 instances helps improve the scalability of the api in response to requests received.

The auto scaling group is set up to have a minimum of 4 EC2 instances and a maximum of 6 EC2 instances.

Further, the instances in the auto scaling group have been configured to be provisioned in different availability zones which improves the availability of the api. The api will be accessible even when one availability zone is unavailable.




## Storage 

For the deployment, the Postgres database and Redis were not containerized. 

The deployment utilizes external storage i.e. AWS Postgres RDS (`oclapi2.cj9iazgawc6u.us-east-1.rds.amazonaws.com`) and Elastic cache for redis (`bo-oclapi-redis.e9c1k4.ng.0001.use1.cache.amazonaws.com`), which also have the advantage of offering data backup and facilitating disaster recovery. 

Also, with RDS, it is easy to connect ec2 instances in auto scaling groups to the same database.

Isolating the database from other application services enhances database optimization

Redis in elastic cache is configured as a cluster and can auto scale in response to requests.

The redis cluster also supports multi availability zones improving on the availability of the api


## Load Balancer

The deployment utilizes an AWS application load balancer `oclapi2-elb-463422178.us-east-1.elb.amazonaws.com`, which directs http traffic to different ec2 instances that belong to the same target group/auto scaling group. 

The load balancer improves the api's availability and scalability since requests can still be served even in the event that one/two instances are unavailable.



## Nginx Proxy

Nginx was employed to proxy http requests to the api for security purposes among other reasons.


## Security

To ensure security of the api and the instance, strict security group rules were followed.

Only the ports that required inbound access were exposed, limiting the risk of attack from several ports.


## Monitoring

AWS CloudWatch helps to detect issues and resolve problems with enterprise applications, databases, and workloads. 

It can trigger alarms when metrics (e.g. resource metrics) exceeds a defined threshold


