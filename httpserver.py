from wsgiref.handlers import format_date_time
import socket
import os
import mimetypes
import datetime
import time
import threading

server_port = 47590
homedir = os.getcwd()
resources = {}


def processData(data):
    
    response = ""
    #pre-process string
    data = data.splitlines()
    #resource accessed
    filename = data[0].split(" ")[1] #get the requested resource fromt he first line
    filename = filename[1:] #trim off leading '\' ex: \bar.html

    if(not os.path.isfile(filename)):
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
        return response.encode(), filename
    #increment access count
    
    resources[filename] += 1

    filesize = os.path.getsize(filename)
    
    with open(filename, "rb") as fp: #here
        file_contents = fp.read()
    #line 1
    response += "HTTP/1.1 200 OK\r\n"
    #line 2: current time
    timestamp = format_date_time(time.mktime(datetime.datetime.now().timetuple())) #formats a timestamp of this moment into a string
    response += "Date: " + timestamp +"\r\n"
    #line 3: Server
    response += "Server: mgomez4/11.18\r\n"
    #line 4: last modified
    lm_time = datetime.datetime.fromtimestamp(os.path.getmtime(filename)).timetuple()
    response +="Last-Modified: " + format_date_time(time.mktime(lm_time)) + "\r\n"
    #line 5
    response += "Accept-Ranges: bytes\r\n"
    #line 6: file size
    response += "Content-Length: " + str(filesize) + "\r\n"
    #line 7: mime types
    file_mime_type = mimetypes.MimeTypes().guess_type(filename)[0]
    if file_mime_type is None:
        response += "Content-Type: "+ "application/octet-stream" +"\r\n\r\n"
    else:
        response += "Content-Type: "+ str(file_mime_type)+"\r\n\r\n"
    #end of header
    #contents of file
    response = response.encode() + file_contents 

    return bytes(response), filename

def request_handler(client_connection, address, port):
    if(os.getcwd() == homedir):
        os.chdir("www")
    
    #print ("Got connection from", address) @debug
    data = client_connection.recv(1024)
    request_response, resource = processData(data.decode())

    client_connection.send(request_response)
    client_connection.close()
    if resource in resources.keys():
        print(resource,"|",address,"|",port,"|",resources[resource])

    
    

def main():
    if(not os.path.isdir("www")):
        print("Error: Directory 'www' does not exist")
        exit()
    
    ## 
    #Set up counter for resource accesses
    os.chdir("www")
    global resources
    resources = {rsc: 0 for rsc in os.listdir()}

    os.chdir(homedir)
    ##
    s = socket.socket()
    s.bind(('',server_port))
    s.listen(5)
    host, port = s.getsockname() 
    print("Server Initialized\nHost: ", host, " Port: ", port)

    while(True):
        try: 

            c, address = s.accept()
            #new thread TBD
            t = threading.Thread(target= request_handler, args=(c, address[0], address[1],))
            t.start()
            t.join()

        except KeyboardInterrupt:
            break
    print("Ending server...")
main()
