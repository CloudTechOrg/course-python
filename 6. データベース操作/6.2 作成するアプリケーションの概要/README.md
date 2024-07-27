# 6.2 作成するアプリケーションの概要
- 概要
    - タスクの管理を行うアプリケーションを作る
- Lambda関数
    - 5つのLambda関数を作成し、DynamoDBの操作を行う
        - createTask：タスクの登録
        - indexTask：タスクの一覧検索
        - updateTask：タスクの更新
        - deleteTask：タスクの削除
        - showTask：タスクの詳細検索
- DynamoDB
    - タスクのデータを保存するテーブルを作成
    - テーブル名：tasks
    - テーブルの構成
        
        
        | 項目名 | 説明 | その他 |
        | --- | --- | --- |
        | id | タスクを識別するID（UUID） | キー項目 |
        | title | タスクの概要を表す |  |
        | details | タスクの詳細を表す |  |
        | createdAt | 作成した日時と時刻（タイムスタンプ） |  |
- UUIDとは
    - ほぼ衝突のない一意の識別子を生成する標準規格です
    - Pythonにて自動生成が可能