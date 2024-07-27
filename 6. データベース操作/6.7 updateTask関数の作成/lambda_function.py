import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # 1. 入力パラメータのチェック
    if "id" not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('id does not exist')
        }
    
    # 2. 入力パラメータの取得
    item_id = event["id"]  # タスクID
    title = event.get("title")  # タスク概要（存在しない場合はNone）
    details = event.get("details")  # タスク詳細（存在しない場合はNone）
    
    # 3. タイムスタンプの取得
    timestamp = datetime.now().isoformat()  # 例：2024-07-17T23:11:11.541085
    
        
    # 4. DynamoDBリソースの初期化
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    
    # 5. 更新する内容の定義
    update_expression = "SET updatedAt = :updatedAt"
    expression_attribute_values = {
        ':updatedAt': timestamp
    }
    
    if title is not None:
		    # titleがNoneでない場合のみ更新
        update_expression += ", title = :title"
        expression_attribute_values[':title'] = title
    
    if details is not None:
		    # detailsがNoneでない場合のみ更新
        update_expression += ", details = :details"
        expression_attribute_values[':details'] = details
    
    try:
        # 6. DynamoDBにデータを更新
        table.update_item(
            Key={'id': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
    except Exception as e:
        # 7. エラーが発生した場合、ステータスコード500（内部サーバエラー）を返す
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error updating item in DynamoDB: {str(e)}')
        }
    
    # 8. ステータスコード200（正常終了）を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'task updated successfully!',
            'id': item_id
        })
    }

