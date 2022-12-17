from urllib import request
import json
from config import *

number_page = 1

def get_json_data(url):
    response = request.urlopen(url)
    json_data = json.loads(response.read())
    return json_data

def get_public_photos(api_key, user_id, photos_per_page):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "people.getPublicPhotos&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&per_page=" + str(photos_per_page) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_photoset(api_key, photoset_id, user_id, photos_per_page):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "photosets.getPhotos&api_key=" + str(api_key) + \
        "&photoset_id=" + str(photoset_id) + \
        "&user_id=" + str(user_id) + \
        "&per_page=" + str(photos_per_page) + \
        "&page=" + str(number_page) + \
        "&media=photos&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_gallery(api_key, gallery_id, photos_per_page):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "galleries.getPhotos&api_key=" + str(api_key) + \
        "&gallery_id=" + str(gallery_id) + \
        "&per_page=" + str(photos_per_page) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_favorites(api_key, user_id, photos_per_page):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "favorites.getPublicList&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&per_page=" + str(photos_per_page) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_most_popular(api_key, user_id, photos_per_page):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "photos.getPopular&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&per_page=" + str(photos_per_page) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

# def main():
#     config = read_config_file()
#     print(get_favorites(get_api_key(config), get_user_id(config), get_photos_per_page(config)))
#     print(get_gallery(get_api_key(config), get_gallery_id(config), get_photos_per_page(config)))
#     print(get_most_popular(get_api_key(config), get_user_id(config), get_photos_per_page(config)))
#     print(get_photoset(get_api_key(config), get_photoset_id(config), get_user_id(config), get_photos_per_page(config)))
#     print(get_public_photos(get_api_key(config), get_user_id(config), get_photos_per_page(config)))

# main()