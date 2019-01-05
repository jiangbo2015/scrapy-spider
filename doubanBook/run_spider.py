from scrapy import cmdline

cmd_str = 'scrapy crawl douban -o book.json'
cmdline.execute(cmd_str.split(' '))