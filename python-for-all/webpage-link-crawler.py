from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from collections import deque
from bs4 import BeautifulSoup
def crawl(start_url):
    visited = set()
    queue=deque([start_url])
    while queue:
        base_url = queue.popleft()
        if base_url in visited:continue
        visited.add(base_url)
        print(f"Visiting : {base_url}")
        try:
            for tag in BeautifulSoup(urlopen(base_url).read(), 'html.parser')('a'):
                link = tag.get('href', None)
                if link:
                    full_url = link if urlparse(link).netloc else urljoin(base_url, link)
                    if urlparse(full_url).netloc!=urlparse(base_url).netloc : continue
                    title = tag.get('title', None)
                    text = tag.text.strip()
                    info = (
                        f"title => {title}, text => {text}" if title and text else
                        f"title => {title}" if title else
                        f"text => {text}" if text else
                        f"Alternate Text => {tag.find('img').get('alt')}" if tag.find('img') and tag.find('img').get('alt') else
                        "no info"
                    )
                    print(info + " : " + full_url)
                    queue.append(full_url)
        except Exception as e:
            print(f"Error visiting {base_url}: {e}")
crawl(input("Enter Your Link : "))  # Replace with the starting URL you want to crawl