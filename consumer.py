from main import redis
import json
import isCycle

# define redis stream key and group that we will consume from
key = 'input_recieved'
group = 'input-group'

try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists')


while True:
    try:
        # read from stream and process if there are new messages
        newMsg = redis.xreadgroup(group, key, {key: '>'}, 1)
        
        if newMsg:
            streamMsg = newMsg[0][1]

            for id, value in streamMsg:
                
                # get key of value
                listKey = list(value.keys())[0]
                streamData = value[listKey]

                # deserialize list to be checked if it is perfect cycle
                valueDeserialized = json.loads(streamData)

                isListNCycle = isCycle.isListCycle(valueDeserialized)

                # publish result to output redis stream to be fetched in the output consumer
                publishMsg = {listKey: str(isListNCycle)}
                redis.xadd('output', publishMsg)
    except Exception as e:
        print(e)
