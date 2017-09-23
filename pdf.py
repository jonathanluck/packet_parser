def process_pdf(htmlname):
        import re
        import codecs
        import shlex
        import os

        metatag = "<meta charset='UTF-8'>"
        styletag = "<style>body{font-size:28}</style>"
        js = "<script>document.onkeydown = function(e) {{switch (e.keyCode) {{ case 37: window.location.href='{}.html'; break; case 39: window.location.href='{}.html';break;}}}};</script>"
        nextbutton = "<button onclick=\"window.location.href='{}.html'\" style='position: fixed;bottom: 10;right: 10;height: 10%;width: 40%;'>Next Question</button>"
        prevbutton = "<button onclick=\"window.location.href='{}.html'\" style='position: fixed;bottom: 10;left: 10;height: 10%;width: 40%;'>Previous Question</button>"

        def process_question(q, i):
                q = re.sub(r"\s", " ", q.replace("<br/>","").replace("<hr/>", ""), flags=re.UNICODE)
                q = re.sub("ANSWER:", "<br/>ANSWER:", q, flags=re.I)
                q = q.replace("[10]", "<br/>[10]")
                if(q.rfind("<") > q.rfind(">")):
                #we have a bad tag somewhere
                        q = q[:q.rfind("<")]
                q = metatag + js.format(i-1, i+1)+ styletag+ q + nextbutton.format(i+1) + prevbutton.format(i-1)
                return q
        
        f = codecs.open(htmlname, mode = "r", encoding="utf-8")
        questions = re.split(r"(<\/a>|<br\/>)[\r\n]*(<b>)*[\r\n]*[0-9]{1,2}\.[\r\n]*\s*", f.read().replace("&#160;", " ").strip("\r\n\t"), flags=re.UNICODE)
        questions = [""] + [q for q in questions if(q and len(q) > 100)]
        for i in range(len(questions) - 1):
            with codecs.open("{}.html".format(i), mode="w", encoding="utf-8") as out:
                out.write(process_question("<hr>".join((questions[i], questions[i+1])) ,i))
                
        f.close()
        print(len(questions))

