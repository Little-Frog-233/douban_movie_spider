# douban_movie_spider
捣鼓了一个下午加晚上的豆瓣电影短评爬虫。

一开始是想用requests爬来着，发现一直是禁止访问403的状态，就算加上登陆的cookie信息也还是403，这就比较尴尬了(豆瓣真的好严格-_-)

好在还有selenium这个神器在，用它来完全模拟人的行为，发现完全可以爬了也～

有几个要注意的地方：
1 第一个函数是用来寻找能够进行登陆的cookie，需要用到你的用户名
2 第二个函数用来爬去评论，本来想用pyquery来解析，发现不行，后改用selenium自带的css_selector来解析
3 最后爬取的页面不宜过多，我自己只是尝试了爬去5页，要是爬得多我也不清楚会不会封IP或者是封号，自己去尝试吧

需要的包：

* selenium
* json
* time
