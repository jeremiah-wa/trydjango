from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=120)  # max_length = required
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'description',
                'class': 'new-class-name two',
                'id': 'id-for-textArea',
                'rows': 20,
                'cols': 40
            }
        ))
    price = forms.DecimalField(decimal_places=2, max_digits=10000)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "qwerty" in title:
            raise forms.ValidationError("This is an invalid title")
