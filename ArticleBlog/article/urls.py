from django.urls import path
from .import views

app_name="article"
urlpatterns = [
    path('article_show/',views.article_show,name="article_show"),
    
    path('article_delete/<int:id>',views.article_delete,name="article_delete"),
    path('article_create/',views.article_create,name="article_create"),
    path('article_update/<int:id>',views.article_update,name="article_update"),
    path('article_detail/<int:id>',views.article_detail,name="article_detail"),
    path('comment/<int:id>',views.addComment,name="addComment"),
    path('article',views.article,name="article"),

]
