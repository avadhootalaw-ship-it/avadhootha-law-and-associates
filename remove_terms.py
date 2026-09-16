import glob

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        content = f.read()

    # Remove topbar Terms and Privacy
    content = content.replace('<a class="text-body px-2" href="">Terms</a>\n                    <a class="text-body px-2" href="">Privacy</a>', '')
    # Just in case they are on one line or have different spacing
    content = content.replace('<a class="text-body px-2" href="">Terms</a>', '')
    content = content.replace('<a class="text-body px-2" href="">Privacy</a>', '')

    # Remove footer Terms & Condition and Support
    content = content.replace('<a class="btn btn-link" href="#">Terms & Condition</a>', '')
    content = content.replace('<a class="btn btn-link" href="#">Support</a>', '')

    with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(content)
