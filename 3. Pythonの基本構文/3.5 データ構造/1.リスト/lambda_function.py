def lambda_handler(event, context):
    # ------------------------------
    # リストの使い方
    # ------------------------------
    my_list = [1, 2, 3, 4, 5] # リストの定義
    print(my_list) # 出力 1, 2, 3, 4, 5

    for value in my_list:
        print(value) 

    # ------------------------------
    # 要素番号によるアクセス
    # ------------------------------
    my_list = [1, 2, 3, 4, 5]
    print(my_list[0]) # 出力 1
    print(my_list[1]) # 出力 2
    print(my_list[2]) # 出力 3
    print(my_list[3]) # 出力 4
    print(my_list[4]) # 出力 5

    # ------------------------------
    # 値の格納
    # ------------------------------
    my_list = [1, 2, 3, 4, 5] 
    print(my_list) # 出力 1, 2, 3, 4, 5

    my_list[2] = 9 # 特定の要素の値を変更

    print(my_list) # 出力 1, 2, 9, 4, 5