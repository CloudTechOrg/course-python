# value1とvalue2として引数を定義
def add(value1, value2):
    print(value1 + value2)

def lambda_handler(event, context):
    add(10, 20)