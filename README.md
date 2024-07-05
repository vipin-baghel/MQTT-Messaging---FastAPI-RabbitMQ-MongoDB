# MQTT-Messaging---FastAPI-RabbitMQ-MongoDB
Producer send MQTT msg every second with a "status" field containing a random value between 0 and 6 to RabbitMQ. FasApi server consumes the MQTT msg from RabbitMQ and stores in MongoDB with timestamps. It provides an endpoint that accept timestamp range and return the count of each status within the specified time range using aggregate pipeline.

# Setup guide 


Docker server setup for RabbitMQ, MongoDB:
1. Install docker desktop
2. Navigate to directory that contains docker-compose file
3. Run command to download images - docker-compose pull 
4. Run command to start containers in detached mode - docker-compose up -d
5. Rabbitmq GUI management will be up and running on port 15672 
6. Mongodb admin GUI will be up and running on port 8081 

Server setup for Fastapi:
1. Install python 3.12
2. Navigate to directory of fastapi app 
3. Run command to install dependencies - pip install -r requirements.txt
4. Run command to start fastapi server - uvicorn main:app
5. FastApi app will be up and running on port 8000
6. API swagger UI - localhost:8000/docs


Producer (client script) :
1. Install paho library by running cmd - pip install paho-mqtt
2. Run the python file present in producer folder, it will start sending msgs to Rabbitmq every second. (RabbitMQ server should be up and running)


----

API endpoint to get aggregate data from mongodb - /aggregate

Date and Time Format - YYYY-MM-DD HH:MM:SS.SSS

Example - 

start - 2024-07-05 09:00:00.000

end - 2024-07-05 09:05:00.000


