from django import forms
from .models import FeedbackMessage


class FeedbackMessageForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(
                    attrs={'class': 'feedback__field',
                           'placeholder': 'Иванов Иван Иванович'}
                ))
    phone = forms.CharField(widget=forms.TextInput(
                    attrs={'class': 'feedback__field',
                           'placeholder': '+7 (900) 000 00 00'}
                ))
    email = forms.CharField(widget=forms.TextInput(
                    attrs={'class': 'feedback__field',
                           'placeholder': 'ivanov-ivan@ivanovich.ru'}
                ))
    message = forms.CharField(widget=forms.Textarea(
                    attrs={'class': 'feedback__textarea',
                           'placeholder': 'Текст сообщения или вопрос'}
                ))
    agreement = forms.BooleanField(widget=forms.CheckboxInput(
                    attrs={'class': 'feedback__checkbox _hidden'}
                ))

    class Meta:
        model = FeedbackMessage
        fields = [
            'fullname',
            'phone',
            'email',
            'message',
            'agreement',
        ]