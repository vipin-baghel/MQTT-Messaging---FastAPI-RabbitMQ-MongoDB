# MQTT-Messaging---FastAPI-RabbitMQ-MongoDB
Producer send MQTT msg every second with a "status" field containing a random value between 0 and 6 to RabbitMQ. FasApi server consumes the MQTT msg from RabbitMQ and stores in MongoDB with timestamps. It provides an endpoint that accept timestamp range and return the count of each status within the specified time range using aggregate pipeline.
