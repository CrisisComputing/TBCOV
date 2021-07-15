#USER LOCATION PREPROCESSING

#!/usr/bin/python3.7.0

"""
   Created by Umair Qazi - 
   Research Assistant at 
   Qatar Computing Research Institute
   Jul 15, 2018
"""

# -*- coding: utf-8 -*- 
from cleantext import clean
import re
import emoji
import unicodedata
import sys

PUNCT_TRANSLATE_UNICODE = dict.fromkeys(
    (i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("P")),
    " ",
)

def preprocess_user_location(text):
    #print("Orginal: " + text)

    if(text == None):
        return None
    
    text = text.strip()
    # remove URLs
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', ' ', text)
    text = re.sub(r'http\S+', ' ', text)
    # remove usernames
    text = re.sub('@[^\s]+', ' ', text)
    # remove the # in #hashtag
    text = re.sub(r'#([^\s]+)', r'\1', text)

    #remove emojies
    text = emoji.get_emoji_regexp().sub(u'', text)

    text = text.replace('\n',' ')
    text = text.replace('\t',' ')
    text = text.replace('\r',' ')
    text = text.replace('"',' ')
    text = text.replace('~',' ')
    text = text.replace('|',' ')
    text = text.replace(',','<<<<comma>>>>')


    preprocessed_text = clean(text,
        fix_unicode=True,               # fix various unicode errors
        to_ascii=True,                  # transliterate to closest ASCII representation
        lower=False,                     # lowercase text
        no_line_breaks=True,           # fully strip line breaks as opposed to only normalizing them
        no_urls=True,                  # replace all URLs with a special token
        no_emails=True,                # replace all email addresses with a special token
        no_phone_numbers=True,         # replace all phone numbers with a special token
        no_numbers=False,               # replace all numbers with a special token
        no_digits=False,                # replace all digits with a special token
        no_currency_symbols=True,      # replace all currency symbols with a special token
        no_punct=True,                 # fully remove punctuation
        replace_with_url="",
        replace_with_email="",
        replace_with_phone_number="",
        replace_with_currency_symbol="",
        # replace_with_punct=" ",
        # lang="en"                       # set to 'de' for German special handling
    )

    #accent remove
    text = text.translate(PUNCT_TRANSLATE_UNICODE)

    text = text.replace('<<<<comma>>>>',',')
    
    #remove extra spaces
    text = re.sub(' +', ' ', text)


    #print("Final: "+ text)

    # to avoid cases like ', '
    #to avoid cases like ' ', 'a', ',' etc
    #to avoid cases like ' E',
    if(len(text.replace(',','')) > 1 and len(text.replace(',','').replace(' ','')) > 1 and len(text.replace(' ','')) > 1 and len(text) > 1 and text != '' and text != ' '):
        return text
    else:
        return None



#some tests
print(preprocess_user_location('Doha, Qatar    ####'))
#Converts it to Doha, Qatar

print(preprocess_user_location(' USA     '))
#Converts it to USA



