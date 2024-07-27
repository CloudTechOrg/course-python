import json
import boto3
import os

def lambda_handler(event, context):
    # 1. DynamoDBリソースの初期化
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    
    try:
        # 2. tasksテーブルから全レコードを取得
        response = table.scan(Limit=50)
        items = response.get('Items', [])
    except Exception as e:
        # 3. エラーが発生した場合、ステータスコード500（内部サーバエラー）を返す
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error index from DynamoDB: {str(e)}')
        }
    
    # 4. ステータスコード200（正常終了）を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'tasks index successfully!',
            'tasks': items
        }, ensure_ascii=False)
    }