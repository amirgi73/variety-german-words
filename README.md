# variety-german-words

Plugin for Variety wallpaper changer 

A quotes plugin to show German words with translation and examples. A helpful way to get better at German

## Installation

- Change directory to plugin folder:

        $ cd ~/.config/variety/plugins

- Clone the repository:

        $ git clone https://github.com/amirgi73/variety-german-words.git
- Restart variety.
- Activate the plugin from Variety Preferences > Effects > Quotes > Sources and filtering.
- Activate Change quote every 30 Minutes from Variety Preferences > Effects > Quotes > Regular Change
## Requirements

Needs
- Variety - https://peterlevi.com/variety/

## Change Translation Language
Currently we support English and Persian. The default language is set to English. If you want to use Persian instead, use the commands bellow:

- to use translations from b-amooz.com:

        $ cd ~/.config/variety/plugins/variety-german-words
        $ sed -i '0,/English/s//Persian B-amooz/' german_words.py
- or to use translations from translate.google.com:

        $ cd ~/.config/variety/plugins/variety-german-words
        $ sed -i '0,/English/s//Persian G-translate/' german_words.py  
 
- Restart variety.
## Screenshots
![screenshot1](/screenshots/de_english.jpg?raw=true "With English translations")


## Notes

- This plugin was tested with Variety 0.8.3 (python 3.8)
- This plugin is in early development.

## Credits

Variety is developed by Peter Levi  - https://peterlevi.com/variety/

german_words.py is inspired by variety-goodreads-quotes  - https://github.com/dsbmac/variety-goodreads-quotes and variety-vdm-quotes  - https://github.com/LG666/variety-vdm-quotes


### License

MIT - Copyright(c) 2020 amirgi73
