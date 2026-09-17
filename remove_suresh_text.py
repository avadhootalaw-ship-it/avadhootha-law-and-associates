import os

filepath = 'd:/Projects/avadhootha law and associates/profile-suresh.html'

target = '<p class="text-muted" style="font-style: italic;">Final results awaited as per the submitted CV.</p>'
target_alternative = '<p class="text-muted" style="font-style: italic;">Final results awaited as per the submitted \nCV.</p>'

with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

if target in content:
    content = content.replace(target, '')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully removed the text.")
else:
    # Try regex or something else if it doesn't match perfectly
    import re
    new_content = re.sub(r'<p class="text-muted" style="font-style: italic;">\s*Final results awaited as per the submitted\s*CV\.</p>', '', content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully removed the text using regex.")
    else:
        print("Could not find the text to remove.")
