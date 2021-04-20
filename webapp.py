import random
import string
from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

if __name__=="__main__":
    app.run(debug=False, port=54321)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/response', methods=['GET'], ['POST'])
def render_response():
    if request.method == 'POST':
        length = request.form['length'] 
        amount = request.form['amount'] 
        color = request.form['color'] 
        pet = request.form['pet']
        symbol = request.form['symbol'] 
        number = request.form['number'] 
        replyTwo = ""
        if length != "" and amount != "" and length.isnumeric() and amount.isnumeric() and int(amount) < 101 and int(length) < 51:
            if int(length) <= 5:
                reply = "Your password must have more than 5 characters."
            elif int(amount) <= 0:
                reply = "Generate at least 1 password."
            else:
                reply = "Passwords:"
            keyWord = color
            keyWordTwo = pet
            if reply == "Passwords:":
                for x in range(0, int(amount)):
                    keyWord = color
                    keyWordTwo = pet
                    while (len(keyWord) + len(keyWordTwo)) >= (int(length) - 2):
                        rand = random.randrange(0, 2)
                        if rand == 0 and len(keyWord) >= 2:
                            rand = random.randrange(1, len(keyWord))
                            keyWord = keyWord[0:rand]
                        elif len(keyWordTwo) >= 2:
                            rand = random.randrange(1, len(keyWordTwo))
                            keyWordTwo = keyWordTwo[0:rand]
                    randB = random.randrange(0, 2)
                    if randB == 0:
                        replyTwo = replyTwo + keyWord + keyWordTwo
                    else:
                        replyTwo = replyTwo + keyWordTwo + keyWord
                    for y in range(0, (int(length) - len(keyWord) - len(keyWordTwo))):
                        if symbol == "true" and number == "true":
                            replyTwo = replyTwo + random.choice(string.digits + string.punctuation)
                        elif symbol == "true":
                            replyTwo = replyTwo + random.choice(string.punctuation)
                        elif number == "true":
                            replyTwo = replyTwo + random.choice(string.digits)
                        else:
                            replyTwo = replyTwo + "█"
                    if (x+1) != int(amount):
                        replyTwo = replyTwo + " _______ "
            else:
                replyTwo = ""
        elif (length.isnumeric() == False or length == "") and (amount.isnumeric() == False or amount == ""):
            reply = "Please specify a length between 5 and 50 and amount between 1 and 100."
        elif length == "" or length.isnumeric() == False or int(length) > 50:
            reply = "Please specify a length between 6 and 50."
        elif amount == "" or amount.isnumeric() == False or int(amount) > 100:
            reply = "Please specify an amount between 1 and 100."
        else:
            reply = "There was an error processing your request."
        return render_template('response.html', response = reply, responseTwo = replyTwo)
    else:
        return render_template('home.html')
