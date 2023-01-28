
from django import forms
from transactions.models import Transaction

class UploadFile(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"