#!/usr/bin/env python3
import os
import sys

cmdpath = sys.argv[1]
bash_cmd = ["cd " + cmdpath, "git status"]

result_os = os.popen(' && '.join(bash_cmd)).read()

for result in result_os.split('\n'):
	#print(result)
	#print('---')
	if result.find('modified') != -1:
		prepare_result = result.replace('\tmodified:    ', '')
		print(prepare_result)
for i in range(len(result_os.split('\n'))):
	if result_os.split('\n')[i] == 'Untracked files:':
		print("\tThe new file: ",result_os.split('\n')[i+2])
