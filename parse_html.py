from bs4 import BeautifulSoup

# Read sample HTML file
with open('samples/sample.html', 'r') as file:
    html_content = file.read()

# Parse HTML and count tags
soup = BeautifulSoup(html_content, 'html.parser')
tags = soup.find_all()
tag_counts = {}
for tag in tags:
    tag_name = tag.name
    tag_counts[tag_name] = tag_counts.get(tag_name, 0) + 1

# Print results
print("HTML Tag Counts:", tag_counts)