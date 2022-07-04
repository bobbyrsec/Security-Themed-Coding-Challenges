'''
Recover deleted items

Most software will keep deleted items for ~30 days for recovery. Find out where these are stored.
Write a script to pull these items from local databases.
'''

import os

def recover_deleted_files():
	#recover each deleted file by moving it into the /tmp/recovered folder
	os.system("mkdir /tmp/recovered; mv /$HOME/.local/share/Trash/files/* /tmp/recovered; ls -la /tmp/recovered")
	print ("files recovered")

recover_deleted_files()
