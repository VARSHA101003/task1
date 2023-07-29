import request
from bs4 import BeautifulSoup
import panda
import argparse
import connect

parser= argparse.ArgumentParser()
parser.add_agrument("--page_num_max",help="Enter the number of pages to parse", type=int)
parser.add_agrument("--dbname",help="Enter the name of db",type=str)
args=parser.parse_args()

oyo_url= "hhtps://www.oyorooms.com/hotels-in-bangalore/?page="

page_num_max=args.page_num_max
scrapped-info_list=[]
connect.connect(args.dbname)

for page_num in range(1,page_num_max):
    url=oyo_url+str(page_num)
    print("get request for:" + url)

    req=requests.get(url)
    content=req.content

    soup=BeautifulSoup(cotent,"html.parser")

    all_hotels= soup.find_all("div",{"class": "hotelCardlisting"})

    for hotel in all_hotels:
        hotel_dict={}

        hotel_dict["name"]=hotel.find("h3",{"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop": "streetaddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class": "listingprice__finalprice"}).text
        #try...except
        try:
            hotel_dict["rating"]=hotel.find("span",{"class": "hotelRating__ratingsummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None 

        parent_amenities_elemanet=hotel.find("div",{"class": "amenityWrapper__amenity"})

        amenities_list=[]
        for amenity in parent_amenities_element.find_all("div",{"class": "amenityWrapper_-amenity"}):
         ameneties_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"]=' , '.join(amenities_list[:-1])

        scrapped_info_list.append(hotel_dict)
        connect.insert_into_table(arg.dbname,tuple(hotel_dict.values())

    # print(hotel_name, hotel_price, hotel_rating, amenities-list)

dataFrame= pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv("oyo.csv")
print("creating csv file ...")
connect.get_hotel_info(args.dbname)

         
