from django import forms


class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "border rounded p-2 w-full",
                                                        "cols": "30",
                                                        "rows": "5",
                                                        "placeholder": "Write your review"}))
    image = forms.ImageField(required=False)
