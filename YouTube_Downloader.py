"""
MIT License

Copyright (c) 2023 IceMaster24

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""



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
