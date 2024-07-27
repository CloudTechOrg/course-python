def lambda_handler(event, context):
    # 足し算は、+ の記号を使用する
    addition = 20 + 10
    print(addition) # 出力：30

    # 引き算は、- の記号を使用する
    subtraction = 20 - 10
    print(subtraction) # 出力：10

    # 掛け算は、* の記号を使用する
    multiplication = 20 * 10
    print(multiplication) # 出力：200

    # 割り算は、/ の記号を使用する
    division = 20 / 10
    print(division) # 出力：2

    # 割り算の余りは、% の記号で求められる
    remainder = 20 % 7
    print(remainder) # 出力：6