# ############## Azure SDK Setup #######################
# pip install --pre azure
# http://azure-sdk-for-python.readthedocs.io/en/latest/

# ############# Script Setup ###########################
# https://azure-sdk-for-python.readthedocs.io/en/latest/resourcemanagement.html

# ############# RHEL Server #########################
# https://github.com/Azure/azure-quickstart-templates/tree/master/101-vm-simple-rhel

from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.resources import ResourceManagementClient, ResourceManagementClientConfiguration
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.mgmt.resource.resources.models import Deployment
from azure.mgmt.resource.resources.models import DeploymentProperties
from azure.mgmt.resource.resources.models import DeploymentMode
from azure.mgmt.resource.resources.models import ParametersLink
from azure.mgmt.resource.resources.models import TemplateLink
from pprint import pprint


subscription_id = '65e7482b-addd-4edf-8d8f-dbfefc56f2e0'

credentials = UserPassCredentials(
    'ian@ianphilpot.onmicrosoft.com',    # Your new user
    'Aw3someP@ss',  # Your password
)

resource_client = ResourceManagementClient(
    ResourceManagementClientConfiguration(
        credentials,
        subscription_id
    )
)

group_name = 'SyntaxCon'
result = resource_client.resource_groups.create_or_update(
    group_name,
    ResourceGroup(
        location='eastus',
        tags={
            'tag1': 'lildiddy',
        },
    )
)

print "Created Resource Group:", group_name
    
deployment_name = 'SyntaxConDep'

template = TemplateLink(
    uri='https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-rhel/azuredeploy.json',
)

parameters = ParametersLink(
    uri='https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-rhel/azuredeploy.parameters.json',
)

result = resource_client.deployments.create_or_update(
    group_name,
    deployment_name,
    properties=DeploymentProperties(
        mode=DeploymentMode.incremental,
        template_link=template,
        parameters_link=parameters,
    )
)

print "Resource Deployment: There are %s exceptions" % result._exception
print "Created Deployment:", deployment_name

# pprint (vars(result))