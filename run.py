#!usr/bin/python2.7
# coding=utf-8

# Title : Facebook Get Cookies Simple #
# Author : Risky Prsty #
# Github : https://github.com/riskyprsty #
# FB : Risky Prsty ~ Alwxsky Cherenkov #
# Python : Versi 2.0 #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #

import requests,bs4,sys,os,json,pickle
import requests,sys
import itertools,threading,time,sys
from multiprocessing.pool import ThreadPool

def kukis():
	p=requests.Session()
	p.get("https://mbasic.facebook.com/login")
	p.headers.update({"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; Lenovo-A6020l36 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36"})
	a=p.post("https://mbasic.facebook.com/login", data={"email":raw_input("\033[1;92m[*] Email: "),"pass":raw_input("\033[1;92m[*] Password: ")}).url
        sd=p.cookies.get_dict()
	if "c_user" in p.cookies.get_dict():
                print "\n \033[1;91m[*] Result Cookies\n\n"
                ab=p.cookies['datr']
                cd=p.cookies['sb']
                ef=p.cookies['c_user']
                gh=p.cookies['xs']
                ij=p.cookies['fr']
                xd = "datr="
                sr = "sb="
                jr = "c_user="
                id = "xs="
                ex = "fr="
                peler = "; "
                hasil = xd + ab + peler + sr + cd + peler + jr + ef + peler + id + gh + peler + ex + ij + peler
                print(hasil)
                print "\n \033[1;93m[*] Copy Cookies diatas"
                sys.exit()
        if "checkpoint" in a:
                print "\n \033[1;91m[!] Akun terkena checkpoint atau sandi salah"

def keluar():
       sys.exit()

def browser():
     print "\033[1;93m{∆} Login terlebih dahulu di browser agar cookie valid dan tidak checkpoint (jangan dilogout sebelum mendapatkan cookies)"
     time.sleep(1)
     print "\033[1;93m{~} Lalu kembali lagi dan login ulang disini"
     time.sleep(1)
     for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rMenunggu Login browser ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSilahkan Login disini     ')
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(10)

logo=('''\n\n
  \033[1;94m••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\033[0m
  \033[1;94m>>>     \033[1;92mGET COOKIES FB SIMPLE\033[0m     \033[1;93m<<<
  \033[1;94m••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••\n\033[0m''')


while True:
        os.system("clear")
        print(logo)
	print "\033[1;93m[1] GET Cookies"
	print "\033[1;93m[2] Keluar\n"
	r=raw_input("\033[1;93m Pilih: ")
	if r=="":
		os.system("clear")
	elif r =="1":
                browser()
                os.system("termux-open https://mbasic.facebook.com")
		kukis()
                
	elif r=="2":
		keluar()
	else:
		print "\033[1;93m Pilihan yang lu masukin salah ler"
