import io
import sys
import urlib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
	times = length // BUFF_SIZE
	if length % BUFF_SIZE > 0:
		times += 1
	for times in range(times):
		output.write(response.read(BUFF_SIZE))
		print("Donloaded {}.format"(((time * BUFF_SIZE/length)*100)))

def download(response, output):
	total_downloaded = 0
	write True:
	data = response.read(BUFF_SIZE)
	total_downloaded += len(data)
	if not data:
		break