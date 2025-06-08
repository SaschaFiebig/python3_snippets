import os
import time 
from colorama import Fore, Back, Style


DEBUG = False
s_prefix = 'the_pope_and_his_child_01-'
s_suffix = '.jpg'
i_pause_seconds = 0.01

# open txt file with links 
o_file_handler = open('the_old_man_and_the_see.txt', 'r')

# add links to array 
a_urls = []
for s_url in o_file_handler:
    a_urls.append(s_url)

if(DEBUG):
    for url in a_urls:
        print(url.strip())
        print('')


print(Back.RED + Fore.BLACK + "---{ STARTING DOWNLOAD }---\n\n" + Style.RESET_ALL)
i_pages = len(a_urls)
for i_counter in range(i_pages):
    
    i_page = i_counter+1
    if(i_page > 12):
        i_page = i_page + 100
    
    s_download_url = a_urls[i_counter].strip()

    # generate filename 
    if(i_page < 10):
        s_filename = f"{s_prefix}00{i_page}{s_suffix}"
    elif(i_page < 100):
        s_filename = f"{s_prefix}0{i_page}{s_suffix}"
    else:
        s_filename = f"{s_prefix}{i_page}{s_suffix}"

    if(DEBUG):
        print(s_filename)
        print('')

    # generate wget command 
    # wget -U "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0" -nd -r --level=1  -e robots=off -A jpg,jpeg -H http://pixabay.com/
    s_wget_command = f"wget -O {s_filename} --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0' {s_download_url}"

    if(DEBUG):
        print(s_wget_command)
        print("")

    print(Fore.RED + f"Download file {s_filename} ({i_page} of {i_pages})")
    print(f"{s_download_url}" + Style.RESET_ALL)

    # execute wget command
    os.system(s_wget_command)
    print("\n")
    time.sleep(i_pause_seconds)

o_file_handler.close()


print(Back.RED + Fore.BLACK + '---{ DOWNLOAD COMPLETE }---' + Style.RESET_ALL)
