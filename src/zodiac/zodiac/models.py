# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Zodiac(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
