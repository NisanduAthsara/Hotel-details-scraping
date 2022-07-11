from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os.path

def scraping_hotels(hotel):
    title = hotel.find('header',class_='bui-spacer--medium').a['title'].strip().replace('\n','')
    rating = hotel.find('div',class_='bui-review-score__badge').text.strip()
    review_count = hotel.find('div',class_='bui-review-score__text').text.strip().replace(' reviews','')
    price = hotel.find('div',class_='bui-price-display__value bui-f-color-constructive').text.strip()
    link = hotel.find('header',class_='bui-spacer--medium').a['href']
    link = f"https://www.booking.com{link}"
    return title,rating,review_count,price,link

def get_hotels(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content,'lxml')
    hotels = soup.find_all('div',class_='sr__card js-sr-card')

    file_exists = os.path.exists('hotels/hotel.txt')
    if file_exists == False:
        with open('hotels/hotel.txt','w') as file:
            for hotel in hotels:
                title,rating,review_count,price,link = scraping_hotels(hotel)
                file.write(f"{title}\n")
                file.write(f"Rating: {rating}\n")
                file.write(f"Review Amount: {review_count}\n")
                file.write(f"Price per night: {price}\n")
                file.write(f"More Info: {link}\n")
                file.write("\n\n\n")
        print('File wrote with hotel details...!')        
    else:
        print('Your file already has previous data. Shall we overwrite it? \nEnter t if you agree and enter f if you disagree')
        isOveride = input('>')
        if isOveride == 't':
            with open('hotels/hotel.txt','w') as file:
                for hotel in hotels:
                    title,rating,review_count,price,link = scraping_hotels(hotel)
                    file.write(f"{title}\n")
                    file.write(f"Rating: {rating}\n")
                    file.write(f"Review Amount: {review_count}\n")
                    file.write(f"Price per night: {price}\n")
                    file.write(f"More Info: {link}\n")
                    file.write("\n\n\n")
            print('File wrote with hotel details...!')        
        elif isOveride == 'f':
            date = datetime.now()
            formated_name = date.strftime("%Y-%m-%d")
            with open(f'hotels/{formated_name}.txt','w') as file:
                for hotel in hotels:
                    title,rating,review_count,price,link = scraping_hotels(hotel)
                    file.write(f"{title}\n")
                    file.write(f"Rating: {rating}\n")
                    file.write(f"Review Amount: {review_count}\n")
                    file.write(f"Price per night: {price}\n")
                    file.write(f"More Info: {link}\n")
                    file.write("\n\n\n")
            print('File wrote with hotel details...!')        
        else:
            print('Invalid input...!')    
            print('Unable to write a file with hotel details...!')    

if __name__ == '__main__':
    print('Enter the destination where you liked to visit among Nuwara Eliya,Kandy,Colombo,Ella,Anuradhapura,Jaffna,Badulla,Matale')
    destination = input('>')     
    print(f"Searching hotels in {destination}")
    destination = destination.replace(' ','').lower()

    nuwara_eliya_link = 'https://www.booking.com/city/lk/nuwara-eliya.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gCieSvlgbAAgHSAiQ2YjczZDhhMi0zYTY1LTRjNDgtOTgyMy1hYjE2YTliZjRlNGHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    kandy_link = 'https://www.booking.com/city/lk/kandy.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    colombo_link = 'https://www.booking.com/city/lk/colombo.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    ella_link = 'https://www.booking.com/city/lk/ella.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    anuradhapura_link = 'https://www.booking.com/region/lk/anuradhapura.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    jaffna_link = 'https://www.booking.com/region/lk/jaffna.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    badulla_link = 'https://www.booking.com/region/lk/nuwara-eliya.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'
    matale_link = 'https://www.booking.com/region/lk/matale.html?aid=356980&label=gog235jc-1DCAIohQFCAmxrSDNYA2iFAYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gC7t6wlgbAAgHSAiRjOGI2ZTQ3Yi03YzA0LTQ2OWItYmQ3Mi0yMTY3NTdhMzRkNTHYAgTgAgE&sid=22ce85d4d362d3742f5d85dde1468db2'

    if destination == 'nuwaraeliya':
        get_hotels(nuwara_eliya_link)
    elif destination == 'kandy':
        get_hotels(kandy_link)
    elif destination == 'colombo':
        get_hotels(colombo_link)
    elif destination == 'ella':
        get_hotels(ella_link)
    elif destination == 'anuradhapura':
        get_hotels(anuradhapura_link)
    elif destination == 'jaffna':
        get_hotels(jaffna_link)
    elif destination == 'badulla':
        get_hotels(badulla_link)
    elif destination == 'matale':
        get_hotels(matale_link)        
    else:
        print('Invalid Destination...!')              