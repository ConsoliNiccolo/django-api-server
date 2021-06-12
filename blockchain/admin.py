from django.contrib import admin
from blockchain.models import Token
from prettyjson import PrettyJSONWidget
from django import forms


class TokenJSONForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = '__all__'
        widgets = {
            'attributes': PrettyJSONWidget(),
        }


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    form = TokenJSONForm
