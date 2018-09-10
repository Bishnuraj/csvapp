import config, redis

REDIS_HOST = getattr(config, 'REDIS_HOST', 'localhost')
REDIS_PORT = getattr(config, 'REDIS_PORT', 6379)
REDIS_PASSWORD = getattr(config, 'REDIS_PASSWORD', None)
REDIS_DB_INDEX = getattr(config, 'REDIS_DB_INDEX', 0)

redis_connection = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB_INDEX)