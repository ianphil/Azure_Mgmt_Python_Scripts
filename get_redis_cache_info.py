import json
from pprint import pprint

from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.resources.models import ResourceGroup
from azure.mgmt.resource.resources import ResourceManagementClient, ResourceManagementClientConfiguration
from azure.mgmt.redis import RedisManagementClient, RedisManagementClientConfiguration
from azure.mgmt.redis.models import * #RedisResource, RedisListKeysResult, Sku, RedisProperties, Resource, RedisCreateOrUpdateParameters

with open("az_config.json.pw") as data_file:
    data = json.load(data_file)
    
def get_credentials(config_data):
    return UserPassCredentials(
        config_data["username"],
        config_data["password"],
    )

credentials = get_credentials(data)
print "Creds have been delivered from:", credentials.cred_store

group_name = 'fourthward'

redis_client = RedisManagementClient(
    RedisManagementClientConfiguration(
        credentials,
        str(data["subscription_id"])
    )
)

cache_name = 'sixshotcache'
redis_cache = redis_client.redis.get(group_name, cache_name)
print "Redis cache is at:", redis_cache.host_name
pprint(vars(redis_cache))

redis_keys = redis_client.redis.list_keys(group_name, cache_name)
print "The primary key is:", redis_keys.primary_key
# pprint(vars(redis_keys))