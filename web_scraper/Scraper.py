import requests
from bs4 import BeautifulSoup

# getting the html form the static websites and javascript in case of dynamic websites
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

#TODO add convertion of javascript to html for dynamic websites

# parsing using beautiful soup directly done for static websites and
# converting to html for dynamic website and then parsing it
soup = BeautifulSoup(page.content, 'html.parser')

# filtering the page content for a result set with id (here id='ResultsContainer') and
# printing the pretty results
results = soup.find(id='ResultsContainer')
print(results.prettify())

# finding all the job results using class and printing all of them
# here you can see the diff between find and find_all
# python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
# above is example to search jobs for python developer if all job listings are in h2 tag
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)


# each job_elem is a new BeautifulSoup object.
# you can use the same methods on it as you did before.
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# to search for apply links in above jobs use the below code
# for p_job in python_jobs:
    # link = p_job.find('a')['href']
    # print(p_job.text.strip())
    # print(f"Apply here: {link}\n")


