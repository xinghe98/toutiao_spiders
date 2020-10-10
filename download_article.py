from toutiao.factory import TouTiao

class SaveArticle(TouTiao):
    """
    文章保存类
    继承TouTiao类
    """

    def __init__(self,offset = 0,**kwargs):
        super().__init__()
        self.offset = offset
        if 'keyword' in kwargs:
            self.keyword = kwargs.get("keyword")
        else:
            self.keyword = input("请输入搜索关键词：")

    def run(self):
        while True:
            data = TouTiao.article_info(self,self.offset,self.keyword)
            try:
                for info in data:
                    if 'article_url' in info:
                        title = info['title']
                        title = TouTiao.validateTitle(title).replace('?', '').replace('？', '')
                        data = TouTiao.download_article(self,info['article_url'],title)
                        if not data is None:
                            print(title + "   完成")
                        else:
                            print("这不是头条内文章")
                self.offset += 20
            except TypeError as e:
                print('Done')
                break


if __name__ == '__main__':
    save = SaveArticle()
    save.run()