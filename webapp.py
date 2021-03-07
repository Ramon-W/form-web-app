import random
import string
from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    length = request.args['length'] 
    amount = request.args['amount'] 
    color = request.args['color'] 
    pet = request.args['pet']
    symbol = request.args['symbol'] 
    number = request.args['number'] 
    if int(length) <= 5:
        reply = "Your password must have more than 5 characters."
    elif int(amount) <= 0:
        reply = "Generate at least 1 password."
    else:
        reply = "Passwords:"
    replyTwo = ""
    keyWord = color
    keyWordTwo = pet
    while len(keyWord) + len(keyWordTwo) <= int(length):
        rand = random.ranrange(0,2)
        if(rand == 0):
            keyWord = keyWord[0]
        else
            keyWordTwo = keyWordTwo[0]
    if reply == "Passwords:":
        for x in range(1, int(amount)):
            while len(keyWord) + len(keyWordTwo) <= int(length):
                rand = random.ranrange(0, 2)
                if rand == 0:
                    rand = random.ranrange(0, len(keyWord))
                    keyWord = keyWord[0]
                else:
                    rand = random.ranrange(0, len(keyWordTwo))
                    keyWordTwo = keyWordTwo[0]
            rand = random.ranrange(0, 2)
            if rand == 0:
                replyTwo = keyWord + keyWordTwo
            else:
                replyTwo = keyWordTwo + keyWord
            for y in range(1, int(length) + len(keyWord) + len(keyWordTwo):
                if symbol == "true" and number == "true":
                    replyTwo = replyTwo + random.choice(string.digits + string.punctuation)
                elif symbol == "true":
                   replyTwo = replyTwo + random.choice(string.punctuation)
                elif number == "true":
                    replyTwo = replyTwo + random.choice(string.digits)
            replyTwo = replyTwo + " _______ "
    else:
        replyTwo = ""
    return render_template('response.html', response = reply, responseTwo = replyTwo)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
