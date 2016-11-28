#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dave Carlson'
SITENAME = u'Pelican Blog'
SITEURL = ''

MARKUP = ('md', 'ipynb')
PATH = 'content'

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'
BOOTSTRAP_THEME = 'yeti'
PYGMENTS_STYLE = 'vs'
BOOTSTRAP_NAVBAR_INVERSE = True
TYPOGRIFY = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search', 'ipynb.markup', 'tag_cloud', 'related_posts']

MD_EXTENSIONS = ['codehilite(css_class=codehilite)', 'extra']
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search')
STATIC_PATHS = ['favicon.ico', 'CNAME', 'static/ipython.css']
IGNORE_FILES = ['.ipynb_checkpoints']

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']
USE_FOLDER_AS_CATEGORY = False

RELATIVE_URLS = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
HIDE_SIDEBAR = True
TIPUE_SEARCH = True
SUMMARY_MAX_LENGTH = 150

MENUITEMS = [
    ('Tags', '/tags.html'),
    ('Archives', '/archives.html'),
    ('About', '/pages/about.html')
]

IPYNB_IGNORE_CSS = True
CUSTOM_CSS = 'static/ipython.css'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
