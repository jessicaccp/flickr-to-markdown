from to_markdown import *

def json_processing(photo, is_photoset):
    if is_photoset:
        src = photo['url_m']
        owner = photo['ownername']
        owner = owner[1:]
    else:
        src = photo['url_l']
        owner = photo['owner']

    alt = ""
    title = photo['title']
    id = photo['id']
    flickr_url = "https://flickr.com/photos/" + owner + "/" + id
    return title, alt, src, flickr_url

def write_page(file, data):
    f = open(file, "w", encoding='utf-8')
    header = get_markdown_header()
    f.write(header)
    first_data_key = list(data.keys())[0]

    if first_data_key == 'photos':
        for x in data['photos']['photo']:
            title, alt, src, flickr_url = json_processing(x, is_photoset=False)
            f.write(get_markdown_photo(title, alt, src, flickr_url))

    elif first_data_key == 'photoset':
        for x in data['photoset']['photo']:
            title, alt, src, flickr_url = json_processing(x, is_photoset=True)
            f.write(get_markdown_photo(title, alt, src, flickr_url))

    else:
        raise ValueError('JSON error.')
    f.close()