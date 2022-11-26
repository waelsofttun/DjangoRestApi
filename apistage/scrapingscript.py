import requests
from bs4 import BeautifulSoup

from apistage.models import Offer





def scrapingmethod(key):
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    Result=[]
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title").text.strip()
        if key in title_element.lower():
            company_element = job_element.find("h3", class_="company").text.strip()
            location_element = job_element.find("p", class_="location").text.strip()
            print(title_element)
            print(company_element)
            print(location_element)
            offer=Offer(title=title_element,companyName=company_element,Keyword=key,place=location_element)
            offer.save()
            Result.append(offer)
    return Result    


        