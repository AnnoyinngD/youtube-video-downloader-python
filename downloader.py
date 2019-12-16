

from pytube import YouTube
SAVE_PATH = "folder locayion" :
links = open('Songs.txt','r')
for l in links:
	get_true = True
	while get_true:
		try:
			yt = YouTube(l)
			get_true = False
		except:
			print("Connection Error")
			continue
	mp4files = yt.filter('mp4')
	try:
		print(yt.filename)
		print(mp4files[-1])
	except:
		pass
	
	video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		video.download(SAVE_PATH)
	except:
		print("Error, Maybe Duplicate File")
		continue
