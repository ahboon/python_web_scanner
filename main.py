import requests
import threading

def urlread(url, param_list):
    message = ""
    for param_item in param_list:
        scan_url = url + "/"+ param_item
        r = requests.get(scan_url)
        if r.status_code == 200:
            print(scan_url)
            

word_list = []
word_cell = []
counter = 0
word_counter = 0
threads = []

# base_url have to include 'http://' . Example: http://www.example.com , http://192.168.0.1 
base_url = ""

with open('wordlist/Filenames_or_Directories_All.wordlist','r') as dirfile:
    for lines in dirfile:
        lines = lines.rstrip('\n')
        word_counter += 1
        if counter > 15000:
            word_list.append(word_cell)
            counter = 0
            word_cell = []
        else:
            word_cell.append(lines)
            counter += 1
if len(word_cell) > 0:
    word_list.append(word_cell)

print(str(len(word_list)) + " threads are running against:" + str(word_counter) + " possible words.")

for i in range(len(word_list)):
    t = threading.Thread(target=urlread,args=(base_url,word_list[i]))
    threads.append(t)
    t.start()

