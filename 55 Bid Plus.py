"""
PROBLEM 55
Write a program to print the output of the following poblem statement :-
USE SELENIUM
Write a Python code to Scrap data and download data from given url.
url = "https://bidplus.gem.gov.in/bidlists"
Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
 
     Make a csv file add all data in it.
     csv Name: bid_plus.csv?
"""

from  selenium import webdriver
import pandas as pd

bid_url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get(bid_url)
    
bid_num, item, quantity_request, dept_det, date_start, time_start, date_end, time_end, pdf= [], [], [], [], [], [], [], [], []

for i in range(1,11):
    bid_num = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.replace("\n"," ")
    bid_num.append(bid_num)    
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.replace("\n"," ")
    item.append(item)    
    quantity_req = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.replace("\n"," ")
    quantity_request.append(quantity_request)    
    dept_details = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.replace("\n"," ")
    dept_det.append(dept_det)    
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:10]
    date_start.append(date_start)    
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    time_start.append(time_start)    
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:10]
    date_end.append(date_end)    
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    time_end.append(time_end)
    pdf_button = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')


DataFrame = pd.DataFrame()
DataFrame["Bid Number :"] = bid_num
DataFrame["Items :"] = item
DataFrame["Quantity Required :"] = quantity_request
DataFrame["Department Name :"] = dept_det
DataFrame["Start Date :"] = date_start
DataFrame["Start Time :"] = time_start
DataFrame["End Date :"] = date_end
DataFrame["End Time :"] = time_end


DataFrame.to_csv("bid.csv")

browser.quit()



