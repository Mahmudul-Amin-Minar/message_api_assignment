from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MessageList
urlpatterns = [
    path('messages/', MessageList.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
