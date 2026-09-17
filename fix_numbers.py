import os

css_path = 'd:/Projects/avadhootha law and associates/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to add font-variant-numeric: lining-nums; to the body and headings override.

old_block = """body, p, a, button, input, select, textarea, span {
    font-family: 'Playfair Display', serif !important;
    font-weight: 500 !important;
}

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 700 !important;
}"""

new_block = """body, p, a, button, input, select, textarea, span {
    font-family: 'Playfair Display', serif !important;
    font-weight: 500 !important;
    font-variant-numeric: lining-nums !important;
}

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 700 !important;
    font-variant-numeric: lining-nums !important;
}"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated style.css with lining-nums")
else:
    print("Could not find the block. I will append the lining-nums rule.")
    append_block = "\n* { font-variant-numeric: lining-nums !important; }\n"
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(append_block)
    print("Appended to style.css")
