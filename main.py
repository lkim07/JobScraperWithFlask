from flask import Flask, render_template, request, redirect, send_file
import requests
from bs4 import BeautifulSoup
from job_scraper import searching, export_file

db={}
app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html", name="Laura")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")

  if keyword == None or keyword == "":
    return redirect("/")
  else: 
    keyword = keyword.lower()

  if keyword in db:
    jobs = db[keyword]
  else: 
    jobs = searching(keyword) 
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs, db=db)

@app.route("/export")
def export():
  keyword = request.args.get("keyword") 
  if keyword==None or keyword=="":
    return redirect("/")
  else: 
    keyword = keyword.lower()

  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  export_file(keyword, db[keyword])
  return send_file(f"{keyword}_jobs.csv", as_attachment=True)

if __name__ == "__main__":
  app.run("0.0.0.0")
