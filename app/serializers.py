from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomToken(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['last_password_change'] = str(user.last_password_change)
        return token