from django.contrib import admin
# Register your models here.
from.models import Article,Comment
admin.site.register(Comment)
@admin.register(Article) #Admin panelini özelliştirmek için decorater yazıyoruz
class ArticleAdmin(admin.ModelAdmin): #ModelAdmin sınıfından 'ArticleAdmin' nesne türetiyoruz
    list_display = ["author","title","content","created_date"]
    list_display_links = ["author","title","content","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta: #özelleştirmek için Meta yı kullanıyoruz
        
        model = Article #Article sınıfımızı dahil etmiş oluyoruz
