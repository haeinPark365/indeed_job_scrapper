import requests
from bs4 import BeautifulSoup


def get_last_page(URL):
  request = requests.get(URL)
  soup = BeautifulSoup(request.text,"html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_pages = pages[-2].find("span").string
  return int(last_pages)


def extract_jobs(last_page, URL):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO: Page: {page}")
    request = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(request.text,"html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  
  return jobs


def extract_job(html):
  title = html.find("h2",{"class":"mb4"}).find("a")["title"]
  company, location = html.find("h3").find_all("span", recursive=False) # unpacking
  #recursive는 span안에 포함된 span을 가져오지 않도록

  company = company.get_text(strip=True)
  location = location.get_text(strip=True)

  job_id = html['data-jobid']

  return {
    'title': title, 
    'company': company, 
    'location': location, 
    'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def get_jobs(word):
  
  URL = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(URL)
  jobs = extract_jobs(last_page, URL)
  return jobs