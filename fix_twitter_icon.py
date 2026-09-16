import glob

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        content = f.read()

    # Replace the broken ?? with the HTML entity for 𝕏
    content = content.replace(
        '<span style="font-family: Arial, sans-serif; font-weight: bold; font-style: normal; font-size: 1.2em;">??</span>',
        '<span style="font-family: Arial, sans-serif; font-weight: bold; font-style: normal; font-size: 1.2em;">&#120143;</span>'
    )

    with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(content)
