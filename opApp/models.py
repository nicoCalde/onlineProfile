from django.db import models

# Create your models here.
class IndexSkillSet(models.Model):
    favicon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    last = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} {self.last}'

class Skills(models.Model):
    DOMAINS = (
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Database', 'Database'),
        ('Version control', 'Version control'),
        ('Cloud services and platforms', 'Cloud services and platforms'),
        ('Data Analysis', 'Data Analysis'),
        ('API tools', 'API tools'),
        ('Development environments', 'Development environments'),
        ('Currently Learning', 'Currently Learning'),
        ('Coming Next', 'Coming Next'),
    )
    domain = models.CharField(max_length=100, choices=DOMAINS)
    name = models.CharField(max_length=50)
    link = models.URLField()
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def delete(self,using=None,keep_parents=False):
        self.logo.delete(self.logo.name)
        super().delete()

class Works(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    skills = models.CharField(max_length=50)
    modal_image =  models.ImageField(upload_to='images/')
    modal_description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    def delete(self,using=None,keep_parents=False):
        self.image.delete(self.image.name)
        super().delete()
    
    def delete(self,using=None,keep_parents=False):
        self.modal_image.delete(self.modal_image.name)
        super().delete()

class Education(models.Model):
    start = models.PositiveSmallIntegerField()
    end = models.PositiveSmallIntegerField(null=True, default=None)
    establishment = models.CharField(max_length=60)
    first = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.first} {self.degree}'

class About(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph