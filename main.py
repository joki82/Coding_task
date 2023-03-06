from bs4 import BeautifulSoup
from googletrans import Translator

file_path = "/Users/Josip/Desktop/Programiranje/Coding Allstars/Translate/index.html"
# file_path = "/Users/Josip/Desktop/Programiranje/Coding Allstars/Translate/myweb.html"

# Open & read locally saved web page
with open(file_path) as webpage:
    content = webpage.read()
# print(content)

# Google translator
translator = Translator(service_urls=["translate.google.com"])

# Parsing html with beautiful soup
soup = BeautifulSoup(content, "html.parser")
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


with open(file_path, 'w') as file:
    file.write(str(soup))

# print(soup)
