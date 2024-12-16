"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ThreadComment
from django.utils.translation import gettext_lazy

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=gettext_lazy("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class FeedbackPoolingForm(forms.Form):
    feedbacktype = forms.ChoiceField(label="Тип",
                                     widget=forms.Select({'id': 'fbty'}),
                                     choices=[
                                       ("reg", "Обычная"),
                                       ("que", "Вопрос"),
                                       ("rep", "Жалоба"),
                                       ("sug", "Предложение")])
    feedbacktext = forms.CharField(label="Сообщение",
                                   required=True,
                                   widget=forms.Textarea({'id': 'fbte'}))
    publishfeedback = forms.BooleanField(label="Опубликовать",
                                         widget=forms.CheckboxInput({'id': 'fbpu'}),
                                         required=False,)
    siterating = forms.IntegerField(label="Оцените работу сайта от 1 до 10",
                                    widget=forms.NumberInput({'id': 'fbra'}),
                                    min_value=1, max_value=10)
    provideas = forms.ChoiceField(label="Отправить как",
                                  widget=forms.RadioSelect({'id': 'fbas'}),
                                  choices=[
                                      ("user", "пользователь"),
                                      ("anon", "аноним")])

class CommentCreationForm(forms.Form):
    text = forms.CharField(label="Комментарий",
                                   required=True,
                                   widget=forms.Textarea({'id': 'commte'}))
    image_1 = forms.ImageField(label="Изображение",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im1'}))
    image_2 = forms.ImageField(label="Изображение (2)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im2',
                                                                       'class': 'inherit-hidden'}))
    image_3 = forms.ImageField(label="Изображение (3)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im3',
                                                                       'class': 'inherit-hidden'}))
    provideas = forms.ChoiceField(label="Отправить как",
                                    required = True,
                                    widget=forms.RadioSelect({'id': 'commas'}),
                                    choices=[
                                        ("user", "пользователь"),
                                        ("anon", "аноним")])

class ThreadCreationForm(forms.Form):
    title = forms.CharField(max_length = 192, label = "Название", required = True)
    short_desc = forms.CharField(max_length = 512, label = "Краткое описание", required = False)
    theme = forms.ChoiceField(required = True,
                             label = "Тематика", choices = [
                                ("AL", "Инопланетная жизнь"),
                                ("CU", "Таинственные культы"),
                                ("GV", "Правительственный заговор"),
                                ("IL", "Заговор иллюминатов"),
                                ("RI", "Мировая элита"),
                                ("00", "Неспецифический заговор"),
                            ])
    image = forms.ImageField(label="Изображение",
                                    required = False,
                                    widget = forms.ClearableFileInput())

class PostCreationForm(forms.Form):
    title = forms.CharField(max_length = 128, label = "Заголовок")
    short_desc = forms.CharField(required = False, max_length = 512, label = "Краткое описание")
    text = forms.CharField(label = "Основной текст", widget = forms.Textarea())
    image_1 = forms.ImageField(label="Изображение",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im1'}))
    image_2 = forms.ImageField(label="Изображение (2)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im2',
                                                                       'class': 'inherit-hidden'}))
    image_3 = forms.ImageField(label="Изображение (3)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im3',
                                                                       'class': 'inherit-hidden'}))

class MerchCreatorForm(forms.Form):
    name = forms.CharField(max_length = 128, label = "Заголовок", required = True)
    description = forms.CharField(label = "Основной текст", widget = forms.Textarea(), required = True)
    cost = forms.DecimalField(label = "Цена", min_value=0, decimal_places = 2, required = True)
    
    image_1 = forms.ImageField(label="Изображение",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im1'}))
    image_2 = forms.ImageField(label="Изображение (2)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im2'}))
    image_3 = forms.ImageField(label="Изображение (3)",
                                    required = False,
                                    widget = forms.ClearableFileInput({'id': 'im3'}))

class OrderPlacementForm(forms.Form):
    amount = forms.IntegerField(min_value = 1, max_value = 1000, label="Количество")