from serpapi import GoogleSearch
import pandas as pd
import newspaper
from newspaper import Article

print("Hallo Tolong Masukkan kata kunci dan tanggal\n")
print("==============================================")
print("Masukkan Tanggal Awal\n")
first_day = int(input())
print("Masukkan Bulan Awal\n")
first_month = int(input())
print("Masukkan Tahun Awal\n")
first_year = int(input())
print("==============================================")
print("Masukkan Tanggal Akhir\n")
last_day = int(input())
print("Masukkan Bulan Akhir\n")
last_month = int(input())
print("Masukkan Tahun Akhir\n")
last_year = int(input())
print("==============================================")
print("Masukkan Keyword\n")
q = str(input())
print("Masukkan perkiraan jumlah\n")
number = int(input())
print("Masukkan 2 huruf bahasa.Bisa dilihat di https://serpapi.com/google-languages\n")
lang = str(input()).lower()
print("Masukkan lokasi berita.Bisa dilihat di  https://serpapi.com/locations-api\n")
loc = str(input()).capitalize()
print("Memulai Mining\n")


params = {
        "tbm":"nws",
        "q":f"{q}",
        "location":f"{loc}",
        "hl":f"{lang}",
        "num":f"{number}",
        "tbs": f"cdr:1,cd_min:{first_month}/{first_day}/{first_year},cd_max:{last_month}/{last_month}/{last_year}",
        "api_key": "69b24ec3aa1e40f4dabf7440adeda63c70adba534a8e8581088661895957c22e",

}


search = GoogleSearch(params)
result = search.get_dict()
news = result['news_results']

link = []

for data in news:
  link.append(data.get('link'))

df = pd.DataFrame({'link':link})

urls = df['link'].to_list()

new_df = pd.DataFrame
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


        pd.DataFrame({'penulis':[author],'tanggal':[dates],'additional':[add_data],'berita':[text],'tags':[tag],'judul':[title],'kata':[keywords]})
        data.append(new_df)

print("Mining Selesai\n")
print("==============================================")
print("Masukkan Nama File\n")
file_name = str(input())
new_df.to_excel(f"{file_name}.xlsx")
