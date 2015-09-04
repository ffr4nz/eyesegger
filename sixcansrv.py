#!/usr/bin/env python
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "ffranz"
__copyright__ = "2015"
__credits__ = ["ffranz"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "ffranz"
__email__ = "ffranz@sinfonier-project.net"
__status__ = "Developing"

import socket
from socket import *
import optparse
import datetime
import time
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hide_service():
	abort(404)

@app.route('/about')
def about():
	return 'tuoba'

@app.route('/ip/<path:host>/<path:port>/<path:proto>')
def scan_ip(host,port,proto):
        insert_data ={}
        try:
                #socket initialization
		if proto == 'udp':
                	sckt = socket(AF_INET6, SOCK_DGRAM)
		elif proto == 'tcp':
                	sckt = socket(AF_INET6, SOCK_STREAM)
		received = ''
		sckt.settimeout(1.5)
                sckt.connect((host, int(port)))
                if port == 80:
                    sckt.send('GET / HTTP/1.0\r\n\r\n'.encode('utf-8'))
		    results = sckt.recv(1024)
		elif port == 21:
		    results = sckt.recv(1024)
		elif port == 161:
		    results = sckt.recv(1024)
                else:
                    sckt.send('Hello\r\n'.encode('utf-8'))
		    results = sckt.recv(1024)
                print('---- Port %d open ----'% int(port))
                print(host, results.decode('utf-8'))

                insert_data['dest_ip'] = host
                insert_data['port'] = port
                #insert_data['response'] = results.replace('\r\n','<br />').replace('\n\r','<br />').replace('\r','<br />').replace('\n','<br />')
                insert_data['response'] = results
                insert_data['str_date'] = datetime.datetime.now().strftime("%d-%m-%y_%H:%M")
                insert_data['epoch_date'] = int(datetime.datetime.now().strftime("%s")) * 1000
		insert_data['status'] = "success"
        except timeout as terr:
		print('Timeout! ',terr)
		insert_data['error_code'] = 0	
                insert_data['error_desc'] = str(terr)
                insert_data['status'] = "error" 
	except Exception as err:
                print('Error! ',err)
		insert_data['error_code'] = err[0]
		insert_data['error_desc'] = err[1]
		insert_data['status'] = "error"
        finally:
                sckt.close()
	return jsonify(insert_data)

def main():
    parser = optparse.OptionParser(usage="%prog [options]  or type %prog -h (--help)")
    parser.add_option('-p','--port',
		dest='port',
		action='store',
		help='The port to run server on',
		default=4343)
    (options, args) = parser.parse_args()
    port = int(options.port)
    key="ip"
    print 'Tornado on port {port}...'.format(port=port)

    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(app))

    http_server.listen(int(port))
    IOLoop.instance().start()

if __name__ == '__main__':
	main()
