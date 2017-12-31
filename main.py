import requests

def get_dir_filename_pages(url):
	message = ''
	message += "---Directory and Filename Scan---" + "\n"
	with open('wordlist/Directories_test.wordlist','r') as dirfile:
		for lines in dirfile:
			lines = lines.rstrip("\n")
			scan_url = url + lines
			r = requests.get(scan_url)
			if r.status_code == 200:
				message += scan_url + "\n"
	return message

def get_php_pages(url):
	message = ''
	message += "---PHP Filename Scan---" + "\n"
	with open('wordlist/Directories_test.wordlist','r') as filenames:
		for lines in filenames:
			lines = lines.rstrip("\n")
			scan_url = url + lines
			r = requests.get(scan_url)
			if r.status_code == 200:
				message += scan_url + "\n"
	return message	

# base_url have to include 'http://' . Example: http://www.example.com , http://192.168.0.1 

base_url = ""
dir_filename_output = get_dir_filename_pages(base_url)
php_output = get_php_pages(base_url)

with open("output_file.txt", 'w') as write_file:
	write_file.write(dir_filename_output)
	write_file.write("\n")
	write_file.write(php_output)

print("Done. Output in output_file.txt")








