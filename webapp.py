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
    if int('length') < 6:
        reply = "Your password must be longer than 5 characters."
    else:
        reply = " "
    if int('amount') <= 0:
        replyTwo = "You must generate at least 1 password."
    else:
        replyTwo = " "
    replyThree = "Hi"
    return render_template('response.html', response = reply, responseTwo = replyTwo, responseThree = replyThree)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
