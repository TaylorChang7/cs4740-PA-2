from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import subprocess
import os
app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd())
#container = os.path.join(app.instance_path,'uploads')
#os.makedirs(container,exists_ok = True)
#print(os.path.join(os.getcwd()))
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd())

@app.route('/upload')
def upload():
	#p = subprocess.call("./autograder.py", shell = True)
	return render_template('upload.html')
@app.route('/')
def main_page():
	return render_template('home.html')

@app.route('/uploader',methods = ['GET','POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		# Testing
		#print(os.path.join("/home/ubuntu/",secure_filename(f.filename)))
		#f.save(os.path.join("/home/ubuntu/",secure_filename(f.filename)))
		print(os.path.join(os.getcwd()))
		f.save(os.path.join(os.getcwd(),secure_filename(f.filename)))

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
		return render_template('uploader.html', info = content, correct = num_correct, title = f.filename)
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



