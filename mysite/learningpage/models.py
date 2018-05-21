from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class learningpost(models.Model):
    Topic=models.TextField(blank=False,max_length=500,unique=True,default='Here put the topic of your post this is only for the Database entry')
    headline=RichTextField(max_length=500,blank=False,unique=True,default='Here put the Headline of your post')
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    date = models.DateTimeField()
    #body = RichTextField()
    body = RichTextUploadingField()
    links = models.URLField(max_length=500,blank=True)
    website = models.URLField(max_length=250,blank=True)

    def __str__(self):
        return self.Topic

