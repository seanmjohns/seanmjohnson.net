#!/usr/local/bin/python3

from yattag import Doc, indent
import sys, os

if(len(sys.argv) < 1 or sys.argv[1] == "-help"):
	print("pagegen.py file type\n")
	print("If the type is 'project', supply the name of the directory that it is located in as the file\n")
	print("Otherwise, just give the name of the file to be generated\n") 
	exit()

file=""
type=""

email="seanmjohns1@gmail.com"
github="pigcoder3"
phone=""

if(len(sys.argv) >= 2):
	file = sys.argv[1]
	if(sys.argv[1] == 'pagegen.py'):
		print("STOP! You are attempting to regenerate the page generation script!")
		exit()
	if(sys.argv[1][len(sys.argv[1])-4:len(sys.argv[1])] != 'html' and sys.argv[2] != "project"):
		print("STOP! You are attempting to regenerate a page that is not an html page!")
		exit()
if(len(sys.argv) >= 3):
	type = sys.argv[2]

#the start function
def createdoc():
	doc.asis('<!DOCTYPE html>');
	with tag('html'):
		with tag('head'):
			with tag('title'):
				if(type == "project"):
					text(parseBasicInfo(file, 'name') + ' - Sean Johnson')
			with tag('meta', name='viewport', content='width=device-width', charset='UTF-8'): pass
			if(type != "project"):
				with tag('script', type='text/javascript', src='stickynav.js'): pass
				with tag('link', rel='stylesheet', href='navbar.css'): pass
			else:
				with tag('script', type='text/javascript', src='../stickynav.js'): pass
				with tag('link', rel='stylesheet', href='../navbar.css'): pass
				with tag('link', rel='stylesheet', href='../project.css'): pass
			if(file == "index.html"):
				with tag('link', rel='stylesheet', href='index.css'): pass
			if(file == "contact.html"):
				with tag('link', rel='stylesheet', href='contact.css'): pass
			
		with tag('body'):
			doc.asis(nameheader())
			doc.asis(navbar())
			with tag('div', id='primary'):
				if(file == "index.html"):
					with tag('div', klass='content_container', id='intro'):
						with tag('a', href='https://github.com/pigcoder3'):
							with tag('img', id='profile', src='github-profile.png', alt='github profile'): pass
						with tag('span', id='desc'):
							text('I program for fun when I\'m not overloaded with work from my high school classes. I am moderately fluent in Java, C, Python, and Bash.');
					doc.asis(createprojectcontainers())
				if(file == "contact.html"):
					with tag('h2', id='contact-header'):
						text("Contact")
					with tag('div', klass='content-container', id='github'):
						with tag('a', href='https://github.com/pigcoder3'):
							with tag('img', src='github-logo.png', id='github-logo'): pass
						with tag('span', klass='notes'):
							text('You can contact me through GitHub (')
							with tag('strong'):
								text(github)
							text('), although I do not check it very often.')
					with tag('div', klass='content-container', id='email'):
						with tag('img', src='email.png', id='email-logo'): pass
						with tag('span', klass='notes'):
							text('Email me at ')
							with tag('strong'):
								text(email)
							text('. I check my email often, so it is likely you will be able to get a hold of me.')
					with tag('div', klass='content-container', id='phone'):
						with tag('img', src='phone.png', id='phone-logo'): pass
						with tag('span', klass='notes'):
							text('I do not yet have a phone number, but I likely will soon.')
				if(type == "project"):
					with tag('h2', id='project-name'):
						text(parseBasicInfo(file, "name"))
					with tag('div', klass='content-container', id='intro'):
						with tag('a', href=parseBasicInfo(file, "github")):
							with tag('img', id='project-img', src=file+'.png'): pass
						with tag('span', id='project-desc'):
							text(parseBasicInfo(file, "longdesc"))
					with tag('div', id='technical-info'):
						with tag('div', klass='content-container', id='download'):
							with tag('span', klass='subheader', id='download-header'):
								text("Download")
							with tag('div', klass='container-body'):
								with tag('div', id='source'):
									with tag('span', id='source-header'):
										text('Source')
									with tag('a', href=parseBasicInfo(file, "github")):
										text('Github')
								with tag('div', id='precompiled'):
									with tag('span', id='precompiled-header'):
										text('Compiled')
									if(parseBasicInfo(file, "compiled")):
										with tag('a', href='https://pigcoder3.github.io/'+file+'/'+parseBasicInfo(file, "compiled")):
											text(parseBasicInfo(file, "compiled"))
									else:
										with tag('a'):
											text("-")
						with tag('div', klass='content-container', id='requirements'):
							with tag('span', klass='subheader', id='requirements-header'):
								text("Requirements")
							with tag('div', klass='container-body'):
								with tag('ul'):
									doc.asis(parseBasicInfo(file, "requirements"))
					with tag('h2', id="gallery-header"):
						text("Gallery")
					with tag('div', klass='content-container', id='gallery'):
						with tag('button', id='left-button', klass='gallery-button', onclick="goLeft()"):
							text(' < ')
						with tag('div', id='image-container'):
							with tag('div', id='image-number-container'):
								with tag('span', id='image-number'):
									text("0 / 0")
							if(os.path.isdir(file+"/gallery")):
								for name in os.listdir(file+"/gallery"):
									if(os.path.isfile(file+"/gallery/"+name)):
										with tag('img', klass='gallery-image', src="https://pigcoder3.github.io/"+file+'/gallery/'+name): pass
							with tag('span', id='no-images'):
								text("It looks like we have no images for this project")
						with tag('button', id='right-button', klass='gallery-button', onclick='goRight()'):
							text(' > ')
						with tag('script', type='text/javascript', src='../gallery.js'): pass
