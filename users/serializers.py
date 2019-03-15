from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields=('email','username','password','is_admin','is_candidate')


class CustomRegisterSerializer(RegisterSerializer):
 is_candidate=serializers.BooleanField()
 is_admin = serializers.BooleanField()
 class Meta:
  model = User
  fields=('email','username','password','is_admin','is_candidate')
 def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_admin': self.validated_data.get('is_admin', ''),
            'is_candidate': self.validated_data.get('is_candidate', ''),
        }

 def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_admin = self.cleaned_data.get('is_admin')
        user.is_candidate = self.cleaned_data.get('is_candidate')
        adapter.save_user(request, user, self)
        
        return user
        print(user)
class TokenSerializer(serializers.ModelSerializer):
       user_type = serializers.SerializerMethodField()

       class Meta:
              model = Token
              fields = ('key','user','user_type')


       def get_user_type(self,obj):
              serializer_data = UserSerializer(
                 obj.user    
              ).data
              is_admin = serializer_data.get('is_admin')
              is_candidate = serializer_data.get('is_candidate')
              return {
                     'is_candidate':is_candidate,
                     'is_admin':is_admin
              }
