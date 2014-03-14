#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Karan Luthra'
SITENAME = u'Karan Luthra'
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = u'en'
DEFAULT_DATE = ('fs')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

# Formatting for urls
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

MENUITEMS = (('Home','/index.html'),
	     ('Archives','/archives.html'),)

REVERSE_CATEGORY_ORDER = True

# Blogroll
LINKS =  (('Jai Luthra', 'http://jailuthra.in/'),
          ('Rishab Arora', 'http://blog.rishab.in/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/karanluthra/'),
          ('Facebook', 'http://facebook.com/karanluthra06'),
          ('Twitter', 'https://twitter.com/karanluthra06'),
          ('Google+', 'https://plus.google.com/+KaranLuthra06'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
