from bs4 import BeautifulSoup, NavigableString
import requests

# url = 'https://schedules.calpoly.edu/courses_CSC_curr.htm'
subject = input("Department (ex 'CSC' or 'BUS'): ")
quarter = input("Quarter ('curr' or 'next'): ")

url = 'https://schedules.calpoly.edu/courses_' + subject + '_' + quarter + '.htm'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')
tbody = doc.tbody
trs = tbody.contents

d = {}

for tr in trs[1:]:
    if isinstance(tr, NavigableString):
        continue

    coursenum = tr.find("td", "courseName").a.string
    if coursenum in d:
        continue 
    
    coursename = tr.find("td", "courseDescr").string
    ecap = tr.find_all("td", "count", limit=2)[1].string
    enrl = tr.find_all("td", "count", limit=3)[2].string
    seats_left = (int)(ecap) - (int)(enrl)
    d[coursenum] = seats_left

    print(coursenum, coursename, "\nseats left = ", seats_left, "\n")
