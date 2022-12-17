import configparser

def read_config_file():
    config = configparser.ConfigParser()
    config.read("../config.ini")
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
    return config['PHOTOS']['photos_per_page']

# def main():
#     config = read_config_file()
#     print(get_api_key(config))
#     print(get_user_id(config))
#     print(get_photoset_id(config))
#     print(get_gallery_id(config))
#     print(get_photos_per_page(config))

# main()