from django import forms
from .models import TransactionDetail


# creating a form

class Transaction_form(forms.ModelForm):
    class Meta:
        model = TransactionDetail
        fields = "__all__"
