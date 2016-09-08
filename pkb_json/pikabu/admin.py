from django.contrib import admin

# Register your models here.
from .models import Categorys, Storys, Tags, TagsInStorys, Users


class PikabuCategorys(admin.ModelAdmin):
    list_display = ('cat_id', 'search_num', 'info')
    list_filter = ['cat_id']


class PikabuStorys(admin.ModelAdmin):
    list_display = ('story_id', 'ratio', 'date', 'href')
    list_filter = ['date']

class PikabuTags(admin.ModelAdmin):
    list_display = ('tag_id', 'text', 'href')
    list_filter = ['tag_id']

class PikabuTIS(admin.ModelAdmin):
    list_display = ('story', 'tag')
    list_filter = ['story']

class PikabuUsers(admin.ModelAdmin):
    list_display = ('user_id', 'nick')
    list_filter = ['user_id']




admin.site.register(Categorys,PikabuCategorys)
admin.site.register(Storys,PikabuStorys)
admin.site.register(Tags,PikabuTags)
admin.site.register(TagsInStorys,PikabuTIS)
admin.site.register(Users,PikabuUsers)