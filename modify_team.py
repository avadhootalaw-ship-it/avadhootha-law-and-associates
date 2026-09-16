import glob
import re

files = glob.glob('d:/Projects/avadhootha law and associates/*.html')
files = [f for f in files if 'admin.html' not in f]

suresh_block = """                <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.5s">
                    <div class="team-item position-relative">
                        <div class="position-relative">
                            <img class="img-fluid" src="img/team-4.jpg" alt="">
                            <div class="team-social text-center">
                                <a class="btn btn-square" href=""><i class="fab fa-facebook-f"></i></a>
                                <a class="btn btn-square" href=""><span style="font-family: Arial, sans-serif; font-weight: bold; font-style: normal; font-size: 1.2em;">𝕏</span></a>
                                <a class="btn btn-square" href=""><i class="fab fa-instagram"></i></a>
                            </div>
                        </div>
                        <div class="bg-light text-center p-4">
                            <h4 class="mt-2 team-name" style="word-wrap: break-word; font-size: 1.1rem; line-height: 1.4;">Adv. Suresh R L</h4>
                            <span class="text-primary">Team Member</span>
                        </div>
                    </div>
                </div>
"""

for file in files:
    with open(file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        content = f.read()
    
    if '<!-- Team Start -->' in content:
        if 'team-4.jpg' not in content:
            content = re.sub(r'col-lg-4 col-md-6 wow fadeInUp', r'col-lg-3 col-md-6 wow fadeInUp', content)
            content = content.replace('data-wow-delay="0.5s">\n                    <div class="team-item position-relative">\n                        <div class="position-relative">\n                            <img class="img-fluid" src="img/team-2.jpg"', 'data-wow-delay="0.7s">\n                    <div class="team-item position-relative">\n                        <div class="position-relative">\n                            <img class="img-fluid" src="img/team-2.jpg"')
            content = content.replace('<div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">\n                    <div class="team-item position-relative">\n                        <div class="position-relative">\n                            <img class="img-fluid" src="img/team-2.jpg"', suresh_block + '<div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">\n                    <div class="team-item position-relative">\n                        <div class="position-relative">\n                            <img class="img-fluid" src="img/team-2.jpg"')
            with open(file, 'w', encoding='utf-8', errors='surrogateescape') as f:
                f.write(content)
