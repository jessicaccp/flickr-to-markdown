from datetime import datetime

def get_markdown_photo(title, src, flickr_url):
    code = '[![](' + str(src) + \
    ' "' + str(title) + \
    '")](' + str(flickr_url) + ')\n\n'
    return code

def get_markdown_header():
    title = '"Gallery"'
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    draft = "true"
    header = "---\ntitle: " + title + \
        "\ndate: " + date + \
        "\ndraft: " + draft + "\n---\n\n"
    return header