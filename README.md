# 今日头条爬虫项目

## 项目功能与后续功能

- [x] 搜索关键词下载相应文章
- [ ] 搜索关键词下载相应短视频
- [ ] 将所有相关数据存入Mongodb
- [ ] 特定标题下文章或视频数据

## 环境依赖
### 库安装

  ```shell
pip install selenium==3.14.1
```
### 谷歌浏览器
- 版本：86.0.4240.75
- 文章内容页面暂无除自动化外的解决方法

## 说明
1. 头条按关键词搜索的文章，后台json数据会加载出非头条站内的文章，针对此类文章本项目不做处理

2. 时间有限，无法解析文章内容页的js加载方式，除selenium外，暂无更佳解决办法

3. 暂无法使用无头模式，这会让服务器返回空数据

## 使用方式

```python
from toutiao.download_article import SaveArticle

save = SaveArticle()
save.run()
```
- 这种方式会让你自己手动输入关键词。

- 你也可以使用下面的方式

```python
from toutiao.download_article import SaveArticle

save = SaveArticle(keyword = "电商")
save.run()
```
- 在调用时，自己传入关键词参数。

```python
from toutiao.download_article import SaveArticle

save = SaveArticle(offset = 0,keyword = "电商")
save.run()
```
- 该项目默认从首页开始抓取，你可以传入offset参数，指定开始位置
    - 每20为一页

## 其他
- 项目长期维护并更新
