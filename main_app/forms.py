from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    email = forms.EmailField(label='Почта', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)


class NewsForm(forms.Form):
    title = forms.CharField(max_length=200, label="Заголовок")
    text = forms.CharField(label="Текст")
    image = forms.ImageField(label="Изображение", required=False)


class DMusicForm(forms.Form):
    file = forms.FileField(label="Файл")