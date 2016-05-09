import redis
import json

with open("az_config.json") as data_file:
    data = json.load(data_file)

r = redis.StrictRedis(
    host=data["redis_host"],
    port=6380,
    db=0,
    password=data["redis_key"],
    ssl=True
)

# r.set('foo', 'bar')
value = r.get('foo')
print value 