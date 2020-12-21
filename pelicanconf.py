#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robocenter'
SITENAME = 'MUR OpenSource'
SITEURL = ''
M_SITE_LOGO = 'media/mur-logo.png'
STATIC_PATHS = ['media']
IGNORE_FILES = ['.#*', 'landing.html']
EXTRA_PATH_METADATA = {
    'media/favicon.png': {'path': 'favicon.png'}
}

PATH = 'content'
TIMEZONE = 'Asia/Vladivostok'
DEFAULT_LANG = 'ru'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'

USE_FOLDER_AS_CATEGORY = True
PAGE_PATHS = ['']
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
INDEX_SAVE_AS = 'blog/index.html'
M_BLOG_URL = 'blog/index.html'

M_CSS_FILES = ['/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = ['m.htmlsanity']

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

M_LINKS_NAVBAR1 = [('Проекты', '/pages/projects', '', [
                        #('Middle AUV', '/', ''),
                        ('ElementaryROV', '/pages/elementary-rov', 'elementary-rov'),
                        ('MiddleROV', '/pages/middle-rov', 'middle-rov'),
                        ('HighROV', '/pages/high-rov', 'high-rov'),
                        ('OpenThruster 150', '/pages/open-thruster-150', 'open-thruster-150')
                        ]),
                   ('Инструкции по настройке', '/pages/docs', '', [
                        ('Прошивка RPi Compute Module', '/pages/firmware-rpi', 'firmware-rpi'),
                        ('MiddleAUV: настройка и тестирование', '/pages/setting-up-midauv', 'setting-up-midauv'),
                        ('MiddleAUV: протокол', '/pages/protocol-mur', 'protocol-mur'),
                        ('HighROV: настройка роутера', '/pages/highrov-router', 'highrov-router'),
                        ('HighROV: прошивка по WiFi', '/pages/highrov-ota', 'highrov-ota'),
                        ]),
                   ('Софт', '/pages/docs', '', [
                        ('Сборка MUR IDE', '/pages/building-mur-ide', ''),
                        ('Сборка MUR Simulator', '/pages/building-mur-simulator', ''),
                        #('Сборка RovUI', '/pages/building-rovui', '')
                        ]),
                   ('GitHub', 'https://github.com/murproject', '', []),
                   ]

M_LINKS_FOOTER1 = [('MUR', ''),
                   ('Проект MUR','https://murproject.com'),
                   ('Аппараты', 'https://robocenter.net/goods/kit/')]

M_LINKS_FOOTER2 = [('Документация', ''),
                   ('MUR IDE', 'https://github.com/murproject/mur_ide'),
                   ('MUR Simulator', 'https://github.com/murproject/mur_simulator')]

M_LINKS_FOOTER3 = [('Ссылки', ''),
                   ('GitHub', 'https://github.com/murproject'),
                   ('YouTube','https://www.youtube.com/channel/UCGRhAtYBi-XZ3U5LgmxXUfQ')]

M_LINKS_FOOTER4 = [('Робоцентр', ''),
                   ('Центр развития робототехники','https://robocenter.org'),
                   ('Центр робототехники','https://robocenter.net')]

M_FINE_PRINT = """.. raw:: html

    <!--
    <div class="robot">
        <div class="robot-main">
            <div class="robot-part heart"><div class="back"></div></div>
            <div class="robot-part shoulder-left"></div>
            <div class="robot-part shoulder-right"></div>
            <div class="robot-part arm-left"></div>
            <div class="robot-part arm-right"></div>
            <div class="robot-part body"></div>
        </div>
        <div class="robot-part head"></div>
        <div class="robot-part leg-left"></div>
        <div class="robot-part leg-right"></div>
    </div>
    -->

    <a href="https://robocenter.org/"><img src="/media/robocenter-text.png"></a>

"""

#M_NEWS_ON_INDEX = ("Последние новости", 3)
M_SHOW_AUTHOR_LIST = False
M_HIDE_ARTICLE_SUMMARY = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'mdx_outline': {},
    },
    'output_format': 'html5',
}
