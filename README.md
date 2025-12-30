# blog
我的博客

# 链接
- [Pelican Quickstart](https://getpelican.com/#quickstart)

# TMP
## quick start
- 安装pip依赖：

```bash
pip3 install "pelican[markdown]"
```

- 在当前目录初始化博客：

```bash
pelican-quickstart
```

注：如果报错说`pelican-quickstart`命令找不到，则可以这样解决：

```bash
# 先查看python的安装路径：
python3 -m site --user-base

# 然后在"~/.bashrc"文件中加入：
export PATH="$PATH:<上面的安装路径>/bin"

# 然后：
source ~/.bashrc
```

- 写博客，在`content`目录下创建一个markdown文件：`hi-pelican.md`，内容：

```text
Title: Hi Pelican
Date: 2020-01-01 00:00
Category: Hi

Hi, pelican!
```

- 启动博客：

```bash
pelican content -r -l -p 8000 -b 0.0.0.0 --ignore-caceh
# 注：命令行参数解释：
```

- 在浏览器打开`http://localhost:8000/`预览博客。


## 设置cid极简主题
- 下载主题：https://github.com/hdra/Pelican-Cid
- 在博客根目录创建themes目录，把cid的代码全部放到themes目录下面。
- 在`pelicanconf.py`文件中添加配置：

```python
THEME = "/Users/m2fox/hack/github/blog/themes/Pelican-Cid"
THEME_TEMPLATES_OVERRIDES = ['/Users/m2fox/hack/github/blog/themes/Pelican-Cid/templates/']
```

## 博客微调
### TODO 在首页只展示文章的摘要，不要展示截断的文章内容
### TODO 自定义文章的URL
### TODO 修改右上角菜单栏

