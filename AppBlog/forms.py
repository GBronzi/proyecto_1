from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título"
        self.fields['subtitle'].label = "Subtítulo"
        self.fields['content'].label = "Contenido"
        self.fields['image'].label = "Imagen (opcional)"