# 폼 모양을 바꾸기 (기본 아이디+비번만 있음)
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

#상속해줌
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'e_mail', 'phone_number', 'bio', 'profile']