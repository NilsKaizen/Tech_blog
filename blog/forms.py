from django import forms
from blog.models import Post, Comment

class NewPostForm(forms.ModelForm):
    # insert Validators
    def __init__(self, author, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.author = author

    class Meta(): 
        model = Post
        exclude = ['date_c', 'date_p']
