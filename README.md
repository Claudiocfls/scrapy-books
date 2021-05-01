## Scrapy-books

A simple project using Scrapy to extract books from `http://books.toscrape.com`

## How To Run

```bash
mkdir venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd scrapy_books
scrapy crawl books_spider -o books.csv
```

## Output example

[CSV with the extracted items](https://github.com/Claudiocfls/scrapy-books/blob/main/books.csv)

## Deploy to Cloud

Scrapy spiders can be deployed to the cloud using the Zyte platform. The process is pretty straightforward, just access the platform and follow the instructions.

This is the demo project deployed: `https://app.zyte.com/p/522634/jobs`