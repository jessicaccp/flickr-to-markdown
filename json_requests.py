from urllib import request
from json import loads

number_page = 1

def get_json_data(url):
    try:
        response = request.urlopen(url)
    except:
        raise SystemExit("Error while requesting JSON data.")
    else:
        print("Successfully received data from Flickr.")
        json_data = loads(response.read())
        check_json_stat(json_data)
        return json_data

def check_json_stat(json_data):
    if json_data['stat'] == 'ok':
        return
    elif json_data['stat'] == 'fail':
        raise SystemExit("Flickr returned 'fail'. " + \
            "Check your config file and try again.\n" + \
            "Error code: %s - %s" % (json_data['code'], json_data['message']))
    else:
        raise SystemExit("Error while reading JSON data.")

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