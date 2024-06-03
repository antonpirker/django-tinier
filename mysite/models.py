from django import forms
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email", ]