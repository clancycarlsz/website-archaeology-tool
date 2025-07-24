# from bs4 import BeautifulSoup

# # Read sample HTML file
# with open('samples/sample.html', 'r') as file:
#     html_content = file.read()

# # Parse HTML and count tags
# soup = BeautifulSoup(html_content, 'html.parser')
# tags = soup.find_all()
# tag_counts = {}
# for tag in tags:
#     tag_name = tag.name
#     tag_counts[tag_name] = tag_counts.get(tag_name, 0) + 1

# # Print results
# print("HTML Tag Counts:", tag_counts)


import os
from bs4 import BeautifulSoup

# Get the directory of parse_html.py
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir  # website_archaeology

files_to_parse = [
    os.path.join(base_dir, "samples/sample.html"),
    os.path.join(base_dir, "datasets/html5-boilerplate/dist/index.html")
]

for file_path in files_to_parse:
    print(f"Parsing {file_path}:")
    if not os.path.exists(file_path):
        print(f"  Error: File {file_path} not found")
        continue
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            tags = {tag.name: len(soup.find_all(tag.name)) for tag in soup.find_all()}
            print({"tags": tags, "total_tags": sum(tags.values())})
    except Exception as e:
        print(f"  Error: HTML parsing failed: {str(e)}")