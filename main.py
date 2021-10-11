import pandas as pd
import newspaper
from newspaper import Article
df = pd.read_csv('Link Berita.csv')
urls = df['data'].to_list()

all_authors = {"author": []}
all_dates = {"dates": []}
all_add_data = {"add":[]}
all_text = {"text":[]}
all_tag = {"tag":[]}
all_title = {"title":[]}
all_keyword = {"keyword":[]}

for url in urls:
    try:
        a = Article(url, language='id')
        a.download()
        a.parse()

        author = a.authors
        dates = a.publish_date
        add_data = a.additional_data
        text = a.text
        tag = a.tags
        title = a.title
        keywords = a.keywords

        all_authors['author'].append(author)  # it need in [] because it can be multiple
        all_dates['dates'].append(dates)  # it need in [] because it can be multiple
        all_add_data['add'].append(add_data)  # it need in [] because it can be multiple
        all_text['text'].append(text)  # it need in [] because it can be multiple
        all_tag['tag'].append(tag)  # it need in [] because it can be multiple
        all_title['title'].append(title)  # it need in [] because it can be multiple
        all_keyword['keyword'].append(keywords)  # it need in [] because it can be multiple



    except Exception as e:
        print(e)

new_df = pd.concat(map([all_text,all_authors])




'''
a = Article(cek,language='id')
b = a.download()
c = a.parse()
author = a.authors
date = a.publish_date
add_data = a.additional_data
text = a.text
tag = a.tags
title = a.title
keywords = a.keywords
combine = {'author':author,'date':date,'text':
text,'add_data':add_data,'tag':tag,'tittle':title,'keyword':keywords}
data = pd.DataFrame(data=combine)


data = []
for url in urls:
    try:
        a = Article(url, language='id')
        a.download()
        a.parse()

    except newspaper.ArticleException as e:
        print(e)

    else:
        author = a.authors
        dates = a.publish_date
        add_data = a.additional_data
        text = a.text
        tag = a.tags
        title = a.title
        keywords = a.keywords

        new_df = pd.DataFrame({'penulis':[author],'tanggal':[dates],'additional':[add_data],'berita':[text],'tags':[tag],'judul':[title],'kata':[keywords]})
        data.append(new_df)

df = pd.concat(data)'''