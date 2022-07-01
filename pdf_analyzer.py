'''

/BaseFont /Helvetica
/Encoding /WinAnsiEncoding
endobj
10 0 obj
/Creator (Rave \(http://www.nevrona.com/rave\))
/Producer (Nevrona Designs)
/CreationDate (D:20060301072826)

'''
import subprocess 
import re

def get_pdf_info():
	out = subprocess.check_output(["strings", "/home/parallels/Documents/sample.pdf"])
	out = str(out)
	out = out.replace("\\n", "")
	out = out.replace("\\", "")
	font = re.findall("(?:/BaseFont /)(.*)(?:/Encoding)", str(out))
	print (font[0], "font")
	encoding = re.findall("(?:/Encoding)(.*)(?:endobj.*Creator)", str(out))
	print (encoding[0], "encoding")
	creator = re.findall("(?:/Creator)(.*)(?:/Producer.*)", str(out))
	print (creator[0], "creator")
	producer = re.findall("(?:/Producer)(.*)(?:/CreationDate.*)", str(out))
	print (producer[0], "producer")
	date = re.findall("\d{14}", str(out))
	print (date[0], "date")

get_pdf_info()