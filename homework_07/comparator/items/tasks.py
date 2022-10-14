from celery import shared_task

#installed requests
import requests

# need to install lxml
import lxml.html


@shared_task
def parse(self, url):
    try:
        api = requests.get(url)
    except:
        return ...
    tree = lxml.html.document_fromstring(api.text)
    price = tree.xpath(...)

    return price
