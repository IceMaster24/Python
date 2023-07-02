import sys
from pytube import YouTube
import os


audio = str(input("Download audio only? type y/n : "))
file_link = str(input("Enter YouTube link : "))
file_path = str(input("path : "))   #the path to work might have to be with the double backslash (\\)



class Downloader:
	def __init__(self, link, path, audio_only):
		self.link = link 
		self.path = path
		self.audio = audio_only


	def download_file(self):
		yt= YouTube(self.link)
		try:
   			if (self.audio == "n"):
   				stream= yt.streams.filter(file_extension="mp4").get_highest_resolution()
   				stream.download(output_path= self.path)
   				
   			elif (self.audio == "y"):
   				stream= yt.streams.get_by_itag(140)		#<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">]
   				mp4_file= stream.download(output_path= self.path)

   				name, ext = os.path.splitext(mp4_file)
   				mp3_file= name + ".mp3"
   				os.rename(mp4_file, mp3_file)

   			print("\nDownload completed of :", str(yt.title))

		except:
   			print("\nAn error occurred during the process")
   			


istance = Downloader(file_link, file_path, audio)
istance.download_file()
