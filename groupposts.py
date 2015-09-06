## THIS IS THE MAIN FILE OF THE PROJECT ###
'''

Script : Facebook Feed Grabber 
Author : Khaled Farah
Date : 6th of September 2015
Purpose : grab the posts from a specific facebook group without logging , using the facebook graph API

'''

import requests , sys
indexfile = open("index.html" , "w") # The HTML file
secret = "Your secret access token" # Access token
group_id = "Your Group id"
posts = requests.get("https://graph.facebook.com/"+group_id+"/feed/?access_token="+secret).json() # POST is A json file Now 
data = posts['data'] 

for i in data : 
     try :
     	indexfile.write("POST : "+str(i[u"message"].encode("UTF-8"))) # We are using encoding to UTF-8 to display arabic text
     	indexfile.write("<br> BY :"+str(i[u"from"]["name"].encode("UTF-8")))
	indexfile.write("<br> link : <a href='"+str(i["link"])+"' target='_blank'> here </a> ") #opening the post in a seperate page.
     except : 
	pass 
     try : 
	indexfile.write ("<br> <img src='"+str(i[u"picture"])+"'>")
     except :  # The Post has no pic included 
             a.write("no pic")
     indexfile.write("<br><br><br>")

indexfile.close()
for i in range(int(sys.argv[1])) :  # The Number of pages in the group 
	indexfile = open("index.html" , "a")
	posts = requests.get(posts['paging']['next'])
	data = posts['data']
	for i in data : 
     		try :
     			indexfile.write("POST : "+str(i[u"message"].encode("UTF-8")))
     			indexfile.write("<br> BY :"+str(i[u"from"]["name"].encode("UTF-8")))
			indexfile.write("<br> link : <a href='"+str(i["link"])+"' target='_blank'> here </a> ")
     		except : 
			pass 
     		try : 
			indexfile.write ("<br> <img src='"+str(i[u"picture"])+"'>")
     		except : 
             		indexfile.write("no pic")
     		indexfile.write("<br><br><br>")# Making space between posts 
indexfile.close()
