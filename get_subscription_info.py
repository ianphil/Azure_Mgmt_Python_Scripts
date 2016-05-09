from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.subscriptions import SubscriptionClient, SubscriptionClientConfiguration
from azure.mgmt.resource.subscriptions.models import SubscriptionPaged, LocationPaged
from pprint import pprint
import json

with open("az_config.json.pw") as data_file:
    data = json.load(data_file)
    
def get_credentials(config_data):
    return UserPassCredentials(
        config_data["username"],
        config_data["password"],
    )

credentials = get_credentials(data)
print "Creds have been delivered from:", credentials.cred_store
# pprint(vars(credentials))

subscription_client = SubscriptionClient(
    SubscriptionClientConfiguration(
        credentials
    )
)

subscription_info = subscription_client.subscriptions.get(data["subscription_id"])

print "The name of the current subscription is:", subscription_info.display_name
# pprint(vars(subscription_list))