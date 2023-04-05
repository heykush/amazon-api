#for reference check this library 

#https://github.com/sergioteula/python-amazon-paapi

from amazon_paapi import AmazonApi

access_key = ''
secret_key = ''
associate_tag = ''
country = 'IN'

amazon = AmazonApi(access_key, secret_key, associate_tag, country, throttling=60)
#throttling in seconds  
item = amazon.get_items('B0BSFSKZ9N')[0]

print(item.item_info.title.display_value)
