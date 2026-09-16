import glob
import re

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        html = f.read()

    # Remove the empty container that used to hold Terms/Privacy
    html = re.sub(
        r'<div class="h-100 d-inline-flex align-items-center py-3 me-2">\s*</div>',
        '',
        html
    )

    # Add py-3 to the social icons container to restore the topbar's height
    html = html.replace(
        '<div class="h-100 d-inline-flex align-items-center">\n                    <a class="btn btn-sm-square btn-outline-body me-1" href=""><i class="fab fa-facebook-f"></i></a>',
        '<div class="h-100 d-inline-flex align-items-center py-3">\n                    <a class="btn btn-sm-square btn-outline-body me-1" href=""><i class="fab fa-facebook-f"></i></a>'
    )

    with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(html)
