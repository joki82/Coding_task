import requests
from googletrans import Translator
from bs4 import BeautifulSoup

web_to_scrape = "https://www.classcentral.com"
file_path = "/Users/Josip/Desktop/Programiranje/Coding Allstars/Translate/index.html"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
response = requests.get(web_to_scrape, headers=HEADERS)

# 200 ok
# print(response)

# Google translator
translator = Translator(service_urls=["translate.google.com"])

# Parsing html with beautiful soup
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
elements = ["p", "h2", "h3", "h4", "h5", "title", "a"]

# Loop trought web page content looking for elements with text and replacing it with translated text
for element in soup.findAll(name=elements):
    try:
        hindu = translator.translate(element.text, dest="hi")
        print(hindu.text)
        # element.replace(element.text, hindu.text)
        element.replace_with(hindu.text)
    except IndexError:
        pass
        # print(element)
    except TypeError:
        pass
        # print(element)
    finally:
        with open(file_path, 'w') as file:
            file.write(str(soup))


