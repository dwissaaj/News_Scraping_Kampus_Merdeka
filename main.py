import pandas as pd
import newspaper
from newspaper import Article
df = pd.read_excel(' 1.xlsx')
urls = df['data'].to_list()


for url in urls:
    try:
        a = Article(url, language='id')
        a.download()
        a.parse()

        author = a.authors
        dates = a.publish_date
        text = a.text
        tag = a.tags
        title = a.title
        keywords = a.keywords

        new_df = pd.DataFrame({'author':[author],'dates':[dates],'text':[text]
                               ,'tag':[tag],'title':[title],'keywords':[keywords]})
    except Exception as e:
        print(e)



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
data = pd.DataFrame(data=combine)'''