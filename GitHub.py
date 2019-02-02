"""
Scrape Site
"""

'''
from selenium import webdriver
import pickle

url1 = "http://www.thebaseballgauge.com/year.php?yearID="
url2 = "&tab=plays&type=HR&WPA=game&game_type=All&invTm=All&batTm=All&fldTm=All&awTm=All&hmTm=All&bases=All&outs=All&half=All&inning=All&results=500&page="
url3 = "&sort=WPA_a"

table_name = "freeze-three"

lst = []

for year in range(1998,2018):
    Page = True
    for i in range(1,20):
        if Page == False: break
        driver = webdriver.Chrome()
        driver.get(url1+str(year)+url2+str(i)+url3);
        table = driver.find_elements_by_class_name(table_name)
        for t in table:
            cell = t.find_elements_by_tag_name("td")
            for c in cell:
                if c.text == "Query has returned 0 results":
                    Page = False
                    break
                print(c.text)
                lst.append(c.text)
        print(i)
        driver.quit()

with open("data/AllResults.txt", "wb") as fp:  # Pickling
    pickle.dump(lst, fp)
'''


"""
Read Text
"""

'''
import pickle
import re
count = 0
results = []

header = ["Rk", "WPA", "LI", "Play", "Description", "Batter/Pitcher","Game", "Inn", "Outs", "Rnrs", "Score"]



Final = []
lst = []
with open("data/AllResults.txt", "rb") as fp:   # Unpickling
    data = pickle.load(fp)
for d in data:
    if d == "": continue
    score = re.match("^[0-9]*[-][0-9]*$", d)
    lst.append(d)
    if score:
        Final.append(lst)
        lst = []
        
with open("data/DctLst3.txt", "wb") as fp:   #Pickling
    pickle.dump(Final, fp)
    
    
import pickle


with open("data/DctLst3.txt", "rb") as fp:   # Unpickling
    data = pickle.load(fp)


    
    
#Add the number of runs scored from the HomeRun as a new column
newResults = []
for d in data:
    if "3-Run" in d[3]:
        d.append(3)
    if "Grand Slam" in d[3]:
        d.append(4)
    if "2-Run" in d[3]:
        d.append(2)
    if "Solo" in d[3]:
        d.append(1)
    newResults.append(d)    
'''


"""
Write to Excel
"""
from openpyxl import load_workbook

# Write Header to Excel:
Columns = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
Names = ["RK", "WPA", "LI", "Desc", "Batter", "Pitcher", "Date", "Inn", "Outs", "Score", "Runs"]


wb = load_workbook("data/AllResults.xlsx")
H = wb["Sheet1"]
index = 1


# Make Header
for c in range(len(Columns)):
    H[Columns[c]+str(index)] = Names[c]

index += 1
for row in newResults:
    for i in range(len(row)):
        H[Columns[i] + str(index)] = row[i]
    index += 1


wb.save("data/AllResults.xlsx")

'''
