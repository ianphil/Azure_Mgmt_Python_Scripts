# ############## Azure SDK Setup #######################
# pip install --pre azure
# http://azure-sdk-for-python.readthedocs.io/en/latest/

# ############# Script Setup ###########################
# https://azure-sdk-for-python.readthedocs.io/en/latest/resourcemanagement.html

# ############# RHEL Server #########################
# https://github.com/Azure/azure-quickstart-templates/tree/master/101-vm-simple-rhel

# My intellect's devour
# With Diesel Power
# Blows your mind drastically, fantastically
# -The Prodigy

import json
from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.resources import ResourceManagementClient, ResourceManagementClientConfiguration
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.mgmt.resource.resources.models import Deployment
from azure.mgmt.resource.resources.models import DeploymentProperties
from azure.mgmt.resource.resources.models import DeploymentMode
from azure.mgmt.resource.resources.models import ParametersLink
from azure.mgmt.resource.resources.models import TemplateLink
# from pprint import pprint

with open("az_config.json") as data_file:
    data = json.load(data_file)
    
def get_credentials(config_data):
    return UserPassCredentials(
        config_data["username"],
        config_data["password"],
    )

credentials = get_credentials(data)
print "Creds have been delivered from:", credentials.cred_store

resource_client = ResourceManagementClient(
    ResourceManagementClientConfiguration(
        credentials,
        str(data["subscription_id"])
    )
)

group_name = 'ether'
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

deployment_name = 'etherPadDepl'

template = TemplateLink(
    uri='https://raw.githubusercontent.com/tripdubroot/Azure_Mgmt_Python_Scripts/master/azuredeploy.json',
)

parameters = ParametersLink(
    uri='https://raw.githubusercontent.com/tripdubroot/Azure_Mgmt_Python_Scripts/master/azuredeploy.parameters.json',
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

print "Created Deployment:", deployment_name