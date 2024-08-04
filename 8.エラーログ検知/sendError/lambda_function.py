import json
import base64
import gzip
import boto3
import os

# --------------------
# エラーメッセージの取得
# --------------------
def read_error_message(event):
    # Base64エンコードされたログデータをデコード
    log_data_zip = base64.b64decode(event['awslogs']['data'])
    
    # gzipで圧縮されたデータを解凍
    log_data = gzip.decompress(log_data_zip)
    
    # 解凍されたデータをJSONとして読み込む
    log_data_json = json.loads(log_data)
    
    # ロググループを取得
    log_group = log_data_json['logGroup']
    
    # ログイベントごとにメッセージを取得し、リストに追加
    messages = []
    for log_event in log_data_json['logEvents']:
        messages.append(log_event['message'])
    
    # messagesがリスト形式のため、文字列に変換
    message = str(messages)
    
    # エラーメッセージとロググループを返す
    return message, log_group

# --------------------
# エラーメッセージの送信
# --------------------
def send_error_mail(message, log_group):
    # SESクライアントの設定
    ses_client = boto3.client('ses', region_name='ap-northeast-1')

    # 環境変数からメール設定を取得
    from_mail_address = os.environ['FROM_MAIL_ADDRESS']
    to_mail_address = os.environ['TO_MAIL_ADDRESS']
    
    # メールを送信
    response = ses_client.send_email(
        Destination={
            'ToAddresses': [
                to_mail_address
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': "UTF-8",
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': "UTF-8",
                'Data': f"{log_group}でエラーが発生しました",
            },
        },
        Source=from_mail_address,
    )
    
# --------------------
# Main関数
# --------------------
def lambda_handler(event, context):
    # エラーメッセージを取得
    message, log_group = read_error_message(event)
    
    # エラーメッセージがある場合にSES経由でメールを送信
    send_error_mail(message, log_group)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }