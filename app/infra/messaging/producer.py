import pika
import json
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)

def publish_task(task_data: dict):
    connection = pika.BlockingConnection(
        pika.URLParameters(settings.RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(
        queue=settings.RABBITMQ_QUEUE_NAME,
        durable=settings.RABBITMQ_QUEUE_DURABLE
    )

    message = json.dumps(task_data)
    channel.basic_publish(
        exchange="",
        routing_key=settings.RABBITMQ_QUEUE_NAME,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
            )
    )
    logger.info(f"Published task: {message}")
    connection.close()