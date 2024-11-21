from django.db import models

# Create your models here.
CATEGORY_CHOISES= (
    ('WD','Web Development'),
    ('DT','Descktop Development'),
    ('DS','Data Science')

)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=())
    published = models.BooleanField(default= True)
    email = models.EmailField(max_length=(50), null= False, blank= False, default= '....@gmail.com')
    views_count = models.IntegerField(default= 0) 
    category = models.CharField(choices= CATEGORY_CHOISES, max_length= 50, default= 'Enter Your Choice')
