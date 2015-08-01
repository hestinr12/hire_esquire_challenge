# hire_esquire_challenge

The hire an Esquire challenge was to build a CRUD service with the following
requirements:

#### Models
   * Job
     * id: uuid (primary key)
     * TimeEntrys: relationship
     * total_minutes: unsignedint
   * TimeEntry
     * minutes_worked: unsignedint
     * date_stamp: date
     * work_summary: entry
     * related_job: uuid

#### Deployment
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
   * sqlite
 * Devops
   * Ansible
   * AWS ec2

#### Installed packages and services notes

As you may have noticed, there is no Nginx. Attempts were made, but
configurations weren't successful. Future details on a solution coming in the 
future. For now, the Django server runs with behind uWSGI, which run directly
against the web.




## Deployment

#### Devops Notes

The playbook was only tested with AWS, but there shouldn't be any issues
when running locally, just match the version of Ubuntu used by Amazon as
best as possible.

There is a basic devops directory for devops related files. Included now are:

 * playbook.yml for Ansible
 * Unused Nginx files

#### Procedure

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

#### Notes

This is a first attempt at using Ansible, so some revisions are likely. The
playbook is very simplistic, and needs reinforcement. There are plenty of
guides for helping get the deploy key set up. Make sure to add this to the repo
through the side! Ideally, the setup process will become more "one button".



## Changes needed for Production

There is a good amount of prep needed to be ready for production. Let's see
here...
 * Set up a distributed database
   * Setting a distributed memory store (as opposed to in memory/on disk) will allow the app to scale accross machines
   * Allows for larger storage capacity, plus many other benefits
 * Pretty much everything listed in [the Django Deployment checklist](https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/)
   * These steps are needed to ensure the integrity of the Django application
   * Which very much obviously includes disabling the debug modes (which are still enabled at HEAD >.<')
   * The secret key for Django is still published in the settings, this needs fixed!
 * Research and add the correct configuration for setting up uWSGI as a daemon
   * The uWSGI service will be responsible for the interface between the web and the application, so we have to make sure it stays alive
   * A lot of people seemed to use `emperor`...?
 * Properly add and configure Nginx for working with uWSGI
   * Nginx is a great lightweight solution as reverse proxy and can help more easily scale out the app
 * Configure automated testing, build, and deploy scripts to use with CI service/Ansible/AWS
   * Things like:
     * Custom AMI for EC2 (help server boot times)
     * Setup autoscaling groups
     * Using Shippable with the current `python manage.py test`
     * [Dynamic Inventory](https://docs.ansible.com/ansible/intro_dynamic_inventory.html) for easier large scale AWS deployments
     * Automate all the things!





:D
