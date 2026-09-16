import re

with open('d:/Projects/avadhootha law and associates/contact.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    content = f.read()

# Replace the form tag
content = content.replace('<form>', '<form action="https://formsubmit.co/avadhootalaw@gmail.com" method="POST">')

# Add name and required attributes to inputs
content = content.replace('id="name" placeholder="Your Name"', 'id="name" name="Name" placeholder="Your Name" required')
content = content.replace('id="email" placeholder="Your Email"', 'id="email" name="Email" placeholder="Your Email" required')
content = content.replace('id="subject" placeholder="Subject"', 'id="subject" name="Subject" placeholder="Subject" required')
content = content.replace('id="message" style="height: 100px"', 'id="message" name="Message" style="height: 100px" required')

# Also add hidden captcha configuration (just to make it look cleaner, formsubmit provides its own recaptcha)
# content = content.replace('</form>', '<input type="hidden" name="_captcha" value="false">\n</form>')

with open('d:/Projects/avadhootha law and associates/contact.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(content)
