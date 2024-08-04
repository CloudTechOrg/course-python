import json
import random

def lambda_handler(event, context):
    # 0〜2のランダムな数を生成
    random_number = random.randint(0, 2)
    
    # 0の場合、任意のエラーを発生させる
    if random_number == 0:
        raise Exception("An error has occurred.")
    
    # 1 or 2の場合、正常終了させる
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Success!',
            'random_number': random_number
        })
    }
    
    return response
