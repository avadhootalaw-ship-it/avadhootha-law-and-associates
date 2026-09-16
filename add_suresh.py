import re

suresh_content = """    <!-- Profile Start -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="row g-5">
                <div class="col-lg-4 wow fadeIn" data-wow-delay="0.1s">
                    <img class="img-fluid w-100" src="img/team-4.jpg" alt="Adv. Suresh R. L.">
                </div>
                <div class="col-lg-8 wow fadeIn" data-wow-delay="0.5s">
                    <h1 class="display-5 mb-2">Adv. Suresh R. L.</h1>
                    <h4 class="text-primary mb-4">HR & Administration Consultant | Legal & Labour Relations Support</h4>
                    
                    <h3 class="mb-3">Professional Profile</h3>
                    <p>Suresh R. L. is an experienced Human Resources and Administration professional with over 20 years of versatile experience spanning HR management, administration, client relations, public relations and corporate communication. His professional background includes experience across consultancy, corporate and public-sector environments, with a strong focus on stakeholder coordination, employee relations and organizational administration.</p>
                    <p>He currently serves as an HR Consultant with Spectrum HR Consultancy, Bengaluru, where his responsibilities include payroll and salary management, statutory compliance, recruitment and talent acquisition, employee engagement, welfare initiatives, grievance handling and addressing labour-related issues.</p>
                    <p class="mb-5">His academic background combines Human Resource Management and Law, enabling him to bring an interdisciplinary perspective to matters involving workplace administration, employee relations, labour compliance and organizational practices.</p>

                    <h3 class="mb-3">Areas of Professional Expertise</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Human Resource Management</li>
                        <li>Labour & Employee Relations</li>
                        <li>HR Administration</li>
                        <li>Labour-law Compliance Support</li>
                        <li>Payroll & Salary Administration</li>
                        <li>Recruitment & Talent Acquisition</li>
                        <li>Employee Grievance Management</li>
                        <li>Employee Welfare & Engagement</li>
                        <li>Statutory Compliance - PF, ESI and related requirements</li>
                        <li>Corporate Communication & Stakeholder Relations</li>
                        <li>Public Relations & Administration</li>
                    </ul>

                    <h3 class="mb-3">Professional Experience</h3>
                    <h5 class="mb-1">HR Consultant &ndash; Spectrum HR Consultancy, Bengaluru</h5>
                    <p class="text-primary fw-bold mb-3">June 2023 &ndash; Present</p>
                    <p class="mb-5">Key areas of responsibility include payroll and salary management, statutory compliance, recruitment and onboarding, attendance and leave administration, employee engagement and welfare, grievance handling, and addressing labour-related issues.</p>

                    <h3 class="mb-3">Previous Professional Experience</h3>
                    <p>Suresh has also worked with:</p>
                    <ul class="mb-3" style="list-style-type: disc; padding-left: 20px;">
                        <li>Shiva Shree Media Pvt. Ltd.</li>
                        <li>GR Infrastructure Pvt. Ltd.</li>
                        <li>Women and Child Development Department, Government of Karnataka</li>
                    </ul>
                    <p class="mb-5">His career has provided exposure to HR, administration, corporate communication, public relations and stakeholder coordination.</p>

                    <h3 class="mb-3">Legal & Academic Qualifications</h3>
                    
                    <h5 class="mb-0">Bachelor of Laws (LL.B.)</h5>
                    <p class="mb-0">Karnataka State Law University, Hubballi</p>
                    <p class="text-muted" style="font-style: italic;">Final results awaited as per the submitted CV.</p>
                    <br>
                    
                    <h5 class="mb-0">Master of Social Work (MSW)</h5>
                    <p class="mb-0">Specialisation: Human Resource Management</p>
                    <p>University of Mysore, Mysuru.</p>
                    <br>
                    
                    <h5 class="mb-0">Bachelor of Arts (B.A.)</h5>
                    <p class="mb-0">Journalism & Mass Communication</p>
                    <p class="mb-5">Maharaja's College, University of Mysore.</p>

                    <h3 class="mb-3">Professional Strengths</h3>
                    <p class="mb-5">His key professional strengths include project management, leadership, teamwork, public relations, effective communication, critical thinking and time management.</p>

                    <h3 class="mb-3">Languages</h3>
                    <p class="mb-0">English &ndash; Fluent</p>
                    <p class="mb-0">Hindi &ndash; Fluent</p>
                    <p class="mb-5">Kannada &ndash; Native.</p>

                    <h3 class="mb-3">Role at Avadhoota Law Associates</h3>
                    <p>Suresh's combination of extensive HR experience and legal education provides a valuable perspective in matters involving <strong>employment practices, labour relations, HR administration, statutory compliance and workplace-related issues.</strong></p>
                    <p class="mb-5">His experience in dealing with employees, organizations and stakeholders complements Avadhoota Law Associates' broader approach to practical, organization-focused legal and professional support.</p>

                    <h3 class="mb-2">Avadhoota Law Associates</h3>
                    <p class="text-primary" style="font-style: italic; font-size: 1.1rem;">Where Justice Meets Dharma</p>
                </div>
            </div>
        </div>
    </div>
    <!-- Profile End -->"""

with open('d:/Projects/avadhootha law and associates/profile-suresh.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    html = f.read()

# Replace the title tag just in case
html = re.sub(r'<title>.*?</title>', '<title>Adv. Suresh R. L. - Profile</title>', html)

# Replace everything from <!-- Profile Start --> to <!-- Profile End --> with the Suresh block
html = re.sub(r'(?s)<!-- Profile Start -->.*?<!-- Profile End -->', suresh_content, html)

with open('d:/Projects/avadhootha law and associates/profile-suresh.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(html)
