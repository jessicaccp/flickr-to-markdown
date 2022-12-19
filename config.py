from configparser import ConfigParser

def read_config_file():
    config = ConfigParser()
    check_config = config.read("config.ini")

    if check_config == []:
        raise SystemExit("Error while reading the config file.\n" + \
            "Please verify if there is a 'config.ini' on the folder and try again.")
    else:
        return config

def get_api_key(config):
    return config['API_KEY']['api_key']

def get_user_id(config):
    return config['IDs']['user_id']

def get_photoset_id(config):
    return config['IDs']['photoset_id']

def get_gallery_id(config):
    return config['IDs']['gallery_id']

def get_photos_per_page(config):
    return config['PHOTOS']['number_photos']

def get_option(config):
    return config['PHOTOS']['option']

def check_api_key(api_key):
    if api_key == '':
        raise SystemExit("API Key cannot be empty. Please edit your 'config.ini'.")
    return

def check_user_id(user_id):
    if user_id == '':
        raise SystemExit("User ID cannot be empty. Please edit your 'config.ini'.")
    return

def check_photoset_id(photoset_id):
    if photoset_id == '':
        raise SystemExit("Photoset ID cannot be empty. Please edit your 'config.ini'.")
    return

def check_gallery_id(gallery_id):
    if gallery_id == '':
        raise SystemExit("Gallery ID cannot be empty. Please edit your 'config.ini'.")
    return

def check_number_photos(number_photos):
    if number_photos == '':
        raise SystemExit("Number of photos cannot be empty. Please edit your 'config.ini'.")
    else:
        try:
            int_number_photos = int(number_photos)
        except:
            raise SystemExit("Number of photos must be an integer number. Please edit your 'config.ini'.")
        else:
            if int_number_photos < 1 or int_number_photos > 100:
                raise SystemExit("Number of photos must be an integer between 1 and 100. Please edit your 'config.ini'.")
            return