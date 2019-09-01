from django.contrib import admin
from .models import  *

# Register your models here.
class LanguageDisplay(admin.ModelAdmin):
    list_display=['name', 'created']
    search_fields=['name']
    class Meta:
        models=Language

admin.site.register(Language, LanguageDisplay)


class BSInlineProducts(admin.TabularInline):
    model=BrouserSupport
    extra=6 #Додаткові поля при виведені масиву ImageForProduct 

class PostDisplay(admin.ModelAdmin):
    list_display=['name', 'prortamLanguage', 'created']
    search_fields=['name', 'description']
    inlines=[BSInlineProducts]
    class Meta:
        models=Post

admin.site.register(Post, PostDisplay)

class BrouserDisplay(admin.ModelAdmin):
    list_display=['name', 'created']
    search_fields=['name']
    class Meta:
        models=Brouser

admin.site.register(Brouser, BrouserDisplay)

class BrouserSupportDisplay(admin.ModelAdmin):
    list_display=['support']
    class Meta:
        models=BrouserSupport

admin.site.register(BrouserSupport, BrouserSupportDisplay)