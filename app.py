from config import *
from json_requests import *
from data_processing import *

def switch(option, config):
    api_key = get_api_key(config)
    check_api_key(api_key)
    number_photos = get_photos_per_page(config)
    check_number_photos(number_photos)

    user_id = get_user_id(config)
    photoset_id = get_photoset_id(config)
    gallery_id = get_gallery_id(config)

    if option == "1":
        check_user_id(user_id)
        data = get_data_public_photos(api_key, user_id, number_photos)

    elif option == "2":
        check_user_id(user_id)
        check_photoset_id(photoset_id)
        data = get_data_photoset(api_key, photoset_id, user_id, number_photos)

    elif option == "3":
        check_gallery_id(gallery_id)
        data = get_data_gallery(api_key, gallery_id, number_photos)

    elif option == "4":
        check_user_id(user_id)
        data = get_data_favorites(api_key, user_id, number_photos)

    elif option == "5":
        check_user_id(user_id)
        data = get_data_most_popular(api_key, user_id, number_photos)

    else:
        raise SystemExit("Option value not valid. Please edit your 'config.ini'.")
    
    return data

def main():
    config = read_config_file()
    option = get_option(config)
    data = switch(option, config)
    file = 'output.md'
    write_page(file, data)

main()