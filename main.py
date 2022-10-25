#from base64 import decode
from unicodedata import name
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from numpy import product
from redis_om import get_redis_connection
from redisConfig import redis_connection
from outputConsumer import consumeOutput

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

# import redis connection
redis = redis_connection

@app.post('/inputList')
async def inputList(request: Request):

    # get input json that has lists
    input = await request.json()

    # convert json to dictonary
    input_dict = dict(input)

    for key in input_dict:

        # take list of n then add it to a redis stream to be processed by input consumer
        inputn = {key: str(input_dict[key])}
        redis.xadd('input_recieved', inputn)

    # get output from the output stream
    results = consumeOutput()
    for key in results:
        if results[key] == 'True':
            results[key] = True
        else:
            results[key] = False
    return results

@app.get("/")
async def root():
    return {"message": "Hello World"}