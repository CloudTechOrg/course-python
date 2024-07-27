import json
import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    # 1. 入力パラメータのチェック
    if "title" not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('title does not exist')
        }
    
    # 2.入力パラメータの取得
    title = event["title"]  # タスク概要
    details = event.get("details", "")  # タスク詳細（存在しない場合は空白）
    
    # 3.idの生成（uuidを取得）
    item_id = str(uuid.uuid4()) # 例：058b2f0a-985a-4fa1-8d42-5c1313f1c0c4
    
    # 4.タイムスタンプの取得
    timestamp = datetime.now().isoformat() # 例：2024-07-17T23:11:11.541085
    
    # 5.DynamoDBリソースの初期化
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    
    # 6.DynamoDBに更新するitemの内容を辞書で定義
    item = {
        'id': item_id,
        'title': title,
        'details': details,
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    
    try:
        # 7.DynamoDBにデータを保存
        table.put_item(Item=item)
    except Exception as e:
        # 8.エラーが発生した場合、ステータスコード500（内部サーバエラー）を返す
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error saving item to DynamoDB: {str(e)}')
        }
    
    # 9.ステータスコード200（正常終了）を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'task saved successfully!',
            'id': item_id
        })
    }
