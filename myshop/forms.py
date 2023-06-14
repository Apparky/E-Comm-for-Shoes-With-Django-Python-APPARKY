from django import forms
from .models import *
from django.db import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_US
        fields = "__all__"
