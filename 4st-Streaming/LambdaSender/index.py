from typing import Any
from LambdaSender.Extractor import Extractor


def lambda_handler(event, context):
    tasks = list()
    response: Any = Extractor().extract()
    for i in response['items']:
        try:
            tasks.append(i['id'])
        except KeyError:
            print("KeyError: ", i['id'])
            continue

    return {
        'statuscode': 200,
        'body': {'taskList': tasks}
    }