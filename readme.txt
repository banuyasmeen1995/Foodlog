
Pre-requisites
-----------------------
---------------------
1.Create an account with AWS
2.Install Putty
---------------------------
	
Step 1. Creating an Instance in AWS
--------------------------------------
a. In AWS Management console Create a S3 bucket 
	i.Click on create and upload the zip file shared into it
	ii.Make sure that the S3 bucket and the zip file are public
	iii.The object URL of this Zip file is used to migrate the Zipfile into EC2 instance from S3 Bucket
b. Create an EC2 instance of type Amazon linux2 (t2 micro)
	i. create a security group and add HTTP type
	ii.Create a security key of SSH type (pem file will autodownload) and launch it
c. Connect SSH into ec2 instance through SSH using Putty
	i.Open your PuttyGen(it is included with your Putty Client installation) on your PC
	ii. Make sure the checkbox “RSA” is selected.
	iii.Click load and go to the folder where you have stored your pem file, select it and choose open
	iv. After the Key is loaded, click on save private key.
	v.Now type a name for your key.
	vi.Now close PuttyGen program and open Putty. Go to SSH section and double-click it
	Vii.Go to Auth section and select the ppk file that we just created.
	viii.Go back at the top in the Session section. Fill the field Hostname (or IP address) with the IP address given to your AWS instance and click open.
	ix. A window will prompt asking for the username, type your distro username.

---------------------------
	
Step 2. Running the file in AWS
--------------------------------------
	i. sudo su - this will change the directory to root
	ii. yum update -y - this will update the EC2 instance
	iii. yum install httpd -y  - this will install apache
	iv. cd/var/www/html - this is to acess EC2 instance
	v. wget <<object URL>> - copy the zip file in the S3 bucket to EC2 Instance
	vi. unzip <<filename.zip>> - to unzip the file into Ec2 instance
	vii. mv <<foldername>>/* . - to move all the files into EC2 Instance from thr folder within the zipfile
	viii. service httpd start - this will start the server
	xi.  pip install Flask
	x. python ***.py- run the file
	
