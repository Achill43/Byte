from django.db import models

# Create your models here.

class Language(models.Model):
    name=models.CharField(max_length=55)
    icon=models.CharField(max_length=50, blank=True, null=True)
    publish=models.BooleanField(default=True)
    intro=models.TextField()
    parent=models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % (self.name)
    class Meta:
        verbose_name='Programm Language'
        verbose_name_plural='Programm Languages'

class Framework(models.Model):
    parent=models.ForeignKey(Language, on_delete=models.PROTECT)
    name=models.CharField(max_length=55)
    publish=models.BooleanField(default=True)
    intro=models.TextField()
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s | %s | %s" % (self.name, self.publish, self.created)
    class Meta:
        verbose_name='Framework'
        verbose_name_plural='Frameworks'

class Post(models.Model):
    name=models.CharField(max_length=55)
    description=models.TextField()
    code=models.TextField()
    result=models.TextField()
    prortamLanguage=models.ForeignKey(Language, on_delete=models.PROTECT)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s"%(self.name)
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

class Brouser(models.Model):
    name=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s"%(self.name)
    class Meta:
        verbose_name='Brouser'
        verbose_name_plural='Brousers'

class BrouserSupport(models.Model):
    brouser=models.ForeignKey(Brouser, on_delete=models.PROTECT)
    post=models.ForeignKey(Post, on_delete=models.PROTECT)
    support=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % (self.brouser.name)
    class Meta:
        verbose_name='BrouserSupport'
        verbose_name_plural='BrouserSupports'