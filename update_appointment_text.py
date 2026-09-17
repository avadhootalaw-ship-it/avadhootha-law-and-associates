import os

files_to_update = [
    'd:/Projects/avadhootha law and associates/index.html',
    'd:/Projects/avadhootha law and associates/appointment.html'
]

target_h1 = '<h1 class="display-5 mb-4">Make An Appointment To Start Your Dream Project</h1>'
replacement_h1 = '<h1 class="display-5 mb-4">Make An Appointment</h1>'

target_p = '<p class="mb-4">Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit. Aliqu diam amet diam et eos. Clita erat ipsum et lorem et sit, sed stet lorem sit clita duo justo magna dolore erat amet</p>'
replacement_p = '<p class="mb-4">To Make an Appointment please fill the details and book an appointment.</p>'


for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check what to do
    # Option 1: Replace both H1 and P as decided (H1 shorter, P has the text)
    # Option 2: Replace H1 with the full text, and remove P. 
    # Let's do Option 2 because it exactly matches "instead of X - Y"
    
    content = content.replace(target_h1, '<h1 class="display-5 mb-4">To Make an Appointment please fill the details and book an appointment.</h1>')
    content = content.replace(target_p, '')
    
    # Wait, if they just meant "change the H1 and remove the paragraph", this does it.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")
