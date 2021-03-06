#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://karanluthra.in/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM ='feeds/%s.atom.xml'

#DELETE_OUTPUT_DIRECTORY = True
#OUTPUT_RETENTION = (('.git'),
#		    ('CNAME'),)

# Following items are often useful when publishing

DISQUS_SITENAME = "blogkaranluthra"
GOOGLE_ANALYTICS = "UA-48523857-1"
TWITTER_USERNAME = "karanluthra06"
GITHUB_URL = 'http://github.com/karanluthra/'
