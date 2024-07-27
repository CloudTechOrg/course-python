def lambda_handler(event, context):
    for i in range(10):
        if i%2 == 0:
            continue # ループを継続
        print(i)

# 出力：1 3 5 7 9