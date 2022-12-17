from to_markdown import *

def json_processing(photo):
    title = photo['title']
    alt = photo['description']['_content']
    src = photo['url_l']
    owner = photo['owner']
    id = photo['id']
    flickr_url = "https://flickr.com/photos/" + owner + "/" + id
    return title, alt, src, flickr_url

def write_page(file, data):
    f = open(file, "w", encoding='utf-8')
    header = get_markdown_header()
    f.write(header)
    for x in data['photos']['photo']:
        title, alt, src, flickr_url = json_processing(x)
        f.write(get_markdown_photo(title, alt, src, flickr_url))
    f.close()