
from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs

"""
Indeed("https://kr.indeed.com") 에서 직업 정보를 받아와 웹페이지로 보여준후 csv 파일로 다운로드를 할 수 있다. 
"""
app = Flask("SuperScrapper")

db = {} 
#fake_DB (directory를 DB처럼 사용)
#report나 home이 재실행되어도 초기화되지않도록

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
    
  return render_template("report.html", searchingBy = word, results_number = len(jobs), jobs = jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    return send_file("jobs.csv")

  except:
    return redirect("/")
app.run(host = "0.0.0.0")

"""
from flask import Flask, render_template, request,  redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("BEAN MADE THIS")


db = {}


@app.route("/")
def home():
  return render_template("home.html")
#it's a same thing like instagram assessing ways 
#@ is decolator, so it just find a def

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")

  return render_template("report1.html", SearchingBy = word, resultsNumber= len(jobs), jobs =jobs)
  # it's a mechanism about the html&python


@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")

  except:
    return redirect("/")
app.run(host = "0.0.0.0")
# host = "0.0.0.0" this is a tool that it can be shown to us our page on repl.it
"""