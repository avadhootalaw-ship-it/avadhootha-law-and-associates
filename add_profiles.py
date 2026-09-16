import glob
import re

profile_madhu = """    <!-- Profile Start -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="row g-5">
                <div class="col-lg-4 wow fadeIn" data-wow-delay="0.1s">
                    <img class="img-fluid w-100" src="img/team-1.jpg" alt="Adv. Madhu Channaiah Vishwakarma">
                </div>
                <div class="col-lg-8 wow fadeIn" data-wow-delay="0.5s">
                    <h1 class="display-5 mb-2">Adv. Madhu Channaiah Vishwakarma</h1>
                    <h4 class="text-primary mb-4">Advocate & Solicitor | Founder, Avadhoota Law Associates</h4>
                    
                    <h3 class="mb-3">Professional Profile</h3>
                    <p>Adv. Madhu Channaiah Vishwakarma is an Advocate with approximately <strong>7 years of experience in the legal field</strong>, bringing together practical experience in litigation, legal research, documentation, administration and institutional affairs.</p>
                    <p>With an academic foundation in <strong>Mechanical Engineering followed by Law</strong>, his professional journey reflects a multidisciplinary approach to problem-solving. His legal experience encompasses <strong>civil and criminal matters, service and administrative matters, labour and employment disputes, Labour Court matters, arbitration, cheque dishonour proceedings, contractual disputes and document verification.</strong></p>
                    <p>Beyond conventional legal practice, he has developed substantial exposure to <strong>institutional administration, NGO and Trust administration, corporate empanelments, governance, compliance and organisational processes.</strong> This combination enables him to look at legal issues not merely as isolated disputes, but in the context of the practical, administrative and organisational circumstances in which they arise.</p>
                    <p class="mb-5">His approach is grounded in <strong>careful legal analysis, strong documentation, practical strategy and an understanding of the client's larger objectives.</strong></p>

                    <h3 class="mb-3">Areas of Legal Practice & Expertise</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Civil Litigation & Civil Disputes</li>
                        <li>Criminal Matters</li>
                        <li>Service & Administrative Law</li>
                        <li>Regulatory & Statutory Compliance</li>
                        <li>Legal Risk Assessment</li>
                        <li>Corporate Legal Support</li>
                        <li>NGO & Trust-related Legal Matters</li>
                        <li>Corporate Empanelments</li>
                        <li>Administrative & Governance Matters</li>
                    </ul>

                    <h3 class="mb-3">Litigation & Legal Practice</h3>
                    <p>Adv. Madhu Channaiah has gained practical experience across multiple areas of litigation and legal practice, including <strong>civil original suits, criminal defence matters, service and administrative law, cheque dishonour cases, arbitration and contractual disputes.</strong></p>
                    <p>His service-law exposure includes matters concerning <strong>promotion and regularisation, retirement and pensionary benefits and other service-related claims.</strong></p>
                    <p>His responsibilities have included preparation and drafting of <strong>petitions, affidavits, written statements and rejoinders</strong>, legal research, case strategy, document verification, contractual compliance review and representation before courts and tribunals.</p>
                    <p class="mb-5">This hands-on exposure has helped develop an approach to legal practice that places importance on <strong>preparation, precision in documentation and understanding the factual foundation of every matter.</strong></p>

                    <h3 class="mb-3">Training & Exposure Under Senior Legal Professionals</h3>
                    <p>An important part of Madhu's early legal development came through practical exposure to experienced members of the legal profession.</p>
                    <p>He had the opportunity to work as an intern under <strong>A.S. Ponnanna, Senior Counsel, AKS Legal</strong>, gaining exposure to professional legal practice and the working environment of senior counsel. He also received practical exposure through the <strong>District Legal Services Authority (DLSA)</strong>, providing insight into legal service delivery and access to justice.</p>
                    <p class="mb-5">These experiences, together with his subsequent independent legal practice, have contributed to the development of a practice-oriented understanding of litigation, legal research, drafting and client representation.</p>

                    <h3 class="mb-3">Administration, Governance & Institutional Experience</h3>
                    <p>Madhu's professional experience extends beyond courtroom practice.</p>
                    <p>He has been associated with <strong>college administration, NGO and Trust administration, corporate empanelments and institutional processes</strong>, giving him an understanding of the administrative and compliance requirements that operate alongside legal obligations.</p>
                    <p>His experience includes exposure to:</p>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Institutional administration</li>
                        <li>NGO & Trust administration</li>
                        <li>Corporate empanelments</li>
                        <li>Documentation and record management</li>
                        <li>Regulatory and statutory compliance</li>
                        <li>Governance and policy interpretation</li>
                        <li>Administrative processes</li>
                        <li>Employee and service-related issues</li>
                        <li>Contractual documentation</li>
                        <li>Organisational coordination</li>
                    </ul>
                    <p class="mb-5">This background is particularly relevant when legal advice must be understood alongside the <strong>operational realities of an institution or organisation.</strong></p>

                    <h3 class="mb-3">A Multidisciplinary Legal Perspective</h3>
                    <p>Madhu's combination of <strong>Engineering and Law</strong> brings a distinctive analytical dimension to his professional practice.</p>
                    <p>Engineering has developed his orientation towards structured thinking, systems and problem-solving, while legal education and practical experience have provided the framework to analyse rights, obligations, procedures and legal risk.</p>
                </div>
            </div>
        </div>
    </div>
    <!-- Profile End -->"""

