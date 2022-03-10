from bs4 import BeautifulSoup
from randomstring import make
import requests as re
import json, wget, os, urllib


class HandleAll():
    def __init__(self):
        self.random_string = make.make_random_string()
    def send_request(self, url):
        self.req = re.get(url)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
        return self.req, self.soup

    def save_image(self):
        for image in self.soup.select('.img-fluid'):
            try:
                wget.download(url=image.get('src'), out=self.random_string)
            except urllib.error.HTTPError:
                print("no photo.")
    
    def save_json(self, information):
        with open(os.path.join(self.random_string, f'{self.random_string}.json'), 'w', encoding='utf-8') as file:
            json.dump(information, file, indent=4, ensure_ascii=False)
    
    def create_directory(self):
        try:
            os.mkdir(self.random_string)
        except Exception as e:
            print(e)
    
    def main(self):
        if bool(self.soup.select("tr:nth-child(9)")):
            name = self.soup.find('h1', class_="card-title").get_text().strip()
            for text in self.soup.select('tr:nth-child(3) .boldTr'):
                shabak = text.get_text().strip()

            for text in self.soup.select('tr:nth-child(2) .boldTr'):
                author = text.get_text().strip()

            for text in self.soup.select('tr:nth-child(1) .boldTr'):
                writers = text.get_text().replace('\n','').replace('\r', '').replace(' ', '').strip().strip()

            for text in self.soup.select('tr:nth-child(9) .boldTr'):
                page = text.get_text().strip()[40:44]+' صفحه'

            for text in self.soup.select('tr:nth-child(5) .boldTr'):
                price = text.get_text().strip()+' ریال'

            for text in self.soup.select('tr:nth-child(9) .boldTr'):
                description = text.get_text().replace('\n','').replace('\r', '').replace(' ', '').strip()
            
            self.create_directory()
            self.save_image()
            
            information = {
                'نام': name,
                'شابک': shabak,
                'انتشارات': author,
                'نویسنده': writers,
                'تعداد صفحات': page,
                'قیمت': price,
                'توضیحات': description
            }
            self.save_json(information)
        
        else:
            name = self.soup.find('h1', class_="card-title").get_text().strip()
            for text in self.soup.select('tr:nth-child(2) .boldTr'):
                author = text.get_text().strip()

            for text in self.soup.select('tr:nth-child(1) .boldTr'):
                writers = text.get_text().replace('\n','').replace('\r', '').replace(' ', '').strip().strip()

            for text in self.soup.select('tr:nth-child(8) .boldTr'):
                page = text.get_text().strip()[40:44]+' صفحه'

            for text in self.soup.select('tr:nth-child(4) .boldTr'):
                price = text.get_text().strip()+' ریال'

            for text in self.soup.select('tr:nth-child(8) .boldTr'):
                description = text.get_text().replace('\n','').replace('\r', '').replace('  ', '').strip()
            
            self.create_directory()
            self.save_image()
            
            information = {
                'نام': name,
                'انتشارات': author,
                'نویسنده': writers,
                'تعداد صفحات': page,
                'قیمت': price,
                'توضیحات': description
            }
            
            self.save_json(information)

create = HandleAll()