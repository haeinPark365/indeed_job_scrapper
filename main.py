from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {} #report나 home이 재실행되어도 초기화되지않도록

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word : #word가 none이 아닐때
    word = word.lower()
    from_db = db.get(word)
    if from_db: #from_db가 비어있지(none) 않을때
      jobs = from_db
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else :
    return redirect("/")
  return render_template(
    "report.html",
    searchingBy = word, 
    results_number = len(jobs),
    jobs = jobs
  )


app.run(host = "0.0.0.0")