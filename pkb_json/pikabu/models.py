# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categorys(models.Model):
    cat_id = models.SmallIntegerField(primary_key=True)
    search_num = models.SmallIntegerField()
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorys'


class Storys(models.Model):
    story_id = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    pron = models.IntegerField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    category = models.ForeignKey(Categorys, models.DO_NOTHING, db_column='category')
    href = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'storys'


class Tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    href = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tags'


class TagsInStorys(models.Model):
    story = models.IntegerField()
    tag = models.ForeignKey(Tags, models.DO_NOTHING, db_column='tag')

    class Meta:
        managed = True
        db_table = 'tags_in_storys'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    nick = models.TextField()

    class Meta:
        managed = True
        db_table = 'users'
