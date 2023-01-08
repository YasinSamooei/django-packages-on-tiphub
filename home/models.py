from django.db import models
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from comment.models import Comment
class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image=models.ImageField(upload_to='Image',verbose_name="تصویر ")
    slug = models.SlugField(unique=True,verbose_name="آدرس",allow_unicode=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    ratings = GenericRelation(Rating, related_query_name='foos')
    # date = models.DateTimeField()
    comments=GenericRelation(Comment)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:article-detail' , args=[self.slug])



   
