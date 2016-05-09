import redis

r = redis.StrictRedis(
    host='sixshotcache.redis.cache.windows.net',
    port=6380,
    db=0,
    password='4NJYqV6/9+eP1eNu0SYaAunhb6IcgYkPnCt/Si0bsNI=',
    ssl=True
)

r.set('foo', 'bar')
value = r.get('foo')
print value 