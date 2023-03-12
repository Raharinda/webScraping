import re
from urllib.request import urlopen
url = "https://anbidev.github.io/"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_result = re.search(pattern, html, re.IGNORECASE)
title = match_result.group()
title = re.sub("<.*?>","",title)

print(title)