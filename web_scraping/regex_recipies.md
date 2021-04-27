# Regex Recipies

This is a collection of useful regex scripts to accomplish specific web scraping tasks
**Remember please check a sites terms and conditions to check whether web scraping is allowed**

Contents
--
| Page Links | Description |
| ---------- | ----------- |
| [Get all html between two html tags](####Get-all-html-between-two-html-tags) | Targets all html between two specified html tags and creates a BeautifulSoup object |


#### Get all html between two html tags
```python
import re
from bs4 import BeautifulSoup

match = re.search(r"<description of start tag including closing tag>.?<tag to stop searching at>", html, re.DOTALL)
start_index = match.start()
end_index = match.end() - len("tag to stop searching at")
target_html = html[start_index:end_index]
soup = BeautifulSoup(target_htmlm "html.parser")
```
Code comes from [stackoverflow - maltman](https://stackoverflow.com/questions/4456679/using-beautifulsoup-to-grab-all-the-html-between-two-tags)
