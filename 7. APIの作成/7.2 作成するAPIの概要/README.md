# 7.2 作成するAPIの概要
- APIのエンドポイント（入口）として、API Gatewayを使用する（API名：`taskAPI`）
- `taskAPI`にて、メソッドタイプとパスパラメーターによって、該当するLambda関数を実行
    - パスパラメーター：https://example.com/`{id}`

    | メソッド | パスパラメーター | ヘッダー | 実行するLambda関数 |
    | --- | --- | --- | --- |
    | GET | {id} | なし | showTask |
    |  | なし | なし | indexTask |
    | POST | なし | title, details | createTask |
    | PUT | なし | id, title, details | updateTask |
    | DELETE | なし | id | deleteTask |
- 今回の講座では
    - API GatewayからLambda関数を呼び出す方法を扱う
    - API Gatewayの詳細説明は省略 → CloudTechの関連講座を参照