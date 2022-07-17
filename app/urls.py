from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import CustomView, NewView

from django.urls import path

urlpatterns = [
    path('api/token/', CustomView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', NewView.as_view())
]