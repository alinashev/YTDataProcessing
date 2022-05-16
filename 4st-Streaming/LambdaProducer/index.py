import json
from Executor import Executor


def lambda_handler(event, context):
    executor: Executor = Executor()
    executor.execute(event)

    return {
        'statusCode': 200,
        'body': json.dumps('200!')
    }