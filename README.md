# cs457-557-spring20-pa1-MGomez99
cs457-557-spring20-pa1-MGomez99 created by GitHub Classroom

# How to Run: 
- "python3 httpserver.py" will start the server. The port is printed to console, and can be changed by modifying
- the "server_port" global variable at the start of the file. 
- Opening a different terminal/remote session allows you to test the functionality via   
"wget http://remote[XX].cs.binghamton.edu:[PORT]/test.html" where test.html can be substituted for any of the files in www
- the www directory MUST BE POPULATED CORRECTLY PRIOR TO STARTING THE SERVER, as the dictionary is initalized once at start time

# Implementation:   

- Used the socket library to set up the server. Standard set up where the program calls bind() and listen(5) [so 5 max req.]
- New accepted connections are handled in a new thread [threading library]
- Formatting of http requests is done via other libraries or manually creating string literals
- Counter of file accesses is stored in a dictionary and printed after each request
- Mimetypes library is used to auto-guess the type [uses /etc/mimetypes], but binary files are manually found
- **Control+C will terminate the server in the terminal**
             

# Sample Input/Output:   
Input on terminal 1:   
    
    python3 httpserver.py   
Input on terminal 2:   

    wget http://remote04.cs.binghamton.edu:47590/test.html
Output on terminal 1:   

    Server Initialized   
    Host:  0.0.0.0  Port:  47590   
    test.html | 128.226.114.207 | 32998 | 1   
Output on terminal 2:   

    --2020-02-20 00:15:19--  http://remote04.cs.binghamton.edu:47590/test.html   
    Resolving remote04.cs.binghamton.edu (remote04.cs.binghamton.edu)... 128.226.114.204   
    Connecting to remote04.cs.binghamton.edu (remote04.cs.binghamton.edu)|128.226.114.204|:47590... connected.   
    HTTP request sent, awaiting response... 200 OK   
    Length: 279 [text/html]   
    Saving to: ‘test.html’   
    test.html   
    100%[==========================================================================================================================================================>]     279  --.-KB/s    in 0s   
    2020-02-20 00:15:19 (40.6 MB/s) - ‘test.html’ saved [279/279]   
    mgomez4@remote07:~/cs457/cs457-557-spring20-pa1-MGomez99$ 
    
