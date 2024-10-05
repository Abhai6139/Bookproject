from django import forms
from.models import Book,AUTHOR


class Authorform(forms.ModelForm):
    class Meta:
        model=AUTHOR
        fields=['name']


class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter the book author'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book price'})
        }