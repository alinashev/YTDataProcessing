import boto3


class ServiceSQS:
    
    def __init__(self) -> None:
        self.connect()

    def connect(self) -> None:
        self.sqs = boto3.resource('sqs')
        
    def send_message(self, message_body, queue_name) -> None:
        self.queue = self.sqs.get_queue_by_name(QueueName=queue_name)
        self.queue.send_message(MessageBody=message_body)
        