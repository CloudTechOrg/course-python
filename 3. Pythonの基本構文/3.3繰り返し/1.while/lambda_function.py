def lambda_handler(event, context):
    index = 0

    # index < 10 の間、ループする
    while index < 10:
        print(index)
        index += 1
        
    # 出力：0 1 2 3 4 5 6 7 8 9
