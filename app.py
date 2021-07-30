__author__ = "Lokanath Reddy E"

import sys
import csv
from hashids import Hashids
import json
from flask import Flask, request

app = Flask(__name__)
hashids = Hashids(min_length=4, salt="KanB@n")


# Writing code by accessing the file.
# Assuming 1st line will be as below
# id,url,short_url
# I am considering my project website as https://local.urlshortner.com


@app.route('/url_shortner', methods=['POST'])
def url_shortner():
    url = request.form["url"] if "url" in request.form else ""
    if not url:
        return "Invalid URL"
    with open('short_urls.csv', 'r') as short_urls_file:
        data = csv.DictReader(short_urls_file)
        for each_url in data:
            if url == each_url["url"]:
                return json.dumps({"status": "success", "short_url": each_url["short_url"]})

    with open('short_urls.csv', 'ab+') as short_urls_file:  # Since i use windows machine its appending extra \
        # new line so i am opening in append in binary mode.
        file_content = list(csv.reader(short_urls_file))
        url_id = len(file_content) + 1  # +1 because we are assuming 1st line will be headings of each column.
        short_url_id = hashids.encode(url_id)
        short_url = "https://local.urlshortener.com/" + short_url_id
        short_url_writter = csv.writer(short_urls_file)
        short_url_writter.writerow([url_id, url, short_url])
        short_urls_file.close()
        return json.dumps({"status": "success", "short_url": short_url})
