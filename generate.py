# This file generates HTML for featured articles
# 
# Based on: http://www.nytimes.com/2016/03/20/magazine/the-fugitive.html?_r=0

open("index.html", 'w').close()
title = raw_input("Title: ")
subtitle = raw_input("Subtitle: ")
author = raw_input("Author: ")
date = raw_input("Month Day, Year : ")
date = date.upper()
author = author.upper()

headImageUrl = raw_input("Image Url: ")
headImageSentence = raw_input("Image Sentence: ")
headImageCredit = raw_input("Image Credit(Jon Tonks for The New York Times): ")
logoColor = raw_input("Logo color: ")

paragraphs = []
with open("article.txt", "r") as article:
	content = article.read()
	content = content.splitlines()
	for x in range(0, len(content)):
		if (content[x] != ''):
			paragraphs.append(content[x])

with open("index.html", "a") as myfile:
	#HEADER
	myfile.write("<!DOCTYPE html>\n<html>\n\t<head>\n");
	myfile.write("\t\t<title>" + title + " | McGill Tribune</title>\n");
	myfile.write("\t\t<meta property=\"og:title\" content=\"" + title + " | McGill Tribune\"/>\n");

	#META TAGS
	myfile.write("\t\t<meta property=\"og:image\" content=\"" + headImageUrl + "\">\n");
	myfile.write("\t\t<meta property=\"og:description\" content=\"" + subtitle  + "\"/>\n");
	myfile.write("\t\t<meta name=\"author\" content=\"The McGill Tribune\">\n");
	myfile.write("\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");

	#LINKS
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=Gentium+Book+Basic|Open+Sans:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link rel=\"stylesheet\"	href=\"index.css\">\n");
	myfile.write("\t\t<link href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>\n");
	myfile.write("\t\t<link rel=\"icon\" type=\"image/png\" href=\"http://mcgilltribune.com/wp-content/uploads/2015/09/favicon.ico\">\n");

	#GOOGLE ANALYTICS
	myfile.write("\t\t<script>\n\t\t\t(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n\t\t\t(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n\t\t\tm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n\t\t\t})(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n\t\t\tga('create', 'UA-34387711-1', 'auto');\n\t\t\tga('send', 'pageview');\n\t\t</script>\n");

	#OPEN BODY
	myfile.write("\t</head>\n\t<body>\n");
	
	#PAGE TOP
	#TODO Need a src for black and white. 
	if((logoColor == 'Black')or(logoColor == 'black')):
		myfile.write("\t\t<img class='tribune-logo' src='black_logo.png'/>\n");
	else :
		myfile.write("\t\t<img class='tribuneLogo' src='white_logo.png'/>\n");
	myfile.write("\t\t<div class='image'>\n");
	myfile.write("\t\t\t<img class='header-image' src='" + headImageUrl + "'/>\n\t\t</div>\n");

	#STORY META
	myfile.write("\t\t<div class='story-meta'>\n")
	myfile.write("\t\t\t<h1 class='title'>" + title + "</h1>\n");
	myfile.write("\t\t\t<h3 class='subtitle'>" + subtitle + "</h3>\n");
	myfile.write("\t\t\t<h5 class='byline'>By " + author +"   " + date + "</h5>\n\t\t</div>\n");
	
	#IMAGE CREDIT
	myfile.write("\t\t<p class='header-image-sentance'>\n\t\t\t" + headImageSentence)
	myfile.write("\n\t\t\t<i class='header-image-credit'>" + headImageCredit + "</i>\n")
	myfile.write("\t\t</p>\n")

	#CONTENT
	myfile.write("\t\t<div class='content-wrapper'>\n");
	for i in range(0, len(paragraphs)):
		myfile.write("\t\t\t<p class='content-paragraph'>\n")
		myfile.write("\t\t\t\t" + paragraphs[i] + "\n")
		myfile.write("\t\t\t</p>\n")
	myfile.write("\t\t<div>\n")
	
#CLOSE BODY
	myfile.write("\t</body>\n</html>")