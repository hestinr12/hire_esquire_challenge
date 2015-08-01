# hire_esquire_challenge

The hire an Esquire challenge was to build a CRUD service with the following
requirements:

 * Models
  * Job
   * id: uuid (primary key)
   * TimeEntrys: relationship
   * total_minutes: unsignedint
  * TimeEntry
   * minutes_worked: unsingnedint
   * date_stamp: date
   * work_summary: entry
   * related_job: uuid

 * Deployment
  * Dependencies installed from requirements.txt into a virtualenv
  * Stored in GitHub (or BitBucket)
  * README.md included
  * All scripts included
  * Use Ansible for deployment to localhost or ec2


## Current State

The current commit of master (at this stage) should be treated as an early 
version of a stable product. Not production ready. The current stack operates
using the following software:

 * Server
  * ec2
  * Ubuntu 14.04
  * uWSGI
  * virtualenv
  * python2.7
  * Django
 * Devops
  * Ansible

### Installed packages and services notes

As you may have noticed, there is no Nginx. Attempts were made, but
configurations weren't successful. Future details on a solution coming in the 
future. For now, the Django server runs with behind uWSGI, which run directly
against the web.

### Devops Notes

The playbook in /devops should correctly deploy the code in the 
hire_esquire_challenge repo on an AWS EC2 instance with the standard Ubuntu.
See below for more details on setting up Ansible with this repo.


## Deployment

There is a basic devops directory for devops related files. Included now are:

 * playbook.yml for Ansible
 * Unused Nginx files

The steps for deploying are as follows:
 1. Push all code to be deployed into master of repo
 2. [Set up a deploy key](https://developer.github.com/guides/managing-deploy-keys/#deploy-keys)
  * Make sure to name them:
   * Public key: id_rsa.pub
   * Private key: id_rsa
   * Note: Will use more dynamic method in future
  * Make sure to store them in ~/.ssh/ on your local machine
  * There is a lot of room for automation/help in this part
 3. Run `ansible-playbook playbook.yml`

### Notes

This is a first attempt at using Ansible, so some revisions are likely. The
playbook is very simplistic, and needs reinforcement. There are plenty of
guides for helping get the deploy key set up. Make sure to add this to the repo
through the side!

