from flask import Flask, request, Response
import os
import binascii
import hashlib
import shlex
from urllib import parse
from pdf import *


def handle_packet(url):

    unescaped = parse.unquote(url)
    dirname = binascii.hexlify(hashlib.md5(bytes(url,"utf-8")).digest()).decode("utf-8")[:8]
    filename = unescaped[unescaped.rfind("/")+1:]
    if(not os.path.isdir(dirname)):
        os.mkdir(dirname)
    os.chdir(dirname)
    if(not os.path.isfile(filename)):
        os.system("wget {}".format(shlex.quote(url)))

    if(".doc" in url[-5:]):
        os.system("libreoffice --headless --convert-to pdf {}".format(shlex.quote(filename)))
        filename = filename[:filename.rfind(".")] + ".pdf"


    htmlname = filename[:-4] + "s.html"
    os.system("pdftohtml {}".format(shlex.quote(filename)))
    process_pdf(htmlname)
    os.chdir("..")
    return "{}/0.html".format(dirname)

app = Flask(__name__)

@app.route("/")
def hello():
    r = Response(handle_packet(request.args["link"]))
    r.headers['Access-Control-Allow-Origin'] = '*'
    print(r)
    return r

app.run("0.0.0.0", 80)



        
