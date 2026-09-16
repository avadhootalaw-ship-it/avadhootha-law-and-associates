import re

sampangi_content = """    <!-- Profile Start -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="row g-5">
                <div class="col-lg-4 wow fadeIn" data-wow-delay="0.1s">
                    <img class="img-fluid w-100" src="img/team-3.jpg" alt="Adv. Sampangi Ramaiah">
                </div>
                <div class="col-lg-8 wow fadeIn" data-wow-delay="0.5s">
                    <h1 class="display-5 mb-2">Adv. Sampangi Ramaiah</h1>
                    <h4 class="text-primary mb-4">Advocate & Tax Consultant | Civil, Criminal, Labour, Service & Income Tax Matters</h4>
                    
                    <h3 class="mb-3">Professional Profile</h3>
                    <p>Sampangi Ramaiah is an Advocate with a substantial professional background spanning Central Government administration, accounts, internal audit, legal and labour-related matters. He served in Central Government organizations from <strong>1982 to 2018</strong>, retiring as <strong>Assistant Director (Administration & Accounts)</strong>.</p>
                    <p>During his government service, he worked across various areas including administration, accounts, audit, bills and law. He also spent approximately <strong>16 years in the Internal Audit Division</strong>, involving extensive professional travel and exposure to Central Government establishments across India.</p>
                    <p>Following his retirement, he continued to contribute his professional experience as a Consultant and Legal Adviser, including with the <strong>Indian Science Congress Association under the Ministry of Science and Technology, Government of India</strong>, where he was involved in legal, administration and accounts-related responsibilities.</p>
                    <p>He subsequently entered legal practice and was enrolled as an Advocate with the <strong>Bar Council of Bangalore in 2022</strong>. He currently practices independently, handling matters relating to <strong>service, civil, criminal, labour, family and income-tax law</strong>.</p>
                    <p class="mb-5">His extensive experience in government administration, audit, accounts and legal matters enables him to approach legal issues with a practical understanding of organizational procedures, regulatory requirements and administrative processes.</p>

                    <h3 class="mb-3">Areas of Legal Practice</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Service Matters</li>
                        <li>Civil Matters</li>
                        <li>Criminal Matters</li>
                        <li>Labour & Employment Matters</li>
                        <li>Family Matters</li>
                        <li>Income Tax Matters</li>
                        <li>Legal & Administrative Matters</li>
                        <li>Drafting, Pleadings & Court Proceedings</li>
                    </ul>

                    <h3 class="mb-3">Professional Experience</h3>
                    
                    <h5 class="mb-1">Advocate &ndash; Independent Legal Practice</h5>
                    <p class="text-primary fw-bold mb-3">2022 &ndash; Present</p>
                    <p>Sampangi Ramaiah has been practising independently as an Advocate since his enrolment in 2022. His practice includes service matters concerning employees, civil matters, criminal cases, labour matters, family matters and income-tax matters.</p>
                    <p>His professional responsibilities include drafting pleadings and legal documents, preparation of plaints, replies and rejoinders, filing of matters and appearing before the court.</p>
                    <p class="mb-5">According to his submitted biodata, he has handled approximately <strong>100 cases during his legal practice</strong>, with the biodata recording favourable outcomes in more than 90 of those matters.</p>

                    <h5 class="mb-1">Assistant Director (Administration & Accounts) &ndash; Central Silk Board</h5>
                    <p class="text-primary fw-bold mb-3">Ministry of Textiles, Government of India | 1982 &ndash; 2018</p>
                    <p>Sampangi Ramaiah served in the Central Silk Board, Ministry of Textiles, Government of India, and retired as <strong>Assistant Director (Administration & Accounts)</strong>.</p>
                    <p>During his tenure, he worked in different capacities and areas involving:</p>
                    <ul class="mb-3" style="list-style-type: disc; padding-left: 20px;">
                        <li>Administration</li>
                        <li>Accounts</li>
                        <li>Internal Audit</li>
                        <li>Bills</li>
                        <li>Legal matters</li>
                    </ul>
                    <p class="mb-5">He spent approximately <strong>16 years in the Internal Audit Division</strong>, travelling extensively throughout India in connection with his professional responsibilities.</p>

                    <h3 class="mb-3">Professional Experience on Deputation</h3>
                    <p>He was also deputed to several Government institutions, including:</p>
                    <ul class="mb-3" style="list-style-type: disc; padding-left: 20px;">
                        <li><strong>National Centre for Biological Sciences</strong>, under the Tata Institute</li>
                        <li><strong>National Institute of Unani Medicine</strong></li>
                        <li><strong>All India Council for Technical Education</strong></li>
                    </ul>
                    <p class="mb-5">During these assignments, he was responsible for administration and accounts functions.</p>

                    <h5 class="mb-1">Consultant & Legal Adviser &ndash; Indian Science Congress Association</h5>
                    <p class="text-primary fw-bold mb-3">Ministry of Science & Technology, Government of India</p>
                    <p>Following his retirement, Sampangi Ramaiah worked for approximately three years with the <strong>Indian Science Congress Association</strong> as a Consultant and Legal Adviser, while also overseeing administration and accounts-related responsibilities.</p>
                    <p class="mb-5">He subsequently also worked as a Consultant at the <strong>All India Council for Technical Education, New Delhi</strong>, before joining the Indian Science Congress Association at Kolkata.</p>

                    <h3 class="mb-3">Academic & Professional Qualifications</h3>
                    
                    <h5 class="mb-0">Master of Arts (M.A.)</h5>
                    <p class="mb-4">English Literature</p>
                    
                    <h5 class="mb-0">Bachelor of Laws (LL.B.)</h5>
                    <p class="mb-4">Three-Year Degree Programme</p>
                    
                    <h5 class="mb-0">Post Graduate Diploma</h5>
                    <p class="mb-5">Hospital Administration & Management</p>

                    <h3 class="mb-3">Additional Professional Training</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Income Tax Practice Training</li>
                        <li>Computer Training</li>
                        <li>Senior English Typewriting</li>
                        <li>Shorthand</li>
                    </ul>

                    <h3 class="mb-3">Professional Strengths</h3>
                    <p>His professional strengths include hands-on experience in legal drafting, preparation of plaints, replies and rejoinders, filing of legal matters and court appearances.</p>
                    <p>His long-standing background in Central Government administration, accounts and internal audit also provides him with practical exposure to administrative procedures, financial matters, compliance-related functions and institutional processes.</p>
                    <p class="mb-5">He continues to maintain an interest in the legal profession through regular reading and updating of his knowledge in the field of law.</p>

                    <h3 class="mb-3">Languages</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Kannada</li>
                        <li>English</li>
                        <li>Hindi</li>
                        <li>Telugu</li>
                        <li>Tamil</li>
                    </ul>

                    <h3 class="mb-3">Role at Avadhoota Law Associates</h3>
                    <p>At <strong>Avadhoota Law Associates</strong>, Adv. Sampangi Ramaiah brings together his experience as a practising Advocate with several decades of professional service in Central Government organizations.</p>
                    <p>His background in <strong>administration, accounts, internal audit and legal matters</strong>, together with his present legal practice, provides a practical and multidisciplinary perspective in matters involving <strong>service law, civil disputes, labour matters, family matters, criminal cases and income-tax matters</strong>.</p>
                    <p class="mb-5">His experience in government organizations and subsequent legal practice contributes to Avadhoota Law Associates' commitment to providing practical informed and professionally grounded legal assistance.</p>

                    <h3 class="mb-2">Avadhoota Law Associates</h3>
                    <p class="text-primary" style="font-style: italic; font-size: 1.1rem;">Where Justice Meets Dharma</p>
                </div>
            </div>
        </div>
    </div>
    <!-- Profile End -->"""

with open('d:/Projects/avadhootha law and associates/profile-sampangiramaiah.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    html = f.read()

html = re.sub(r'<title>.*?</title>', '<title>Adv. Sampangi Ramaiah - Profile</title>', html)
html = re.sub(r'(?s)<!-- Profile Start -->.*?<!-- Profile End -->', sampangi_content, html)

with open('d:/Projects/avadhootha law and associates/profile-sampangiramaiah.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(html)
