AUTHOR = 'cookiecat'
SITENAME = 'cookiecat'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# [KP] 左上角网站名称的链接
SITEURL = 'http://127.0.0.1:8000/'

# [KP] 设置主题
THEME = "/Users/m2fox/hack/github/blog/themes/Pelican-Cid"
THEME_TEMPLATES_OVERRIDES = ['/Users/m2fox/hack/github/blog/themes/Pelican-Cid/templates/']

# [KP] 设置生成的文章的html的文件名（不要是默认的汉语拼音）
FILENAME_METADATA = r'(?P<slug>.*)'
# [KP] 设置文章的URL路径构成
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
