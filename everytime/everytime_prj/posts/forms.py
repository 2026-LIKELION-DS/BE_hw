from django import forms

class Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_anonymous']


    is_anonymous = forms.BooleanField(
        label='익명', 
        required=False, 
        
    )