import json
from pprint import pprint

from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.mgmt.resource.resources import ResourceManagementClient, ResourceManagementClientConfiguration
from azure.mgmt.redis import RedisManagementClient, RedisManagementClientConfiguration
from azure.mgmt.redis.models import Sku, RedisCreateOrUpdateParameters

with open("az_config.json.pw") as data_file:
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

group_name = 'fourthward'
group_exists = False


        
if group_exists == False:
    result = resource_client.resource_groups.create_or_update(
        group_name,
        ResourceGroup(
            location='eastus',
            tags={
                'tag1': 'sixshooter',
            },
        )
    )
    print "Created resouce group:", group_name

redis_client = RedisManagementClient(
    RedisManagementClientConfiguration(
        credentials,
        str(data["subscription_id"])
    )
)

cache_name = 'sixshotcache'
redis_cache = redis_client.redis.create_or_update(
    group_name,
    cache_name,
    RedisCreateOrUpdateParameters(
        sku = Sku(name = 'Basic', family = 'C', capacity = '1'),
        location = "East US"
    )
)

print "Redis cache is in state:", redis_cache.provisioning_state
# pprint(vars(redis_cache))