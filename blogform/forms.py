from django import forms
class fileupload(forms.Form):
    file = forms.ImageField(label='upload file')
    slug=forms.CharField(label='Slug')
    date=forms.DateField()
    content=forms.CharField(label='Content')
    title=forms.CharField(label='Title')
    extract=forms.CharField(label='Extract')
    author=forms.CharField(label='Author')
    postedBy=forms.CharField(label='posted by')