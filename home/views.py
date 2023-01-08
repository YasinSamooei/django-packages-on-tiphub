from django.shortcuts import render
from.models import Article
from hitcount.views import HitCountDetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

def home(request):
    #popular_posts=Article.objects.filter(ratings__isnull=False).order_by('-ratings__average')  #based on average of ratings
    popular_posts=Article.objects.order_by('-hit_count_generic__hits') #based on hit-count
    # recent_posts= Article.objects.order_by('-date')[:6] #based on date of upload
    return render(request,"home/home.html",{'popular_posts':popular_posts })

class ArticleView(HitCountDetailView):
    model = Article
    template_name = 'home/article-detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True    

class ArticleCreate(CreateView):
    model=Article
    fields=['title','description','image','slug']
    template_name="home/article-create.html"
    success_url=reverse_lazy("home:home")