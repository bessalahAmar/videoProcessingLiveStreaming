
from google_images_download import google_images_download

def editName(s):
	s = s.replace("é","e")
	s = s.replace("è","e")
	s = s.replace("É","E")
	s = s.replace("ç","c")
	s = s.replace("ï","i")
	
	return s;
	


response = google_images_download.googleimagesdownload()
f = open("listPresentateur.txt", encoding="utf-8")
for name in f:
	name = editName(name);
	print(name);
	arguments = {"keywords":""+name+"","limit":20,"print_urls":True}
	paths = response.download(arguments)

f.close()



