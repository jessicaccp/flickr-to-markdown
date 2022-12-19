# flickr-to-markdown

![](https://img.shields.io/github/languages/top/jessicaccp/flickr-to-markdown?style=flat) 
![](https://img.shields.io/github/languages/code-size/jessicaccp/flickr-to-markdown?style=flat) 
![](https://img.shields.io/github/issues/jessicaccp/flickr-to-markdown?style=flat) 
![](https://img.shields.io/github/license/jessicaccp/flickr-to-markdown?style=flat) 
![](https://img.shields.io/github/last-commit/jessicaccp/flickr-to-markdown/main?style=flat)

Generates a Markdown file, Hugo based, with photos from Flickr using Python 3.

## Table of Contents

* [Installation](#installation)
* [Configuration](#configuration)
* [Options](#options)
* [Running](#running)
* [Output](#output)

## Installation

```bash
git clone git@github.com:jessicaccp/flickr-to-markdown.git
cd flickr-to-markdown
```

## Configuration

Inside the directory, there is a file `_config.ini`. It must be renamed to `config.ini` and filled with your information, as explained below.

| Variable | Example | Description | How to get |
|---|---|---|---|
| api_key | 32-digit string | A key needed to get the data from Flickr. | You must [apply](https://www.flickr.com/services/apps/create/apply/) for a non-comercial key at App Garden from Flickr. |
| user_id | 11321214@N05 | The user's NSID. | Look for *Your user ID* on [this page](https://www.flickr.com/services/api/explore/?method=flickr.people.getInfo). |
| photoset_id | 72177720298974467 | Photoset is an old reference for an album. An album's ID. | At Flickr's main menu, look for *You* and then *Albums*, choose one and copy the long number at the end of the url. |
| gallery_id | 72157721382143850 | The ID for a gallery curated by someone on Flickr. | You can look up on *You* and then *Galleries* or on *Explore* and *Flickr Galleries*. Choose one and copy the long number at the end of the url. |
| number_photos | 15 | The number of photos you want to show at the generated markdown page. | It must be between 1 and 100. |
| option | 1 | The number for an option of what you want to generate. I'll explain better below. | It must be between 1 and 5. |

## Options

| Number | What it shows at generated page | Required config(*) |
|---|---|---|
| 1 | An user's recent public photos. | api_key, user_id, number_photos, option |
| 2 | Photos from an user's photoset/album. | api_key, photoset_id, user_id, number_photos, option |
| 3 | Photos from a gallery. | api_key, gallery_id, number_photos, option |
| 4 | An user's favorite photos. | api_key, user_id, number_photos, option |
| 5 | An user's most popular photos. | api_key, user_id, number_photos, option |

> (*) You may not modify the default config for the variables you won't use, but don't erase them.

## Running

After editing and renaming the config file to `config.ini`:

```bash
python3 app.py
```
The command will run the project's app and generate an output file named `output.md` on the same folder.

## Output

You may edit the output as you wish, add more parameters and texts. Just remember to change the `draft: True` to  `draft: False` and copy/move the file to your website content's folder.

The project uses YAML formatting for the front matter/header.

If you're using Hugo, for more information about parameters and front matter, [read here](https://gohugo.io/content-management/front-matter/). 