from flask import Flask, render_template, request, url_for, redirect
from database import ans

from news import news

import sqlite3

connect = sqlite3.connect('User_Data.db')


app = Flask(__name__)









@app.route('/')
def main():
    return render_template('main.html', new = news.final )


@app.route("/get")
def get_bot_response_1():
    userText = request.args.get("msg") 
    userText = userText.lower()
    if 'report' in userText :
        return "<a href = 'report.html'> Click here to report player </a>"
    elif 'contact' in userText:
        return "<a href = 'contact_us.html'> Click here to contact us </a>"
    elif 'about' in userText :
        return "<a href = 'about_us.html'> Click here to know about us  </a>"
    elif 'profile' in userText  :
        return "<a href = 'details.html'> Click here to search for a player </a>"
    elif 'hi' in userText :
        return "Hi"
    elif ('name' in userText) or ('peru' in userText) :
        return 'Carlo'
    else:
        return "I don't understand what you are saying"
        


@app.route('/main.html')
def home():
    return render_template('main.html',new = news.final)


@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')


@app.route('/contact_us.html')
def contact_us():
    return render_template('contact_us.html')


@app.route('/report.html')
def report():
    return render_template('login.html', id = "")

@app.route('/details.html')
def details():
    name = ans.ans()
    name = ['','','','','','','']
    return render_template ("details.html", title = "Profile", image = "https://i.ibb.co/ZLqQ6L1/conq-removebg-preview.png", name = name  )


@app.route('/report.html/<id>')
def report_with_id(id):
    return render_template('report.html', id = id)

@app.route('/login.html')
def login_page():
    return render_template('login.html')


@app.route('/details.html/<id>')
def profile(id):
    with sqlite3.connect("User_Data.db") as conn:
        cur = conn.cursor()
        gen = cur.execute(''' SELECT *  FROM USERS  WHERE ID = (?)''', (id,))
        for i in gen:
            name = i
            dict_of_tiers = {
                "CONQUERER":"https://i.ibb.co/ZLqQ6L1/conq-removebg-preview.png",
                "ACE":"https://i.ibb.co/JyBMYw3/ace-removebg-preview-1.png",
                "CROWN":"https://i.ibb.co/z6kPWdg/cr-removebg-preview.png",
                "DIAMOND":"https://i.ibb.co/T1bkZVV/dia-removebg-preview.png",
                "PLATINUM":'https://i.ibb.co/FnRQRbC/lat-removebg-preview-1.png',
                "GOLD":'https://i.ibb.co/0yQ5TXq/gold-removebg-preview.png',
                "SILVER":'https://i.ibb.co/mCMqswG/silver-removebg-preview-1.png',
                "BRONZE":'https://i.ibb.co/Ht7WKz1/bronze-removebg-preview.png',

                }
            return render_template('details.html', title = name[1], image = dict_of_tiers[name[3]], name = name)


@app.route('/bot')
def bot():
    return render_template('bot.html')


if __name__ == "__main__":
    app.run(debug=True)



