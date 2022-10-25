from redis_om import get_redis_connection

redis_connection = get_redis_connection(
    host = "",
    port = ,
    password = "",
    decode_responses = True
)