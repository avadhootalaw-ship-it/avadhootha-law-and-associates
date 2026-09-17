import re
import glob

# 1. Update index.html and appointment.html to remove Choose Time and make Choose Date col-12

appointment_target = """                            <div class="col-12 col-sm-6">
                                <div class="date" id="date" data-target-input="nearest">
                                    <input type="text"
                                        class="form-control datetimepicker-input"
                                        name="Date" placeholder="Choose Date" data-target="#date" data-toggle="datetimepicker" style="height: 55px;">
                                </div>
                            </div>
                            <div class="col-12 col-sm-6">
                                <div class="time" id="time" data-target-input="nearest">
                                    <input type="text"
                                        class="form-control datetimepicker-input"
                                        name="Time" placeholder="Choose Time" data-target="#time" data-toggle="datetimepicker" style="height: 55px;">
                                </div>
                            </div>"""

appointment_replacement = """                            <div class="col-12">
                                <div class="date" id="date" data-target-input="nearest">
                                    <input type="text"
                                        class="form-control datetimepicker-input"
                                        name="Date" placeholder="Choose Date" data-target="#date" data-toggle="datetimepicker" style="height: 55px;">
                                </div>
                            </div>"""

for filepath in ['d:/Projects/avadhootha law and associates/index.html', 'd:/Projects/avadhootha law and associates/appointment.html']:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if appointment_target in content:
        content = content.replace(appointment_target, appointment_replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Target not found in {filepath}")

# 2. Update contact.html to have the same fields.
contact_filepath = 'd:/Projects/avadhootha law and associates/contact.html'
with open(contact_filepath, 'r', encoding='utf-8', errors='ignore') as f:
    contact_content = f.read()

contact_target = """                        <div class="row g-3">
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="name" name="Name" placeholder="Your Name" required>
                                    <label for="name">Your Name</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="email" class="form-control" id="email" name="Email" placeholder="Your Email" required>
                                    <label for="email">Your Email</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="subject" name="Subject" placeholder="Subject" required>
                                    <label for="subject">Subject</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Leave a message here" id="message" name="Message" style="height: 100px" required></textarea>
                                    <label for="message">Message</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <button class="btn btn-primary w-100 py-3" type="submit">Send Message</button>
                            </div>
                        </div>"""

contact_replacement = """                        <div class="row g-3">
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="name" name="Name" placeholder="Your Name" required>
                                    <label for="name">Your Name</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="email" class="form-control" id="email" name="Email" placeholder="Your Email" required>
                                    <label for="email">Your Email</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <input type="text" class="form-control" id="mobile" name="Mobile" placeholder="Your Mobile" required>
                                    <label for="mobile">Your Mobile</label>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-floating">
                                    <select class="form-select" id="service" name="Service" aria-label="Choose Service">
                                        <option selected>Choose Service</option>
                                        <option value="Service 1">Service 1</option>
                                        <option value="Service 2">Service 2</option>
                                        <option value="Service 3">Service 3</option>
                                    </select>
                                    <label for="service">Service</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating date" id="date" data-target-input="nearest">
                                    <input type="text" class="form-control datetimepicker-input" id="choosedate" name="Date" placeholder="Choose Date" data-target="#date" data-toggle="datetimepicker">
                                    <label for="choosedate">Choose Date</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Leave a message here" id="message" name="Message" style="height: 100px" required></textarea>
                                    <label for="message">Message</label>
                                </div>
                            </div>
                            <div class="col-12">
                                <button class="btn btn-primary w-100 py-3" type="submit">Send Message</button>
                            </div>
                        </div>"""

if contact_target in contact_content:
    contact_content = contact_content.replace(contact_target, contact_replacement)
    with open(contact_filepath, 'w', encoding='utf-8') as f:
        f.write(contact_content)
    print("Updated contact.html")
else:
    print("Target not found in contact.html")
