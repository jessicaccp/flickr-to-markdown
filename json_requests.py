from urllib import request
import json

number_page = 1

def get_json_data(url):
    response = request.urlopen(url)
    json_data = json.loads(response.read())
    return json_data

def get_data_public_photos(api_key, user_id, number_photos):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "people.getPublicPhotos&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&extras=description%2C+url_l" + \
        "&per_page=" + str(number_photos) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_data_photoset(api_key, photoset_id, user_id, number_photos):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "photosets.getPhotos&api_key=" + str(api_key) + \
        "&photoset_id=" + str(photoset_id) + \
        "&user_id=" + str(user_id) + \
        "&extras=owner_name%2C+url_m" + \
        "&per_page=" + str(number_photos) + \
        "&page=" + str(number_page) + \
        "&media=photos&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_data_gallery(api_key, gallery_id, number_photos):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "galleries.getPhotos&api_key=" + str(api_key) + \
        "&gallery_id=" + str(gallery_id) + \
        "&extras=description%2C+url_l" + \
        "&per_page=" + str(number_photos) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_data_favorites(api_key, user_id, number_photos):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "favorites.getPublicList&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&extras=description%2C+url_l" + \
        "&per_page=" + str(number_photos) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data

def get_data_most_popular(api_key, user_id, number_photos):
    url = "https://www.flickr.com/services/rest/?method=flickr." + \
        "photos.getPopular&api_key=" + str(api_key) + \
        "&user_id=" + str(user_id) + \
        "&extras=description%2C+url_l" + \
        "&per_page=" + str(number_photos) + \
        "&page=" + str(number_page) + \
        "&format=json&nojsoncallback=1"
    data = get_json_data(url)
    return data