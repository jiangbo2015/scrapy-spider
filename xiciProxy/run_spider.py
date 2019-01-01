from scrapy import cmdline

cmd_str = 'scrapy crawl xici -o ip.json'
cmdline.execute(cmd_str.split(' '))