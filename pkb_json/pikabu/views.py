from django.shortcuts import render
# Create your views here.
from jsonview.decorators import json_view
from .models import Storys
from random import randint
from django.db import connection


@json_view
def anypost(request):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 1 ORDER BY RAND() LIMIT 1")
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def hundred(request):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 100 ORDER BY RAND() LIMIT 1")
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def fivehundred(request):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 500 ORDER BY RAND() LIMIT 1")
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def thousand(request):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 1000 ORDER BY RAND() LIMIT 1")
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def threethousand(request):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 3000 ORDER BY RAND() LIMIT 1")
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}
