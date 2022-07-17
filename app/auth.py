from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class CustomAuth(JWTAuthentication):
    def get_user(self, validated_token):
        user = super().get_user(validated_token)
        token_last_time_change = validated_token['last_password_change']
        if str(user.last_password_change) ==  token_last_time_change:
            return user
        raise AuthenticationFailed("Invalid token try to login again", code = "bad_token")

