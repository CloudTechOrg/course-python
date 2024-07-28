import json
import boto3

def lambda_handler(event, context):
    # 1. 入力パラメータの取得
    item_id = event.get('id') or event.get('pathParameters', {}).get('id')
    
    # 2. 入力パラメータが空白の場合は、エラーとする
    if not item_id:
        return {
            'statusCode': 400,
            'body': json.dumps('id does not exist')
        }

    # 3. DynamoDBリソースの初期化
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tasks')
    
    try:
        # 4. DynamoDBからデータを取得
        response = table.get_item(
            Key={'id': item_id}
        )
        item = response.get('Item')
        
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps('Item not found')
            }
    
    except Exception as e:
        # 5. エラーが発生した場合、ステータスコード500（内部サーバエラー）を返す
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error show item from DynamoDB: {str(e)}')
        }
    
    # 6. ステータスコード200（正常終了）を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'task show successfully!',
            'item': item
        }, ensure_ascii=False)
    }