with open('d:/Projects/avadhootha law and associates/profile-madhu.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    content = f.read()

# Replace header text
content = re.sub(r'<h1 class="display-1 text-white animated slideInDown">.*?</h1>', '<h1 class="display-1 text-white animated slideInDown">Profile</h1>', content)
content = re.sub(r'<li class="breadcrumb-item text-primary active" aria-current="page">.*?</li>', '<li class="breadcrumb-item text-primary active" aria-current="page">Profile</li>', content)

# Replace everything from <!-- About Start --> to <!-- Footer Start --> with the Profile Block
content = re.sub(r'(?s)<!-- About Start -->.*?<!-- Footer Start -->', profile_madhu + '\n    <!-- Footer Start -->', content)

with open('d:/Projects/avadhootha law and associates/profile-madhu.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(content)

# Now inject the "View Profile" buttons globally
files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        html = f.read()
    
    # We need to find: <span class="text-primary">Founder</span></div>
    # And replace with: <span class="text-primary">Founder</span><br><a href="profile-madhu.html" class="btn btn-sm btn-primary mt-3">View Profile</a></div>
    if 'View Profile' not in html:
        # Madhu
        html = html.replace('<span class="text-primary">Founder</span>\n                        </div>', '<span class="text-primary d-block mb-3">Founder</span>\n                            <a href="profile-madhu.html" class="btn btn-sm btn-primary px-4">View Profile</a>\n                        </div>')
        # Sampangiramaiah (create a placeholder page link for them)
        html = html.replace('Adv. Sampangiramaiah</h4>\n                            <span class="text-primary">Team Member</span>\n                        </div>', 'Adv. Sampangiramaiah</h4>\n                            <span class="text-primary d-block mb-3">Team Member</span>\n                            <a href="profile-sampangiramaiah.html" class="btn btn-sm btn-primary px-4">View Profile</a>\n                        </div>')
        # Suresh
        html = html.replace('Adv. Suresh R L</h4>\n                            <span class="text-primary">Team Member</span>\n                        </div>', 'Adv. Suresh R L</h4>\n                            <span class="text-primary d-block mb-3">Team Member</span>\n                            <a href="profile-suresh.html" class="btn btn-sm btn-primary px-4">View Profile</a>\n                        </div>')
        # Chethan
        html = html.replace('Adv. Chethan B.A.</h4>\n                            <span class="text-primary">Team Member</span>\n                        </div>', 'Adv. Chethan B.A.</h4>\n                            <span class="text-primary d-block mb-3">Team Member</span>\n                            <a href="profile-chethan.html" class="btn btn-sm btn-primary px-4">View Profile</a>\n                        </div>')
        
        with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
            f.write(html)
