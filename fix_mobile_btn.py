import glob

html_files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # We want to change the Appointment button class
    # from: class="btn btn-primary py-2 px-4 d-none d-lg-block"
    # to: class="btn btn-primary py-2 px-4 d-block mt-4 mt-lg-0" (adding some margin on mobile)
    
    target = 'class="btn btn-primary py-2 px-4 d-none d-lg-block">Appointment</a>'
    replacement = 'class="btn btn-primary py-2 px-4 d-block mt-4 mt-lg-0">Appointment</a>'
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
