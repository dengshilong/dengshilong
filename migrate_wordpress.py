#coding:utf-8
import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'dengshilong.settings'
import django
django.setup()
import xmltodict
import json
from blog.models import Post,Category,Page
def process_category(d, categories, tags):
    items = d.items()
    d = {}    
    for key,value in items:
        d[key] = value
    name = d['#text']
    if d['@domain'] == 'category':
        categories.append(name)
    else:
        tags.append(name)
if __name__ == "__main__":
    name = sys.argv[1]
    print name
    f = open(name)
    s = f.read()
    result = xmltodict.parse(s)
    #print result
    result = result['rss']
    result = result['channel']
    result = result['item']
    for item in result:
        for key in item:
            pass
            #print key
        id = item['wp:post_id']
        post_type = item['wp:post_type']
        content = item['content:encoded']
        title = item['title']
        publish_time = item['wp:post_date']

        if not (post_type == 'post' or post_type == 'page'):
            continue 
        slug = title
        slug = slug.replace('(','')
        slug = slug.replace(')','')
        slug = slug.replace(' ','-')
        content = content.replace('<div>', '')
        content = content.replace('</div>', '')
        #print item['title'],item['wp:post_type'],item['wp:post_date'],item['wp:post_name'].encode('utf-8'),
        #print item['content:encoded']
        categories = []
        tags = []
        if post_type == 'post':
                if type(item['category']) == list:
                    for d in item['category']:
                        process_category(d, categories, tags)
                else:
                    process_category(item['category'], categories, tags)
        if post_type == 'post':
            post = Post(id=id,title=title,slug=slug,content=content,publish_time=publish_time)
            post.save()
            print title
            for category in categories:
                try:
                    cat = Category.objects.get(name=category)
                except:    
                    cat = Category.objects.create(name=category)
                post.category.add(cat) 
            for tag in tags:
                post.tag.add(tag)
            post.save()
            post.publish_time=publish_time
            post.save()
        else:
            try:
                page = Page(id=id,title=title,slug=slug,content=content,publish_time=publish_time)
                page.save()
                page.publish_time=publish_time
                page.save()
            except:
                pass
