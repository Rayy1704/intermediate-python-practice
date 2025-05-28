from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from collections import deque
import re

def crawl(start_url):
    visited = set()
    queue = deque([start_url])  # Initialize the queue with a single starting URL
    excluded_paths = ['assets', 'static', 'images', 'css', 'js','xml','uploads','content','docs']  # Folders to exclude

    with open("emails.txt", "a", encoding="utf-8") as email_file:  # Open the output file
        while queue:
            base_url = queue.popleft()
            if base_url in visited:
                continue
            visited.add(base_url)
            print(f"Visiting: {base_url}")
            try:
                response = urlopen(base_url)  # Open the URL
                soup = BeautifulSoup(response.read(), 'html.parser')
                # Find all text in the page
                page_text = soup.get_text()
                # Extract emails using regex
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', page_text)
                for email in emails:
                    # Check if the email contains the desired keywords
                    if any(keyword in email.lower() for keyword in ['hr', 'human', 'resources','careers','jobs','job','recruitment','recruiter','hiring','talent']):
                        print(f"\n\n\nFound matching email: {email}\n\n\n")
                        email_file.write(email + "\n")  # Write the email to the file
                # Process links on the page
                for tag in soup('a'):
                    link = tag.get('href', None)
                    if link:
                        full_url = link if urlparse(link).netloc else urljoin(base_url, link)
                        # Skip excluded paths
                        if any(excluded in full_url for excluded in excluded_paths):
                            continue
                        if full_url not in visited and urlparse(full_url).netloc == urlparse(base_url).netloc:
                            queue.append(full_url)
            except Exception as e:
                print(f"Error visiting {base_url}: {e}")

# List of initial URLs to crawl





# Start crawling
crawl(input("Enter the URL to start crawling: "))