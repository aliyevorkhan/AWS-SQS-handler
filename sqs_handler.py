"""
AWS SQS Service class to handling queue messages
"""
import boto3
import environ


class SQSHandler:
    """Initializer for SQS"""
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, queue_name) -> None:
        self.client = self.create_connection(
            aws_access_key_id, aws_secret_access_key, region_name)
        self.queue_url = self.create_queue(queue_name).url

    def create_connection(self, aws_access_key_id, aws_secret_access_key, region_name):
        """
            Creates connection for SQS service for given credentials
        """
        try:
            client = boto3.resource('sqs', aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key, region_name=region_name)
            print("Connection successfully created!")
            return client
        except Exception as exception:
            print(f"Error occurred when connection creation: {exception}")
            return None

    def create_queue(self, queue_name):
        """
            To create queue for given queue_name
            If queue exists it does not create new one
        """
        try:
            response = self.client.create_queue(
                QueueName=queue_name
            )
            print("Queue successfully created!")
            return response
        except Exception as exception:
            print(f"Error occurred when queue creation: {exception}")
            return None

    def show_all_available_queues(self):
        """Shows all the available queues"""
        for queue in self.client.queues.all():
            print(f"Queue: {queue.url}")

    def send_message(self, message_body):
        """To send given message body"""
        try:
            self.client.Queue(url=self.queue_url).send_message(
                MessageBody=message_body)
            print(f"Message:{message_body} -> has been sent")
        except Exception as exception:
            print(f"Error occurred when message sending: {exception}")

    def receive_message(self):
        """To recieve message from initialized queue"""
        receipt = self.client.Queue(url=self.queue_url).receive_messages()
        for message in receipt:
            print(f"Message body: {message.body}")
            print(f"Message: {message}")
            message.delete(
                QueueUrl=self.queue_url, ReceiptHandle=message.receipt_handle)
            print("Message has been read and deleted!")


if __name__ == "__main__":
    env = environ.Env()
    environ.Env.read_env()

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
    REGION_NAME = env("REGION_NAME")
    QUEUE_NAME = 'MyQueue'

    sqs_handler = SQSHandler(
        AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, QUEUE_NAME)
    sqs_handler.show_all_available_queues()
    sqs_handler.send_message("Hello")
    sqs_handler.receive_message()
