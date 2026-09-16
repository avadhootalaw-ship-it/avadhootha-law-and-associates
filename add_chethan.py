import re

chethan_content = """    <!-- Profile Start -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="row g-5">
                <div class="col-lg-4 wow fadeIn" data-wow-delay="0.1s">
                    <img class="img-fluid w-100" src="img/team-2.jpg" alt="Adv. Chethan B. A.">
                </div>
                <div class="col-lg-8 wow fadeIn" data-wow-delay="0.5s">
                    <h1 class="display-5 mb-2">Adv. Chethan B. A.</h1>
                    <h4 class="text-primary mb-4">Advocate | Legal Associate</h4>
                    
                    <h3 class="mb-3">Professional Profile</h3>
                    <p>Chethan B. A. is a law graduate with a strong foundation in legal research, drafting, case-law analysis and legal documentation. A graduate of The Oxford College of Law, HSR Layout, affiliated with Karnataka State Law University, Hubballi, he completed his B.A. LL.B. in 2025.</p>
                    <p>His practical legal exposure includes internships with law firms in Bengaluru, where he assisted in legal research, preparation of legal documents, petitions, notices, agreements, affidavits and case briefs. He has gained exposure to civil, criminal and corporate matters, as well as court proceedings and client-related documentation.</p>
                    <p class="mb-5">With an analytical approach and strong interest in legal research and drafting, Chethan contributes to the firm's legal work with attention to detail, professional discipline and a commitment to ethical legal practice.</p>

                    <h3 class="mb-3">Areas of Legal Exposure</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Civil Law</li>
                        <li>Criminal Law</li>
                        <li>Corporate & Commercial Matters</li>
                        <li>Legal Research</li>
                        <li>Legal Drafting</li>
                        <li>Case Law Analysis</li>
                        <li>Legal Documentation</li>
                        <li>Litigation Support</li>
                        <li>Arbitration & Mediation &ndash; Academic/Workshop Exposure</li>
                    </ul>

                    <h3 class="mb-3">Professional Experience</h3>
                    
                    <h5 class="mb-1">Legal Intern &ndash; Express Legal India, Malleswaram, Bengaluru</h5>
                    <p class="text-primary fw-bold mb-3">July 2025 &ndash; October 2025</p>
                    <p>During his internship, Chethan:</p>
                    <ul class="mb-4" style="list-style-type: disc; padding-left: 20px;">
                        <li>Assisted in drafting legal documents, petitions and case summaries.</li>
                        <li>Conducted legal research relating to civil, criminal and corporate matters.</li>
                        <li>Observed court proceedings and prepared case briefs.</li>
                        <li>Assisted senior advocates during client meetings and documentation.</li>
                    </ul>

                    <h5 class="mb-1">Legal Intern &ndash; Kanchi Varadaraya Law Associates, Bengaluru</h5>
                    <p class="text-primary fw-bold mb-3">June 2024 &ndash; November 2024</p>
                    <p>His responsibilities included:</p>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Researching statutory provisions and case laws for ongoing matters.</li>
                        <li>Assisting in drafting notices, agreements and affidavits under supervision.</li>
                    </ul>

                    <h3 class="mb-3">Moot Court & Legal Development</h3>
                    <p>Chethan participated in a <strong>National Moot Court Competition in 2024</strong>, where he prepared memorials and presented oral arguments involving Competition Law and Criminal Law.</p>
                    <p class="mb-5">He has also attended workshops covering <strong>legal drafting, arbitration and mediation</strong>, contributing to his practical understanding of legal processes and dispute resolution.</p>

                    <h3 class="mb-3">Education</h3>
                    <h5 class="mb-0">B.A. LL.B.</h5>
                    <p class="mb-0">The Oxford College of Law, HSR Layout</p>
                    <p class="mb-0">Karnataka State Law University, Hubballi</p>
                    <p class="fw-bold mb-5">2025</p>

                    <h3 class="mb-3">Core Skills</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Legal Research & Drafting</li>
                        <li>Case Law Analysis</li>
                        <li>Legal Databases &ndash; Manupatra & SCC Online</li>
                        <li>MS Office</li>
                        <li>Analytical Skills</li>
                        <li>Professional Communication</li>
                    </ul>

                    <h3 class="mb-3">Languages</h3>
                    <p class="mb-0">Kannada and English &ndash; Fluent in reading and writing</p>
                    <p class="mb-5">Hindi and Telugu &ndash; Known.</p>

                    <h3 class="mb-3">Role at Avadhoota Law Associates</h3>
                    <p>Chethan brings a research-oriented and detail-focused approach to legal work, with particular interest in understanding legal principles, analysing case law and developing clear and effective legal documentation.</p>
                    <p class="mb-5">As part of Avadhoota Law Associates, he supports the firm's commitment to providing diligent, ethical and well-researched legal assistance.</p>

                    <h3 class="mb-2">Avadhoota Law Associates</h3>
                    <p class="text-primary" style="font-style: italic; font-size: 1.1rem;">Where Justice Meets Dharma</p>
                </div>
            </div>
        </div>
    </div>
    <!-- Profile End -->"""

with open('d:/Projects/avadhootha law and associates/profile-chethan.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    html = f.read()

html = re.sub(r'<title>.*?</title>', '<title>Adv. Chethan B. A. - Profile</title>', html)
html = re.sub(r'(?s)<!-- Profile Start -->.*?<!-- Profile End -->', chethan_content, html)

with open('d:/Projects/avadhootha law and associates/profile-chethan.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write(html)
