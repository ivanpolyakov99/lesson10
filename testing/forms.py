from django import forms

from testing.models import Test


class MyForm(forms.Form):
    email = forms.EmailField(required=False)
    number = forms.IntegerField()
    text = forms.CharField()

    def clean_number(self):
        if self.cleaned_data['number'] < 0:
            raise forms.ValidationError('Must be >= 0')
        return self.cleaned_data['number']

    def clean_text(self):
        return self.cleaned_data.get('text', '').replace(' ', '')


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'level')

    def clean_name(self):
        exec(self.cleaned_data['name'])
