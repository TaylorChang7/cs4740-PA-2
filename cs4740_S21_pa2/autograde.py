#!/usr/bin/env python
import os
import subprocess

num_correct = subprocess.call("./execute_submission_and_assess_output.sh", shell=True)
print ("Score: " + str(num_correct) + " out of 2 correct.")
print("*************Original submission*************")
with open('subtract.py','r') as fs:
	print(fs.read())


