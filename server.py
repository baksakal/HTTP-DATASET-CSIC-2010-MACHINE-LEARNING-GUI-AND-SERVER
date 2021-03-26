from flask import Flask, request, jsonify
from train import *

#from prep import *
#from train import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    #print(request.method + " " + request.base_url)
    #print("User-Agent: "+request.headers.get('User-Agent'))
    #print("Accept: "+request.headers.get('Accept'))
    #print("Accept-Encoding: "+request.headers.get('Accept-Encoding'))
    #print("Accept-Charset: "+ str(request.headers.get('Accept-Charset')))
    #print("Accept-Language: "+request.headers.get('Accept-Language'))
    #print("Host: "+request.headers.get('Host'))
    #print("Connection: "+request.headers.get('Connection'))
    #print(request.headers.get('Content-Length'))
    #print(request.get_data())

    req = str(request.method) + " " + str(request.base_url) + "\n" + "User-Agent: " + str(request.headers.get('User-Agent')) + "\n" + "Accept: " + str(request.headers.get('Accept')) + "\n" + "Accept-Encoding: " +str(request.headers.get('Accept-Encoding')) + "\n" + "Accept-Charset: "+ str(request.headers.get('Accept-Charset')) + "\n" + "Accept-Language: " + str(request.headers.get('Accept-Language')) + "\n" + "Host: " + str(request.headers.get('Host')) + "\n""Connection: " + str(request.headers.get('Connection')) + "\n" + str(request.headers.get('Content-Length')) + "\n" + str(request.get_data())
    req = calcFeatures([req],2)
    res = model.predict(scaler.transform(req))

    # POST curl --data 'AAAAAAAAAAAAAAAAAAAA' http://127.0.0.1:5000
    # curl http://127.0.0.1:5000

    if res == [0]:
        return("Safe")
    else:
        return("Malicious")
        
if __name__ == '__main__':
    app.run()



