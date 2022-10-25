# Introduction:
This microservice will take in an input of lists in as a json and will trevarse through it with and decided if it is a perfect cycle or not. Please see the expected input (input.json) and output (output.json). In this project we're using Python, Fastapi, and Redis-Streams for publisher and subscriber model.

Required packages:
uvicorn 0.18.3
fastapi 0.85.1
redis 4.3.4
redis-om 0.1.0

Run instructions:
1. Rename the file "redisConfig copy.py" to "redisConfig.py"
2. From Redis cloud create a database and get the following: host, port, and password
3. Enter the information in the "redisConfig.py" and save
4. Run the unit tests with the following command: 'python3 -m unittest test'
5. Start the server using 'uvicorn main:app --reload'
6. In another terminal windwo, start the input consumer using 'python3 consumer.py'
7. If everything is running, you can use postman to send post requests to http://localhost:8000/inputList (make sure the port number is the same as the one running with uvicorn)


Api docs:
http://localhost:8000/docs

Improvement to this project:
An improvement to this project would be to dockerize this application. Also, to make sure we have a scaleable solution we could modify the structure to make it return realtime output with redis streams. 
