# This file generates HTML for featured articles
# 
# Based on: http://www.nytimes.com/2016/03/20/magazine/the-fugitive.html?_r=0
open("endpoints.txt", 'w').close()
title = raw_input("Title: ")
subtitle = raw_input("Subtitle: ")
headImageUrl = raw_input("Image Url: ")


with open("endpoints.txt", "a") as myfile:
	
	#HEADER
	myfile.write("<!DOCTYPE html>\n<html>\n\t<head>\n");
	myfile.write("\t\t<title>" + title + " | McGill Tribune</title>\n");
	myfile.write("\t\t<meta property=\"og:title\" content=\"" + title + " | McGill Tribune\"/>\n");

	#META TAGS
	myfile.write("\t\t<meta property=\"og:image\" content=\"" + headImageUrl + "\">\"\n");
	myfile.write("\t\t<meta property=\"og:description\" content=\"" + subtitle  + "\"/>\"\n");
	myfile.write("\t\t<meta name=\"author\" content=\"The McGill Tribune\">\n");
	myfile.write("\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");

	#LINKS
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=Gentium+Book+Basic|Open+Sans:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,700' rel='stylesheet' type='text/css'>\n");
	myfile.write("\t\t<link rel=\"stylesheet\"	href=\"index.css\">\n");
	myfile.write("\t\t<link rel=\"icon\" type=\"image/png\" href=\"http://mcgilltribune.com/wp-content/uploads/2015/09/favicon.ico\">\n");
	

	#GOOGLE ANALYTICS
	myfile.write("\t\t<script>\n\t\t\t(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n\t\t\t(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n\t\t\tm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n\t\t\t})(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n\t\t\tga('create', 'UA-34387711-1', 'auto');\n\t\t\tga('send', 'pageview');\n\t\t</script>\n");

	myfile.write("\t</head>\n\t<body>\n");
	myfile.write("\t</body>\n</html>");


