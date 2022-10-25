from redisConfig import redis_connection
import time


# define redis stream key and group that we will consume from
key = 'output'
group = 'output-group'

def consumeOutput():
    redis = redis_connection
    try:
        redis.xgroup_create(key, group)
    except:
        print('Group already exists')

    results = {}

    while True:
        try:
            # add delay of 1 seconds to ensure all messages are recieved
            # should be fixed in scaled solution
            time.sleep(1)

            # read from stream and process if there are new messages
            newMsg = redis.xreadgroup(group, key, {key: '>'}, 1)
            
            if newMsg:
                streamMsg = newMsg[0][1]

                for id, value in streamMsg:
                    # get key of value
                    listKey = list(value.keys())[0]
                    streamData = value[listKey]
                    results[listKey] = streamData

                    # acknowledge server recieved and processed item; mark redis status to completed
                    redis.xack(key, group, id)
            else:
                break
                
        except Exception as e:
            print(e)

        #time.sleep(1 )
    return results