from .models import User
from .models import Films
from .models import Favorite
from .models import Views
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["Name", "Email", "Password"]
        widgets = {
            "Name": TextInput(attrs=
                              {
                               'class': 'form-control',
                                'name@example.com': 'Введите Имя',
                                'type': 'text',
                                'id': 'Name',
                                'placeholder': 'Введите Имя',

                              }),
            "Email": TextInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'id': 'floatingInput',
                'type': 'email',
            }),

            "Password": TextInput(attrs=
            {
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'floatingPassword',
                'type': 'password',
            })
        }

