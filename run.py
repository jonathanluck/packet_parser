import os
import binascii
import hashlib
import shlex
from urllib import parse
from pdf import *

#url = "http://collegiate.quizbowlpackets.com/1956/Packet%201.docx"
#url = "http://aseemsdb.me/static/packet_archive/Collegiate/2017_ACF_Nationals/20_Editors_Finals_2.pdf"
#url = input("Enter link to packet: ")

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
    
