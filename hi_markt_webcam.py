import os 
import time 
from colorama import Fore, Back, Style 
import random


s_download_url = 'http://rathaus-hildesheim.de/webcam/webcam.jpg'
s_prefix = 'hildesheim_marktplatz_'
s_suffix = '.jpg'
i_pause_in_seconds = 60
i_delay = 0

print(Back.RED + Fore.BLACK + '---{ STARTING DOWNLOAD }---' + Style.RESET_ALL + "\n\n")

while(True):
    # generate time stamp YYYY-MM-DD_hhmmss
    s_timestamp = time.strftime("%Y-%m-%d_%H%M%S")
    # assemble filename 
    s_filename = f"{s_prefix}{s_timestamp}{s_suffix}"
    # assemble wget command 
    s_wget_command = f"wget -O {s_filename} --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0' {s_download_url}"

    # delay execution by random amount to hopefully prevent overBoting the server and getting to much 404s
    i_delay = random.randint(1,8)
    time.sleep(i_delay)
    
    # print progress
    print(Fore.RED + f"Download file: {s_filename}")
    print(f"From: {s_download_url}" + Style.RESET_ALL)

    # execute wget command 
    os.system(s_wget_command)
    time.sleep(i_pause_in_seconds-i_delay)
    print("\n")

print(Back.RED + Fore.BLACK + '---{ DOWNLOAD COMPLETE }---' + Style.RESET_ALL)

