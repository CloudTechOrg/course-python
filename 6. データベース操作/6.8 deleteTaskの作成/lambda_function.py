import json
import boto3

def lambda_handler(event, context):
    # 1. 入力パラメータのチェック
    if "id" not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('id does not exist')
        }
    
    # 2. 入力パラメータの取得
    item_id = event["id"]  # タスクID
    
    # 3. DynamoDBリソースの初期化
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    
    try:
        # 4. DynamoDBからデータを削除
        table.delete_item(
            Key={'id': item_id}
        )
    except Exception as e:
        # 5. エラーが発生した場合、ステータスコード500（内部サーバエラー）を返す
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error delete item from DynamoDB: {str(e)}')
        }
    
    # 6. ステータスコード200（正常終了）を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'task delete successfully!',
            'id': item_id
        })
    }
