from django import forms

class PostForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }