'''
    Python script that grabs Azure subscription information
    using username/password.
    
    @tripdubroot is to blame!
'''
import json

# Import Azure Credentials
from azure.common.credentials import UserPassCredentials

# Import Azure Subscription
from azure.mgmt.resource.subscriptions import SubscriptionClient, SubscriptionClientConfiguration
from azure.mgmt.resource.subscriptions.models import SubscriptionPaged, LocationPaged

# Read json file that contains SubID/Username/Password
with open("az_config.json") as data_file:
    data = json.load(data_file)

# Get auth token using OAuth
def get_credentials(config_data):
    return UserPassCredentials(
        config_data["username"],
        config_data["password"],
    )

credentials = get_credentials(data)
print "Creds have been delivered from:", credentials.cred_store

# Setup Subscription client
subscription_client = SubscriptionClient(
    SubscriptionClientConfiguration(
        credentials
    )
)

# Get subscription info using subscription id
subscription_info = subscription_client.subscriptions.get(data["subscription_id"])
print "The name of the current subscription is:", subscription_info.display_name