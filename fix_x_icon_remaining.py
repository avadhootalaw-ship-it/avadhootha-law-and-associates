import glob
import re

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        html = f.read()

    # Catch any remaining corrupted X icons like 'd? ?' and replace them
    html = re.sub(
        r'<span style="font-family: Arial, sans-serif; font-weight: bold; font-style: normal; font-size: 1.2em;">.*?</span>',
        '<span style="font-family: Arial, sans-serif; font-weight: bold; font-style: normal; font-size: 1.2em;">&#120143;</span>',
        html
    )

    with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(html)
