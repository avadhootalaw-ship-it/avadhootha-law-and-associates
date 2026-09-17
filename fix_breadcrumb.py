import glob
import re

html_files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # regex to match <li class="breadcrumb-item"><a class="text-white" href="#">Home</a></li>
    # ignoring exact spaces/quotes just in case
    new_content = re.sub(r'(<a[^>]*href=[\'"])#([\'"][^>]*>Home</a>)', r'\g<1>index.html\g<2>', content)
    new_content = re.sub(r'(<a[^>]*href=[\'"])[\'"]([^>]*>Home</a>)', r'\g<1>index.html\g<2>', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
        count += 1
print(f"Total updated: {count}")
