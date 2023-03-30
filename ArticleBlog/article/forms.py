
from django.contrib.auth.models import User
from django import forms
from .models import Article

############################################## Article_Create_Form Başlangıç #####################################
#buradaki 'Article_Create_Form' klasımı ,'Article' modelimden miras alarak yaptım
class Article_Create_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'content',
            'title',
            'article_image',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '3','placeholder': 'Write a question...'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a answer...'}),
            'article_image':forms.FileField(),
        }

    class Meta:
        model=Article
        fields=['content','title','article_image']

############################################## Article_Create_Form Bitiş #####################################


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '3','placeholder': 'Write a question...'}),
        }

    class Meta:
        model=Article
        fields=['content']












# #Article class'ından hangi kısımları alacağımı söyledim 
#     class Meta:
#         model=Article
#         fields=['title','content']