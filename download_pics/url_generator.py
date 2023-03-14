
DEBUG = True
s_title = 'the_old_man_and_the_see.txt'
s_url_prefix = 'https://things_and_stuff-'
s_url_sufix = '.bacon'
i_from = 1
i_to = 20 +1
i_offset = 42  # offset can also be negative


# generate url 
def generate_urls(i_from, i_to, i_offset, s_url_prefix, s_url_sufix):
    
    a_urls = []
    i_start = i_from + i_offset
    i_end = i_to + i_offset 

    for i_url_counter in range(i_start, i_end):
        if(i_url_counter < 10):
            s_url_string = f"{s_url_prefix}00{i_url_counter}{s_url_sufix}"
        elif(i_url_counter < 100): 
            s_url_string = f"{s_url_prefix}0{i_url_counter}{s_url_sufix}"
        else: 
            s_url_string = f"{s_url_prefix}{i_url_counter}{s_url_sufix}"

        a_urls.append(s_url_string)

    return a_urls


# molticore processing experiment 
a_finished_urls = generate_urls(i_from, i_to, i_offset, s_url_prefix, s_url_sufix)

# test print generated urls 
if(DEBUG):
    for url in a_finished_urls:
        print(url)

# open file for writing 
o_file_handler = open(s_title, 'x')

# write generated urls to file 
for s_url in a_finished_urls:
    o_file_handler.write(f"{s_url}\n")

o_file_handler.close()
