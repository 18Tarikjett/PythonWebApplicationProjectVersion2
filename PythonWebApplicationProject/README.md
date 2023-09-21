# PythonWebApplicationProject
Web application project in python for coursework 

This is a Python web application which acts as a help desk ticket service. It utilizes django, docker and an assortment of other dependencies which depending on the environment being constructed on will need installation.

Users can register, login and create, read and update tickets they raise for hardware or software issues. 

Only an admin or superuser role has the permissions required to delete a ticket, this is only available on the admin page so that tickets cannot be accessed and deleted by regular users.

There are 4 main status roles for tickets that occur:

- RESOLVED: 
The ticket has been resolved, no further action is required.

- MINOR:
The problem will not lead to any problems in the future, the problem is not critical to basic functionality of an organisation, and the problem can be easily resolved.

- MAJOR: 
The problem can lead to problems down the line that may be major or critical, the problem should be resolved as soon as possible, and can indirectly affect the performance and business organisation status of a team or company.

- CRITICAL: 
The problem is a direct threat to a company or organisation, the problem can lead to complete business failure and must be immediately resolved as soon as possible. 


Users cannot register as admin roles as this role has multiple CRUD privileges, in an industrial real world environment the administrator would be contacted and asked to be granted permissions of an admin or staff role.


It is highly recommended that you create a virtual environment for this project before activating or installing any dependencies, rather than doing system wide installations. 

Your environment will need docker compose if you do not have it already, the installation guide for docker compose can be found here: https://docs.docker.com/compose/install/


**ALL CDK FILES ARE NOT MY OWN, I HAVE ONLY MADE MINOR ADJUSTMENTS NECESSARY TO RUN MY CODE, ALL RIGHTS GO TO THEIR RESPECTIVE OWNERS**

Usage of the AWS pipeline was based upon the AWS petclinic sample which utilises cdk.

cdk petclinic sample and guide can be found here: https://github.com/aws-samples/aws-apprunner-cdk#license

all adjustments made by me were minor and necessary in order to host the python web application


**SETUP**

1. Clone the repository using {git clone https://github.com/18Tarikjett/PythonWebApplicationProject.git}

2. Set up a virtual environment with python using {python3 -m venv .venv}

3. Activate the virtual environment using {. .venv/bin/activate}

4. Install the requirements using {pip install -r requirements.txt}



