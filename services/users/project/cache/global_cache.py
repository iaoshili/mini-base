import redis


def redis_connect() -> redis.client.Redis:
    return redis.Redis(host='redis', port=6379, db=0, password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81")

global_cache = redis_connect()
