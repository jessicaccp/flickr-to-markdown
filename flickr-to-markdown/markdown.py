from datetime import datetime

def get_markdown_photo(title, alt, src, flickr_url):
    code = '[![' + str(alt) + \
    '](' + str(src) + \
    ' "' + str(title) + \
    '")](' + str(flickr_url) + ')'
    return code

def get_markdown_header():
    title = '"Page Title"'
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    draft = "true"
    header = "---\ntitle: " + title + \
        "\ndate: " + date + \
        "\ndraft: " + draft + "\n---\n\n"
    return header

# def main():
#     print(get_markdown_header())

# main()