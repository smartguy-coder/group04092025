"""Basic connection example.
"""

import redis
import config
import datetime as dt


redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USER,
    password=config.REDIS_PASSWORD,
)


# WRITE

# strings
# redis_client.set('myKey', 'secret data')
# redis_client.set('myKeyTTL', 'secret data', ex=15)
# redis_client.set('myKeyTTL', 'secret data', exat=dt.datetime(year=2026, month=1, day=1, hour=2, minute=15))

# lists
# redis_client.lpush('list-key', 'value init')
# redis_client.lpush('list-key', 'value1')
# redis_client.rpush('list-key', 'value2')
# redis_client.expire('list-key', 10666)

# dicts
# redis_client.hset("user:12345", mapping={'name': "Alise", "age": 26})
# redis_client.hset("user:12345", mapping={"city": "Odesa"})
# redis_client.expire('user:12345', 106666666)
#
#
# # READING
# # strings
# my_key_str = redis_client.get('myKey')
# print(my_key_str)
#
# # lists
# data_from_list = redis_client.lrange('list-key', 0, -1)
# print(data_from_list)
#
# # data_from_dict
# data_from_dict = redis_client.hgetall('user:12345')
# print(data_from_dict)
#
# # DELETE
# redis_client.delete('list-key')

# =======================================================

# counter
redis_client.incr("views", -510)
print(redis_client.get("views"))

# pub/sub
redis_client.publish("channel1", 'Hello')
redis_client.publish("channel1", 'Hello')
redis_client.publish("channel1", 'Hello')
redis_client.publish("channel1", 'Hello')

pubsub = redis_client.pubsub()
pubsub.subscribe('channel1')
pubsub.subscribe('news')

for message in pubsub.listen():
    print(message)
