from bs4 import BeautifulSoup
import json
import requests
import socket

def runImageScraper():
    host = socket.gethostname()
    port = 7439

    # creates the socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binds host and port
    s.bind((host, port))

    # server listens with a buffer of 6
    s.listen(6)

    while True:
        # accepts and establishes a new connection
        clientsock, address = s.accept()
        print("connection established with: " + str(address))

        # decode the client request and save the query input
        request = clientsock.recv(1024).decode("utf-8")
        jsonrequest = json.loads(request)
        query = jsonrequest["query"]

        # make the bing search based on the user's inputs
        bingsearch = "https://bing.com/images/search?q=" + query
        print(bingsearch)
        
        # use a user agent to search
        user_agent = {'User-Agent': 'Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)'}
        bingresponse = requests.get(bingsearch, headers=user_agent)
 
        # use beautiful soup to find images related to that query and save them to a dict object
        soup = BeautifulSoup(bingresponse.content, "html.parser")
        images = soup.find_all('a', class_='iusc')

        # Return only 15 results
        image_list = {}
        i = 1
        images = images[0:15]
        for image in images:
            m = json.loads(image["m"])
            murl = m["murl"]
            image_list[str(query) + str(i)] = murl
            i += 1
            
        # convert the dictionary object to a json object and send to client
        response = json.dumps(image_list)
        clientsock.send(response.encode("utf-8"))
        clientsock.close()

if __name__ == '__main__':
    runImageScraper()
       




