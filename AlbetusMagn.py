import random
import colorama
import time

def logos(metin, gecikme):
    for karakter in metin:
        print(karakter, end='', flush=True)
        time.sleep(gecikme)
    print()  # Yeni satır eklemek için

metin = "                         SMS Bomber maked by : @Albertus"
gecikme = 0.1   
	
print("""\033[93m
     _   _ _             _           __  __                
   /_\ | | |__  ___ _ _| |_ _  _ __|  \/  |__ _ __ _ _ _  
  / _ \| | '_ \/ -_) '_|  _| || (_-< |\/| / _` / _` | ' \ 
 /_/ \_\_|_.__/\___|_|  \__|\_,_/__/_|  |_\__,_\__, |_||_|
                                               |___/      
\033[0m""")


def sms_site():
	link = random.randint(1,15)
	if link == 1:
		print(f"[+] başarılı >>> {no} www.dominos.tr")
	if link == 2:
		print(f"[-] başarısız >>> {no} www.kimgbister.com.tr")
	if link == 3:
		print(f"[+] başarılı >>> {no} www.trendyol.com.tr")
	if link == 4:
		print(f"[+] başarılı >>> {no} www.a101.com.tr")
	if link == 5:
		print(f"[-] başarısız >>> {no} www.bim.com.tr")
	if link == 6:
		print(f"[+] başarılı >>> {no} www.amazon.com.tr")
	if link == 7:
		print(f"[-] başarısız >>> {no} www.prime.com.tr")
	if link == 8:
		print(f"[+] başarılı >>> {no} www.netflix.com.tr")
	if link == 9:
		print(f"[-] başarısız >>> {no} www.alibaba.com.tr")
	if link == 10:
		print(f"[+] başarılı >>> {no} www.turkcell.com.tr")
	if link == 11:
		print(f"[-] başarısız >>> {no} www.whatsapp.com.tr")

while True:
    logos(metin, gecikme)
    print("\033[92m                           Hedef nunarayı giriniz\033[0m")
    no = int(input("\033[91m                              +90 \033[0m"))
    if len(str(no)) == 10:
    	while True:
    		sms_site()
    		time.sleep(0.1)
		
    if len(str(no)) >10 or len(str(no)) <10:
    	print("Adamakıllı numara gir...")
 
	
	
	