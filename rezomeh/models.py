from django.db import models
from django.contrib.auth import get_user_model

from audioop import reverse

class Home(models.Model):
    FREELANCE_STATUS = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('busy', 'Busy'),
    ]

    name = models.CharField(max_length=155)
    expertise = models.CharField(max_length=155)
    Address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=155)
    freelance_status = models.CharField(
        max_length=15,
        choices=FREELANCE_STATUS,
        default='not_available',
    ) 

    def __str__(self):
        return f"Home by {self.name} on {self.freelance_status}"

class AboutMe(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Servise(models.Model):
    title = models.CharField(max_length=155)
    short_description = models.TextField()  

    def __str__(self):
        return self.title

class Rezomeh(models.Model):
    title = models.CharField(max_length=155)
    short_description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.datetime_created}"

class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=155)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='protfolios')
    description = models.TextField()
    technology = models.CharField(max_length=500) 
    image = models.ImageField(upload_to='images/',  blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio_detail', args=[self.pk])
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    technology = models.CharField(max_length=100) 
    description = models.TextField()
    short_description = models.TextField(blank=True)  
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])


class Comment(models.Model):
    name = models.CharField(max_length=100) 
    message = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Comment author'
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', blank=True, null=True) 
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.datetime_created}"
    
class Contact(models.Model):
    fullname = models.CharField(max_length=155)    
    message = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=155)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.fullname}"
