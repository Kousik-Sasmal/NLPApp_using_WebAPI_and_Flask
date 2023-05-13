from flask import Flask,render_template,request, redirect,session
from database import Database
import api

db = Database()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('name_of_user')
    email = request.form.get('email_of_user')
    password = request.form.get('password_of_user')


    response = db.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('email_of_user')
    password = request.form.get('password_of_user')

    response= db.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message="Incorrect email or password!")

@app.route('/profile')
def profile():
        return render_template('profile.html')


# NER
@app.route('/ner')
def ner():
        return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response= api.ner(text)

    return render_template('ner.html',response=response)


# sentiment analysis
@app.route('/sentiment')
def sentiment():
        return render_template('sentiment.html')

@app.route('/perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    text = request.form.get('sentiment_text')
    sent_response= api.sentiment(text)

    sorted_list = sorted(sent_response['sentiment'].items(), key=lambda item: item[1],reverse=True)
    response = sorted_list[0][0]

    return render_template('sentiment.html',response=response)


# abuse detection
@app.route('/abuse')
def abuse():
        return render_template('abuse.html')

@app.route('/perform_abuse_detection',methods=['post'])
def perform_abuse_detection():
    text = request.form.get('abuse_text')
    abuse_response = api.abuse(text)
    sorted_list = sorted(abuse_response.items(), key=lambda item: item[1],reverse=True)
    response = sorted_list[0][0]
    return render_template('abuse.html',response=response)


# emotion detection
@app.route('/emotion')
def emotion():
        return render_template('emotion.html')

@app.route('/perform_emotion_detection',methods=['post'])
def perform_emotion_detection():
    text = request.form.get('emotion_text')
    emotion_response= api.emotion(text)

    sorted_list = sorted(emotion_response['emotion'].items(), key=lambda item: item[1],reverse=True)
    response = sorted_list[0][0]

    return render_template('emotion.html',response=response)



if __name__=="__main__":
     app.run(debug=True,host='0.0.0.0',port=5000)