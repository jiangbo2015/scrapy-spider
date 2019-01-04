# spider: music163

### 使用selenium爬取网易云音乐中所有歌单

网易网云音乐网页代码里面内嵌了iframe, 无法通过scrapy直接爬取
（访问内嵌的iframe中的src地址会被重定向, 可以使用scrapy-splash或者selenium爬取,
这里使用了selenium，比较简单
