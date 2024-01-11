from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


def usr_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'blog_{0}/{1}'.format(instance.author.id, filename)

class Post(models.Model):
    
    class PostObjects(models.Model):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=usr_directory_path, blank=True, null=True)
    excepts = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', unique=True, null=False)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')


    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    postObjects = PostObjects()

    #ordenar postagens

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title