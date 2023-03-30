from django.db import models

# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Makale")# bunu django hazır kullanıcı tablosundan alıyoruz
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=models.TextField(verbose_name="İçerik")
    article_image=models.FileField(blank=True, null=True, verbose_name="Makaleye Fotoğraf Ekleyin")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return  'author={0}, title={1}'.format(self.author, self.title)#self.title,self.content,self.created_date


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Yorum Yapılan Makale",related_name="comments")#Article Sınıfımız
    comment_author=models.CharField(max_length=50,verbose_name="Yorum Yapanın İsmi")#Yorum Yapanın ismi
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturma Tarihi")
    def __str__(self):
        return self.comment_content






