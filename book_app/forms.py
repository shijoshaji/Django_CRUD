from django.forms import fields
from book_app.models import Review
from django import forms


# creating forms with models, so commenting below logic and creating new
class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']
        labels = {
            'body': 'Review Comments:',
            'image': ''
        }
        help_texts = {
            'body': 'Feedback on this book',
        }

        widgets = {
            'body': forms.Textarea(attrs={"class": "border rounded p-2 w-full",
                                          "cols": "30",
                                          "rows": "5",
                                          "placeholder": "Write your review"}),
        }


# created forms
# class ReviewForm(forms.Form):
#     body = forms.CharField(widget=forms.Textarea(attrs={"class": "border rounded p-2 w-full",
#                                                         "cols": "30",
#                                                         "rows": "5",
#                                                         "placeholder": "Write your review"}))
#     image = forms.ImageField(required=False)
