import glob
import os
import re

font_link = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">'

html_files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = re.sub(r'<link[^>]*family=Open\+Sans[^>]*>', font_link, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
        
css_path = 'd:/Projects/avadhootha law and associates/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

custom_css = """
/* Font override */
:root {
    --bs-font-sans-serif: 'Playfair Display', serif;
    --bs-body-font-family: 'Playfair Display', serif;
}

body, h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6, p, a, button, input, select, textarea {
    font-family: 'Playfair Display', serif !important;
}

/* Ensure Font Awesome still works */
.fa, .fas, .far, .fa-solid, .fa-regular {
    font-family: "Font Awesome 5 Free" !important;
}
.fab, .fa-brands {
    font-family: "Font Awesome 5 Brands" !important;
}
"""

if "Playfair Display" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(custom_css)
    print("Updated style.css")
