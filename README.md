# blog
我的博客

# 链接
- [Pelican Quickstart](https://getpelican.com/#quickstart)

# TMP
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
pelican -r -l
```

- 在浏览器打开`http://localhost:8000/`预览博客。

