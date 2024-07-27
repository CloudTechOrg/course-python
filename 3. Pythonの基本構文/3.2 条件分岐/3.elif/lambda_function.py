def lambda_handler(event, context):
    if score == 100:
        message = "大変良くできました"
    elif score >= 60:
        message = "あと一息です"
    else:
        message = "もっと頑張りましょう"
        
    # 出力：
    # scoreが100である場合は、「大変良くできました」
    # storeが100ではなく、60以上の場合は「あと一息です」
    # それ以外の場合は、「もっと頑張りましょう」
