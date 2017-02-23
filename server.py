#!/usr/bin/env python2

# Arsh Chauhan
# 2/22/2017
# Last edited: 2/22/2017
# Server to return a random cat name from a list of names.
# 	file names.txt generated from names from http://petrix.com/catnames/

import SimpleHTTPServer
import BaseHTTPServer
import random
import os
import argparse

def generate_name(name_file):
	with open (name_file,'r') as cat_names:
		names = [name.strip() for name in cat_names]
		return random.choice(names)

class cat_name_generator(BaseHTTPServer.BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path =='/':
			page = open('web/index.html')
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(page.read())
			self.wfile.close()
		if self.path == '/generate_name':
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(generate_name('files/names.txt'))
			self.wfile.close()

if __name__ == '__main__':
	try:
		handler = cat_name_generator
		parser = argparse.ArgumentParser(description='Return a random cat name to your client')
		parser.add_argument('-port',type=int, default=8080,help='Port to run server on')
		args = parser.parse_args()
		serverAddress = ('127.0.0.1',args.port)
		server = BaseHTTPServer.HTTPServer(serverAddress,handler)
		server.serve_forever()
	
	except KeyboardInterrupt:
		exit(1)
