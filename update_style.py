import re

css_path = 'd:/Projects/avadhootha law and associates/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the primary color
content = content.replace('--primary: #E6B800;', '--primary: #B5914A;')

# Replace the font override block
old_block = """body, h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6, p, a, button, input, select, textarea {
    font-family: 'Playfair Display', serif !important;
}"""

new_block = """body, p, a, button, input, select, textarea, span {
    font-family: 'Playfair Display', serif !important;
    font-weight: 500 !important;
}

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 700 !important;
}"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("Could not find the old block to replace. Maybe already modified?")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated style.css")
