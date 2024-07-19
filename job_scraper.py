import requests
from bs4 import BeautifulSoup
import csv



def get_pages(url):
  response = requests.get(
      url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })
  soup = BeautifulSoup(response.content, "html.parser")

  num = len(
      soup.find("ul", class_="bsj-nav").find_all("a",
                                                 class_="page-numbers")) + 1

  return num


def scraper(url, all_jobs):
  response = requests.get(
      url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })

  soup = BeautifulSoup(response.content, "html.parser")

  jobs = soup.find_all("li", class_="bjs-jlid")

  for job in jobs:

    company_name = ""
    job_link = ""
    job_title = ""
    job_description = ""

    if (job.find("a")):
      job_link = job.find("a")["href"]


    if (job.find("a")):
      job_title = job.find("a").text


    if (job.find("a", class_="bjs-jlid__b")):
      company_name = job.find("a", class_="bjs-jlid__b").text


    if (job.find("div", class_="bjs-jlid__description")):
      job_description = job.find("div", class_="bjs-jlid__description").text


    if(job_title!="" and company_name!="" and job_description!="" and job_link!=""):
      job = {
          "company_name": company_name,
          "job_title": job_title,
          "job_description": job_description,
          "job_link": job_link
      }
      all_jobs.append(job)




def scraper_web3(url, all_jobs):
  response = requests.get(
      url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })

  soup = BeautifulSoup(response.content, "html.parser")

  table = soup.find("table", class_="table")
  jobs = table.find_all("tr", class_="table_row")


  for job in jobs:

    company_name = ""
    job_link = ""
    job_title = ""
    job_description = ""

    if (job.find("a")):
      job_link =f'https://web3.career{job.find("a")["href"]}'


    if (job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary")):
      job_title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text

    if (job.find_all("a")[1]):
      company_name = job.find_all("a")[1].text


    new_response = requests.get(
      job_link,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })
    new_soup = BeautifulSoup(new_response.content, "html.parser")


    if (new_soup.find("div", class_="text-dark-grey-text") and new_soup.find("div", class_="text-dark-grey-text").find("ul")):
      job_description = new_soup.find("div", class_="text-dark-grey-text").find_all("ul")[0].text


    if(job_title!="" and company_name!="" and job_description!="" and job_link!=""):
      job = {
          "company_name": company_name,
          "job_title": job_title,
          "job_description": job_description,
          "job_link": job_link
      }
      all_jobs.append(job)


def scraper_wwr(url, all_jobs):
  response = requests.get(
      url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })
  soup = BeautifulSoup(response.content, "html.parser")

  every_jobs = soup.find("div", class_="col-12 col-md-6")
  jobs = every_jobs.find_all("li", class_="feature") + every_jobs.find_all("li", class_="")


  for job in jobs:

    company_name = ""
    job_link = ""
    job_title = ""
    job_description = ""
    job_text = ""

    if (job.find_all("a")[1]):
      job_link =f'https://weworkremotely.com{job.find_all("a")[1]["href"]}'


    if (job.find("span", class_="title")):
      job_title = job.find("span", class_="title").text

    if (job.find("span", class_="company")):
      company_name = job.find("span", class_="company").text


    new_response = requests.get(
      job_link,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      })
    new_soup = BeautifulSoup(new_response.content, "html.parser")
    job_specification = new_soup.find("div", id="job-listing-show-container")

    
    if (job_specification.find_all("div")):
      job_description = job_specification.find_all("div")
      for i in range(len(job_description)):
        job_text = job_text + job_description[i].text + " " 


    if(job_title!="" and company_name!="" and job_text!="" and job_link!=""):
      job = {
        "company_name": company_name,
        "job_title": job_title,
        "job_description": job_text.strip(),
        "job_link": job_link
      }
      all_jobs.append(job)


    


def searching(keyword):
  all_jobs = []

  scraper(f"https://berlinstartupjobs.com/skill-areas/{keyword}/", all_jobs)
  scraper_web3(f"https://web3.career/{keyword}-jobs", all_jobs)
  scraper_wwr(
      f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
  , all_jobs)
  return all_jobs




def export_file(keyword, jobs_db):
    file = open(f"{keyword}_jobs.csv", mode="w", encoding='utf-8')
    writter = csv.writer(file)
    writter.writerow(["Title", "Company Name", "Description", "Link"])
    for job in jobs_db:
        writter.writerow(job.values())

    file.close()
