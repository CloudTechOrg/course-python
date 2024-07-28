curl -X PUT <your-api-url>\
     -H "Content-Type: application/json" \
     -d '{
           "id": "<your-task-id>",
           "title": "APIから更新したタスク",
           "details": "更新したタスクの詳細"
         }'
