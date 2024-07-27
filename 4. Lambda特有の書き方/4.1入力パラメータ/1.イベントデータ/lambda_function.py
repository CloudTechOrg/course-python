def lambda_handler(event, context):
    print(event) # 入力パラメータの全体を表示
    print(event["test_data"]) # 入力パラメータからtest_dataを取得