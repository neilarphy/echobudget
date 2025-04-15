import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from app.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)

class BaseRabbitConsumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(settings.RABBITMQ_URL)
        )
        self.channel: BlockingChannel = self.connection.channel()
        self.channel.queue_declare(
            queue=settings.RABBITMQ_QUEUE_NAME,
            durable=settings.RABBITMQ_QUEUE_DURABLE,
        )
        self.channel.basic_qos(prefetch_count=1)

    def start_consuming(self):
        logger.info("[*] Starting RabbitMQ consumer...")
        self.channel.basic_consume(
            queue=settings.RABBITMQ_QUEUE_NAME,
            on_message_callback=self.callback_wrapper
        )
        self.channel.start_consuming()

    def callback_wrapper(
            self,
            ch: BlockingChannel,
            method: Basic.Deliver,
            properties: BasicProperties,
            body: bytes,
    ):
        try:
            self.callback(ch, method, properties, body)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            logger.exception(f"Error processing message: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def callback(
            self,
            ch: BlockingChannel,
            method: Basic.Deliver,
            properties: BasicProperties,
            body: bytes,
    ):
        pass