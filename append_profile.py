import re

new_content = """                    <p class="mb-5">This multidisciplinary perspective is particularly valuable in matters involving <strong>contracts, documentation, institutional processes, compliance and disputes</strong> where legal and practical considerations intersect.</p>

                    <h3 class="mb-3">Legal & Academic Qualifications</h3>
                    <ul class="mb-4" style="list-style-type: none; padding-left: 0;">
                        <li><strong>Bachelor of Laws (LL.B.)</strong></li>
                        <li><strong>The Oxford College of Law</strong></li>
                        <br>
                        <li><strong>Bachelor of Engineering (B.E.) &ndash; Mechanical Engineering</strong></li>
                    </ul>
                    <p class="mb-5">His academic background combines technical education with legal training, supporting a structured and analytical approach to legal practice.</p>

                    <h3 class="mb-3">Professional & Legal Training</h3>
                    <p>His practical legal training and professional exposure include:</p>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Exposure to senior counsel practice</li>
                        <li>District Legal Services Authority experience</li>
                        <li>Civil and criminal litigation</li>
                        <li>Service and administrative matters</li>
                        <li>Tribunal-related practice</li>
                        <li>Legal drafting and research</li>
                        <li>Document verification</li>
                        <li>Contractual documentation</li>
                        <li>Case preparation and legal strategy</li>
                    </ul>

                    <h3 class="mb-3">Professional Strengths</h3>
                    <p>Madhu's professional strengths include:</p>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>Strategic legal reasoning</li>
                        <li>Legal drafting & research</li>
                        <li>Case preparation and analysis</li>
                        <li>Document verification</li>
                        <li>Contract review and vetting</li>
                        <li>Institutional governance</li>
                        <li>Administrative understanding</li>
                        <li>Regulatory compliance</li>
                        <li>Legal risk assessment</li>
                        <li>Labour and service matters</li>
                        <li>Effective communication</li>
                        <li>Leadership and coordination</li>
                    </ul>
                    <p class="mb-5">He approaches professional assignments with an emphasis on <strong>integrity, preparation, clarity of thought and practical resolution of legal issues.</strong></p>

                    <h3 class="mb-3">Languages</h3>
                    <ul class="mb-5" style="list-style-type: disc; padding-left: 20px;">
                        <li>English</li>
                        <li>Kannada</li>
                        <li>Telugu</li>
                        <li>Hindi</li>
                    </ul>

                    <h3 class="mb-3">Professional Role at Avadhoota Law Associates</h3>
                    <p>At <strong>Avadhoota Law Associates</strong>, Adv. Madhu Channaiah is involved in the firm's legal practice, client advisory, litigation strategy and professional development.</p>
                    <p>His experience across <strong>civil and criminal litigation, service matters, labour disputes, administrative law, arbitration, contractual matters and document verification</strong> forms an important part of the firm's practice.</p>
                    <p>His additional exposure to <strong>institutional administration, NGO and Trust affairs, corporate empanelments and compliance-related requirements</strong> enables him to appreciate the legal concerns of both individuals and organizations.</p>
                    <p class="mb-5">The firm seeks to bring together legal professionals with diverse areas of experience, allowing matters to be approached through <strong>collective knowledge, careful legal analysis and practical strategy.</strong></p>

                    <h3 class="mb-3">Our Approach</h3>
                    <p>At Avadhoota Law Associates, legal practice is viewed not simply as the resolution of disputes, but as a process of <strong>understanding, advising, preparing and representing.</strong></p>
                    <p class="mb-5">The objective is to provide clients with legal assistance that is <strong>professionally responsible, practically informed and grounded in the principles of law and justice.</strong></p>

                    <h3 class="mb-2">Avadhoota Law Associates</h3>
                    <p class="text-primary" style="font-style: italic; font-size: 1.1rem;">Where Justice Meets Dharma</p>"""

with open('d:/Projects/avadhootha law and associates/profile-madhu.html', 'r', encoding='utf-8', errors='surrogateescape') as f:
    html = f.read()

# Locate the insertion point
target = "procedures and legal risk.</p>"
if target in html and "This multidisciplinary perspective" not in html:
    html = html.replace(target, target + "\n\n" + new_content)
    with open('d:/Projects/avadhootha law and associates/profile-madhu.html', 'w', encoding='utf-8', errors='surrogateescape') as f:
        f.write(html)
