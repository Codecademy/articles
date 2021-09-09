import os, time, csv, re
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait



driver = Safari()

driver.get('http://www.olympedia.org/statistics/medal/country')
driver.implicitly_wait(10)

year_dd = driver.find_element_by_id('edition_select')
year_options = year_dd.find_elements_by_tag_name('option')

gender_dd = driver.find_element_by_id('athlete_gender') 
gender_options = gender_dd.find_elements_by_tag_name('option')

print(year_options[29].get_attribute('text'))

usa_lst = []


for gender in gender_options[1:]:
    gender.click()
    time.sleep(2)
    gender_val = gender.get_attribute('text')
    # print(year_options[0].get_attribute('text'))

    for year in year_options[2:]:
        year.click()
 
        time.sleep(1) # provide time for processing the page update

        the_soup = BeautifulSoup(driver.page_source, 'html.parser')
        

        try:
            year_val = year.get_attribute('text')
            head = the_soup.find(href=re.compile('USA'))
  
            medal_values = head.find_all_next('td',limit=5)
            val_lst = [x.string for x in medal_values[-4:]]
            
        except:
            val_lst = ['0' for x in range(4)]

        val_lst.append(gender_val)
        val_lst.append(year_val)

        usa_lst.append(val_lst)

        if year_val == '2020':
                break

driver.quit()

print(usa_lst[30])
print(usa_lst[31])


try:
    output_f = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output_f)
    for row in usa_lst:
        output_writer.writerow(row)

except:
    pass
finally:
    output_f.close()
    print('done')





