from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

all_jobs = []
def scrape_page(url):
  print(f"Scrapping {url}...")
  response = requests.get(url)
  soup = BeautifulSoup(
    response.content, 
    "html.parser",
  )

  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    companies = job.find_all("span", class_="company")

    company = ''
    position = ''
    region = ''

    if len(companies) > 0:
      company = companies[0].text
    if len(companies) > 1:
      position = companies[1].text
    if len(companies) > 2:
      region = companies[2].text

    url = job.find("div", class_="tooltip--flag-logo").next_sibling
    if url:
      url = url["href"]

    job_data = {
      "title": title,
      "company": company,
      "position": position,
      "region": region,
      "url:": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url)    
  soup = BeautifulSoup(response.content, "html.parser")
  return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")
  
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)
  
print(len(all_jobs))