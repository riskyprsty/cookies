import requests,bs4,sys,os
import requests,sys
from multiprocessing.pool import ThreadPool

def kukis():
	r=requests.Session()
	r.get("https://mbasic.facebook.com/login")
	r.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"})
	r.post("https://mbasic.facebook.com/login", data={"email":raw_input("?: Email: "),"pass":raw_input("?: Password: ")}).url
	if "c_user" in r.cookies.get_dict():
		print(r.cookies.get_dict())
                print "\nCopy Cookies diatas"

def keluar():
       sys.exit()

while True:
	print "[1] GET Cookies"
	print "[2] Keluar\n"
	r=raw_input("?: Choose: ")
	if r=="":
		os.system("clear")
	elif r =="1":
		kukis()
	elif r=="2":
		keluar()
	else:
		print "!Wrong Input ter"
