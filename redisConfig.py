from redis_om import get_redis_connection

host = "redis-12064.c10.us-east-1-2.ec2.cloud.redislabs.com",
port = 12064,
password = "8yUBlhFgwIl2xOYmnbhNNOQFxca5LR5T",
decode_responses = True

redis_connection = get_redis_connection(
    host = "redis-12064.c10.us-east-1-2.ec2.cloud.redislabs.com",
    port = 12064,
    password = "8yUBlhFgwIl2xOYmnbhNNOQFxca5LR5T",
    decode_responses = True
)