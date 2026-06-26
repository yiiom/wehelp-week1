import urllib.request
from bs4 import BeautifulSoup
import csv

url = "https://www.ptt.cc/bbs/Steam/index.html"

articles_data = []

for page in range(3):

    response = urllib.request.urlopen(url)  # 打開列表頁

    html = response.read()  # 讀取 HTML

    soup = BeautifulSoup(html, "html.parser")  # 解析 HTML

    articles = soup.find_all("div", class_="r-ent")  # 找出所有文章

    for article in articles:

        title_tag = article.find("div", class_="title")  # 找標題區塊

        a_tag = title_tag.find("a")  # 找標題連結

        if a_tag is None:  # 被刪除文章直接跳過
            continue

        title = a_tag.text  # 文章標題

        nrec_tag = article.find("div", class_="nrec")  # 推文區塊

        like_count = nrec_tag.text.strip()  # 推文數

        link = a_tag["href"]  # 文章連結

        article_url = "https://www.ptt.cc" + link  # 完整文章網址

        try:

            response = urllib.request.urlopen(article_url)  # 進入文章頁

            html = response.read()

            article_soup = BeautifulSoup(html, "html.parser")

            meta_values = article_soup.find_all(
                "span",
                class_="article-meta-value"
            )

            if len(meta_values) >= 4:
                publish_time = meta_values[3].text  # 發文時間
            else:
                publish_time = ""

        except:
            publish_time = ""

        articles_data.append([
            title,
            like_count,
            publish_time
        ])

    btn = soup.find("a", string="‹ 上頁")  # 找上一頁按鈕

    url = "https://www.ptt.cc" + btn["href"]  # 換成上一頁網址

with open(
    "articles.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.writer(file)

    for article in articles_data:

        writer.writerow(article)

print("完成")

