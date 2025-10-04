from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Expression', max_length=255)
