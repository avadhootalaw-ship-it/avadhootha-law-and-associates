import re

with open('d:/Projects/avadhootha law and associates/contact.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    content = f.read()

# Replace the text message with a welcoming message
old_text = """<p class="mb-4">The contact form is currently inactive. Get a functional and working contact form with Ajax & PHP in a few minutes. Just copy and paste the files, add a little code and you're done. <a href="https://htmlcodex.com/contact-form">Download Now</a>.</p>"""
new_text = """<p class="mb-4">Please fill out the form below and we will get back to you as soon as possible.</p>"""
content = content.replace(old_text, new_text)

# Replace the google maps iframe src
# We'll use regex to replace everything between src=" and "
content = re.sub(
    r'src="https://www\.google\.com/maps/embed\?pb=.*?"',
    r'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d248849.8865389658!2d77.49085309489467!3d12.953959988118836!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1670c9b44e6d%3A0xf8dfc3e8517e4fe0!2sBengaluru%2C%20Karnataka!5e0!3m2!1sen!2sin!4v1714500000000!5m2!1sen!2sin"',
    content
)

with open('d:/Projects/avadhootha law and associates/contact.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(content)
