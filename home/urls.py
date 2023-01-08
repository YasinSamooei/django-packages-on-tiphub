from django.urls import path,re_path,include
from .import views

app_name="home"

urlpatterns=[
    path('',views.home,name='home'),
    re_path(r'article/detail/(?P<slug>[-\w]+)',views.ArticleView.as_view(),name="article-detail"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path("create",views.ArticleCreate.as_view(),name="article-create"),

]