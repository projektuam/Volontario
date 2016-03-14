# -*- coding: utf-8 -*-
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form): 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nazwa uzytkownika"), error_messages={ 'invalid': _("Nazwa uzytkownika moze zawierac litery, cyfry i znak podkreslenia.") })
    password1 = forms.RegexField(regex=r'^[\w\@\$\%\!\+\=\-]{8,}$', widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Haslo"), error_messages={ 'invalid': _("Haslo musi zawierac minimum 8 znakow (litery, cyfry, znaki: -,_,@,$,%,!,+,=") })
    password2 = forms.RegexField(regex=r'^[\w\@\$\%\!\+\=\-]{8,}$', widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Potwierdz haslo"))
    first_name = forms.RegexField(regex=r'^[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź]+[ ]?[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Imie"))
    last_name = forms.RegexField(regex=r'^[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź]+[ ]?[-]?[ ]?[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("Nazwisko"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Adres email"))
    tel = forms.RegexField(regex='^[5-9][0-9]{2}[ ]?[0-9]{3}[ ]?[0-9]{3}$', widget=forms.TextInput(attrs=dict(required=True, max_length=12)), label=_("Telefon"), error_messages={ 'invalid': _("Wprowadz poprawny numer telefonu, zapisany w formacie 123456789 lub 123 456 789") })
    indeks = forms.RegexField(regex=r'^[0-9]{6}$', required=False, label=_("Indeks"), error_messages={ 'invalid': _("Wprowadz 6-cio cyfrowy numer indeksu") })
    
    
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
