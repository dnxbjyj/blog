# 作者
AUTHOR = 'cookiecat'
# 站点名称
SITENAME = 'cookiecat'
# 博客网站的链接
SITEURL = 'http://127.0.0.1:8000/'
# 文章目录路径
PATH = 'content'
# 时区
TIMEZONE = 'Asia/Shanghai'
# 语言
DEFAULT_LANG = 'zh'

# 主题
THEME = "/Users/m2fox/hack/github/blog/themes/Pelican-Cid"
THEME_TEMPLATES_OVERRIDES = ['/Users/m2fox/hack/github/blog/themes/Pelican-Cid/templates/']

# 文章的html文件名（默认是汉语拼音）
FILENAME_METADATA = r'(?P<slug>.*)'
# 文章的URL路径构成
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# 默认分页
DEFAULT_PAGINATION = False