#create the name header
def nameheader():
	doc, tag, text = Doc().tagtext();
	with tag('div'):
		with tag('h1', id='name'):	
			text('Sean Johnson')
	return indent(doc.getvalue())

#basic navbar in all pages
def navbar():
	doc, tag, text = Doc().tagtext();
	with tag('div', id='navbar'):
		with tag('div', id='projects-dropdown', klass='nav'):
			with tag('button', id='projects-dropdown-button', klass='nav-button', onclick='toggle()'):
				text("Projects");
			with tag('div', klass='projects-dd-content', id='dropdown-content'):
				for name in os.listdir("."):
					if(os.path.isdir(name) and name != '.git'):
						with tag('a', klass='project-link', href="https://pigcoder3.github.io/"+name+'/'+name+'.html'):
							text(parseBasicInfo(name, "name"))
		with tag('div', klass='nav'):
			with tag('a', klass='nav-button', href='https://pigcoder3.github.io/'):
				text('Home')
		with tag('div', klass='nav'):
			with tag('a', klass='nav-button', href='https://pigcoder3.github.io/contact.html'):
				text('Contact')
	with tag('div', id='spacer'): pass
	with tag('script'):
		text("""function toggle() {
			var e = document.getElementById("dropdown-content");
			e.classList.toggle("projects-dd-content-shown");
		}

		window.onclick = function(event) {
  			if (!event.target.matches("projects-dropdown-button")) {
				document.getElementsByClassName("projects-dropdown-button")[0].classList.toggle("projects-dd-content-shown");
    		}
  		}""")
	return doc.getvalue();

#create home page project sneak-peeks
def createprojectcontainers():
	doc, tag, text = Doc().tagtext();	
	with tag('h2', id='projects_header'):
		text('Projects');
	with tag('div', id='projects'):
		for name in os.listdir("."):
			if(os.path.isdir(name) and name != '.git'):
				with tag('div', klass='content_container project_container'):
					with tag('a', href=name+'/'+name+'.html'):
						with tag('div', klass='project-desc-container'):
							with tag('span', klass='project_name'):
								text(parseBasicInfo(name, "name"))
							with tag('span', klass='project_desc'):
								text(parseBasicInfo(name, 'simpledesc'))
						with tag('img', src=name+'/'+name+'.png'): pass

	return doc.getvalue();
#gets info from project info files
def parseBasicInfo(filename, key):
	doc, tag, text = Doc().tagtext()
	output = "";
	input = "";
	with open(filename+"/"+filename+".txt", "r") as f:
		while(1):
			input = f.readline();
			if(not input): 
				print("cannot find key '" + tag + "' in file: '" + f + "'")
				exit()
			position = input.find(':')
			if(position > -1):
				if(input[:position] == key):
					if(key == 'requirements'):
						numberOfRequirements = 0
						while(1):
							input = f.readline().strip();
							if(not input): 
								print("Unclosed requirements key in '" + filename + "'")
								exit()
							if(input == ':requirements'): 
								break
							else:
								with tag('li'):
									text(input.strip())
									numberOfRequirements+=1
						if(numberOfRequirements == 0):
							with tag('li'):
								text("None")
						print(doc.getvalue())
						return(indent(doc.getvalue()))
					return input[position+1:].strip()
							

doc, tag, text = Doc().tagtext()

createdoc();
print(indent(doc.getvalue()))
if(type == "project"):	
	with open(file+'/'+file+'.html', 'w') as f:
		f.write(indent(doc.getvalue()))
else:
	with open(file, 'w') as f:
		f.write(indent(doc.getvalue()))