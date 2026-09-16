import glob
import re

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        html = f.read()

    # Replace the Appointment button link in the navbar
    html = re.sub(
        r'<a href="contact\.html" class="btn btn-primary py-2 px-4 d-none d-lg-block">Appointment</a>',
        r'<a href="https://wa.me/919448954564?text=Hello%20Avadhoota%20Law%20Associates%2C%20I%20would%20like%20to%20schedule%20an%20appointment." target="_blank" class="btn btn-primary py-2 px-4 d-none d-lg-block">Appointment</a>',
        html
    )

    with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(html)
