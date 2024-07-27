import boto3

def lambda_handler(event, context):
    # Boto3クライアントの作成
    s3 = boto3.client('s3')

    # S3バケットの一覧を取得
    response = s3.list_buckets()
    print(f"response:{response}")
    
    # 結果をコンソールに出力
    print("S3バケットの一覧を表示します:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")