def lambda_handler(event, context):
    # コンテキストデータから情報を取得して表示
    print(f"Lambda関数名: {context.function_name}")
    print(f"割り当てられたメモリサイズ (MB): {context.memory_limit_in_mb}")
    print(f"タイムアウトまでの残り時間 (ms): {context.get_remaining_time_in_millis()}")