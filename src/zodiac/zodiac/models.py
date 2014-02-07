# -*- coding: utf-8 -*-

import datetime
from google.appengine.ext import db

class GuestBook(db.Model):
	signe = db.StringProperty()
	frase = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add=True)
