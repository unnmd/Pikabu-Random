from django.shortcuts import render
# Create your views here.
from jsonview.decorators import json_view
from .models import Storys
from random import randint
from django.db import connection


@json_view
def anypost(request, pron, my):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 1 AND pron = %s AND my = %s ORDER BY RAND() LIMIT 1", [pron, my] )
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def hundred(request, pron, my):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 100 AND pron = %s AND my = %s ORDER BY RAND() LIMIT 1", [pron, my])
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def fivehundred(request, pron, my):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 500  AND pron = %s AND my = %s ORDER BY RAND() LIMIT 1", [pron, my])
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def thousand(request, pron, my):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 1000 AND pron = %s AND my = %s ORDER BY RAND() LIMIT 1", [pron, my])
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}

@json_view
def threethousand(request, pron, my):
	cursor = connection.cursor()
	cursor.execute("SELECT story_id FROM `storys` WHERE `ratio` > 3000 AND pron = %s AND my = %s ORDER BY RAND() LIMIT 1", [pron, my])
	row = cursor.fetchone()
	return {
	    'vratio': list(row),
    	}
