from scrapy import cmdline

cmd_str = 'scrapy crawl music -o music.json'
cmdline.execute(cmd_str.split(' '))