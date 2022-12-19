from to_markdown import *

def json_processing(photo, is_photoset):
    try:
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
    except:
        raise SystemExit("Error while processing JSON data. Invalid data.")
    else:
        flickr_url = "https://flickr.com/photos/" + owner + "/" + id
        return title, alt, src, flickr_url

def write_page(file, data):
    try:
        f = open(file, "w", encoding='utf-8')
    except:
        raise SystemExit("Error while creating/opening the output file.")
    else:
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
            raise SystemExit("Unexpected error with JSON data.")
            
        f.close()
        print("Successfully processed data. Your 'output.md' is ready.")