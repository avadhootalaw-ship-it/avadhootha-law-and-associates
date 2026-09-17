import glob

html_files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace the phone and email h3 with h4 to make them less heavily bold and huge
    content = content.replace('<h3 class="mb-0">+91 94489 54564, +91 79753 81023</h3>', '<h4 class="mb-0" style="font-weight: 500 !important;">+91 94489 54564, +91 79753 81023</h4>')
    content = content.replace('<h3 class="mb-0">avadhootalaw@gmail.com</h3>', '<h4 class="mb-0" style="font-weight: 500 !important;">avadhootalaw@gmail.com</h4>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated h3 to h4 for contact details.")
