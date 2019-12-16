# from __future__ import unicode_literals
# import youtube_dl
# import os
# from sys import argv

# # Download data and config

# download_options = {
# 	'format': 'bestaudio/best',
# 	'outtmpl': '%(title)s.%(ext)s',
# 	'nocheckcertificate': True,
# 	'postprocessors': [{
# 		'key': 'FFmpegExtractAudio',
# 		'preferredcodec': 'mp3',
# 		'preferredquality': '192',
# 	}],
# }

# # Song Directory
# if not os.path.exists('Songs'):
# 	os.mkdir('Songs')
# else:
# 	os.chdir('Songs')

# # Download Songs
# with youtube_dl.YoutubeDL(download_options) as dl:
# 	with open('../' + argv[1], 'r') as f:
# 		for song_url in f:
# 			dl.download([song_url])

from pytube import YouTube
SAVE_PATH = "C:\Users\mini\Downloads\github2bu\Songs\" :
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