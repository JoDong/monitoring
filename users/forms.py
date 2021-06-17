from django.contrib.auth.hashers import check_password
from django import forms
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="ID")
    password = forms.CharField(label="PW", widget=forms.PasswordInput)

    def clean(self):
        username = self.data['username']
        password = self.data['password']

        try:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                self.add_error('password', '아이디 또는 패스워드가 일치하지 않습니다. - 001')

        except User.DoesNotExist:
            self.add_error('username', '아이디 또는 패스워드가 일치하지 않습니다. - 002')
