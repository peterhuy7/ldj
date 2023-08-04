from django import forms
 
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=3,
    widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)
 
class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
from myapp.models import Article
from myapp.forms import ArticleForm

# Create a form instance from POST data.
f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form.
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()