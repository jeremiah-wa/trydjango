from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 20,
                'cols': 100,
                'placeholder': 'Write away...'
            }
        )
    )

    class Meta:
        model = Article
        fields = [
            "title",
            "content"
        ]
