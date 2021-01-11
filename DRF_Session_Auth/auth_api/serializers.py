from rest_framework import serializers
from auth_api.models import Account
import re

def validate_password(password):
    regex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[-_#])[A-Za-z\d@$!%*#?&]{1,6}$'
    if re.match(regex, password):
        return False
    else:
        return True

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['username', 'name', 'phone', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            name = self.validated_data['name'],
            phone = self.validated_data['phone'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        username = self.validated_data['username']

        errors = {}
        if len(username) > 8:
            errors['username']=[
                'Username should be less than 9 characters'
            ]

        if password != password2:
            errors['password']= ['Passwords must match']

        if validate_password(password):
            if 'password' in errors:
                errors['password'].append('Password should be less than 7 characters and must contain 1 number, 1 character, any of _#-')
            else:
                errors['password'] = ['Password should be less than 7 characters and must contain 1 number, 1 character, any of _#-']

        if len(errors)>0:
            raise serializers.ValidationError(errors)

        account.set_password(password)
        account.save()
        return account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone', 'name']
        extra_kwargs = {
            'username': {'read_only': True}
        }

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'validators': []}
        }

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        accounts = Account.objects.filter(username=username)

        if accounts.count() != 1:
            raise serializers.ValidationError({'username': "Account doesn't exist with this username"})
        
        account = accounts.first()

        if account:
            if not account.check_password(password):
                raise serializers.ValidationError({"password": "Incorrect credentials"})
        return data