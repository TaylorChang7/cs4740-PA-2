from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import subprocess
import os
app = Flask(__name__)

@app.route('/upload')
def uploader():
	#p = subprocess.call("./autograder.py", shell = True)
	return render_template('upload.html')

@app.route('/uploader',methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join("/home/ubuntu/",secure_filename(f.filename)))
		print(f.filename)
		file_str = f.filename
		"""
		1. call the shell script from here 
		2. 
		"""
		#num_correct = subprocess.call("./execute_submission_and_assess_output.sh",shell= True) # Somehow pass the file to this 
		command_line = "./execute_submission_and_assess_output.sh {}".format(f.filename)
		num_correct = subprocess.call(command_line,shell = True)
		with open(f.filename,'r') as fs:
			content = fs.read()
		context = {
			'content': content,
			'num_correct': num_correct,
			'title': f.filename,
		}
		return render_template('result.html', info = content, correct = num_correct, title = f.filename)
		#return ("Score:" + str(num_correct)+ "out of 2 correct.")
		#return "Successfully"
		"""
		f is a file that user submits
		we can run the autograder.py on this script
		if it is valid, then  print the "success" message
		otherwise, print "invalid script"
		"""
		#return 'file uploaded successfully'
#subprocess.run('ls',shell = True,)
if __name__ == '__main__':
	app.run(debug = True,host = "0.0.0.0")



