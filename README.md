# message_api_assignment with Django & Django REST Framework
# get token
http post http://127.0.0.1:8000/api/api-token-auth/ username=testuser password=testuserpassword

# send message
http post http://127.0.0.1:8000/api/messages/ "Authorization: Token 4c97595f4cbae73346cc73a3c4058fc8493f5b52" message="new message"
