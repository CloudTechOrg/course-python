def lambda_handler(event, context):
    for i in range(10):
        print(i)
        if i == 5:
            break # ループを抜ける

    print("ループを抜けました")

    # 出力：0 1 2 3 4 ループを抜けました