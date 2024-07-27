import boto3
import botocore
import json

def lambda_handler(event, context):
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()

    except botocore.exceptions.ClientError as e: # boto3クライアントのエラーを検知
        # エラーメッセージをログに出力
        print(e)
        
        # エラーメッセージをレスポンスとして返す
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error occurred while listing S3 buckets',
                'error': str(e) # エラーメッセージを出力
            })
        }

    except Exception as e: # その他のエラーを検知
        # エラーメッセージをログに出力
        print(e)
        
        # エラーメッセージをレスポンスとして返す
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An unexpected error occurred',
                'error': str(e) # エラーメッセージを出力
            })
        }
    
    # S3バケットの一覧を表示
    print("S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'S3 buckets listed successfully',
            'buckets': [bucket['Name'] for bucket in response['Buckets']]
        })
    }

