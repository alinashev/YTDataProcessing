import json
from Executor import Executor


def lambda_handler(event, context):
    executor: Executor = Executor()
    executor.execute()

    return {
        'statusCode': 200,
        'body': json.dumps('Data sent to stream!')
    }
