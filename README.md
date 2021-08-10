# TBCOV: Two Billion Multilingual COVID-19 Tweets with Sentiment, Entity, Geo, and Gender Labels
Welcome to the code repository for the TBCOV dataset. This code repository offers several scripts helpful to hydrate and process the shared dataset.

The TBCOV dataset comprises more than two billion tweets from 218 countries worldwide. The following map shows worldwide tweets normalized by the total population from each country per 100,000 persons.

![Tweets normalized by countries population](figs/worldwide_normalized_tweets.png)

# Data descriptor for base release files
|Attribute|Type|Description|
|--- |--- |--- |
|tweet_id|Int64|The integer representation of the unique identifier a tweet. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it.|
|date_time|String|UTC time when the tweet was created.|
|lang|String|ISO-6391 Alpha-2 language code consisting of two characters.|
|user_id|String|Represents the id of the author of the tweet.|
|retweeted_id|Int64|If the tweet is a retweet, the retweeted_id represents the id of the parent tweet.|
|quoted_id|Int64|If the tweet is a quoted tweet, the quoted_id represents the id of the parent tweet.|
|in_reply_to_id|Int64|If the tweet is a reply to an existing tweet, the in_reply_to_id represents the id of the parent/original tweet.|
|sentiment_label|Int64|Represents the sentiment label values: -1 (negative), 0 (neutral), 1 (positive).|
|sentiment_conf|Float|Represents the confidence score of the sentiment classifier for a given sentiment label to a tweet.|
|user_type|String|The user types represents the identified type of the user such as person, organization, location, etc.|
|gender_label|String|One character code representing the identified gender of the users. F represents "female" and M represents "male" user types.|
|tweet_text_named_entities|Dictionary array|Named-entities (persons, organizations, locations, etc.) extracted from tweet text are provided in this attribute in the array of dictionary format.|
|geo_coordinates_lat_lon|Float|GPS coordinates in the latitude, longitude format retrieved from the user's GPS-enabled device.|
|geo_country_code|String|Two characters country code learned through resolving the GPS coordinates (latitude, longitude).|
|geo_state|String|The name of the state/province learned through resolving the GPS coordinates (latitude, longitude).|
|geo_county|String|The name of the county learned through resolving the GPS coordinates (latitude, longitude).|
|geo_city|String|The name of the city learned through resolving the GPS coordinates (latitude, longitude).|
|place_bounding_box|Float|Twitter provided bounding boxes representing place tags.|
|place_country_code|String|Two characters country code learned through resolving the place bounding boxes.|
|place_state|String|The name of the state/province learned through resolving the place bounding boxes.|
|place_county|String|The name of the county learned through resolving the place bounding boxes.|
|place_city|String|The name of the city learned through resolving the place bounding boxes.|
|user_loc_toponyms|Dictionary array|Toponyms recognized and extracted from the user location field provided as an array of dictionary.|
|user_loc_country_code|String|Two characters country code learned through resolving the user location toponyms.|
|user_loc_state|String|The name of the state/province learned through resolving the user location toponyms.|
|user_loc_county|String|The name of the county learned through resolving the user location toponyms.|
|user_loc_city|String|The name of the city learned through resolving the user location toponyms.|
|user_profile_description_toponyms|Dictionary array|Toponyms recognized and extracted from the user profile description field provided as an array of dictionary.|
|user_profile_description_country_code|String|Two characters country code learned through resolving the recognized user profile description toponyms.|
|user_profile_description_state|String|The name of the state/province learned through resolving the recognized user profile description toponyms.|
|user_profile_description_county|String|The name of the county learned through resolving the recognized user profile description toponyms.|
|user_profile_description_city|String|The name of the city learned through resolving the recognized user profile description toponyms.|
|tweet_text_toponyms|Dictionary array|Toponyms recognized and extracted from the tweet full_text field in the dictionary array format.|
|tweet_text_country_code|String|Two characters country code learned through resolving the recognized tweet text toponyms.|
|tweet_text_state|String|The name of the state/province learned through resolving the recognized tweet text toponyms.|
|tweet_text_county|String|The name of the county learned through resolving the recognized tweet text toponyms.|
|tweet_text_city|String|The name of the city learned through resolving the recognized tweet text toponyms.|

# Tweets hydration
The tweets hydration process fetches full tweet content from Twitter using tweet-ids. To assist users with hydrating TBCOV tweets, this code reposity
provides a tool written in the Java language that takes tweet-ids as input and retrieves full tweet content from Twitter APIs. More details and a usage guide of the Tweets hydrator are available [here](https://github.com/CrisisComputing/TBCOV/tree/main/tweets_hydrator).

# Preprocessing
Different types of preprocessing were applied on different attributes before using them for any analysis. The preprocessing is important to replicate results. The code reposity provides several scripts used to preprocess different fileds. The preprocessing scripts are avaialablel [here](https://github.com/CrisisComputing/TBCOV/tree/main/preprocessing).

# Meta-data file
The meta-data file provides a convenient and faster way to retrieve tweets from the base files. The meta-data file holds the start and the end tweet-id of all base files. So, given a tweet-id file (e.g., a language or a country), the provided script determines which base files to parse to retrieve tweets matching the ids instead of parsing all two billion tweets.

[meta_file_monthly_ids_range.tsv](https://github.com/CrisisComputing/TBCOV/blob/main/meta_data/meta_file_monthly_ids_range.tsv) file lists range of tweet IDs (between Start_id and End_id) contained in the specific monthly base file as follows:
|File_name|Start_id|End_id|
|--- |--- |--- |
|february_2020_f1.tsv|1223395535882768385|1231201257739649025|

# Parsing using meta-file
In the folder [parsers](https://github.com/CrisisComputing/TBCOV/tree/main/parsers), there are two scripts that are needed to extract the tweet details from base release files, given a specific language or country IDs file.

* [meta_file_parser.py](https://github.com/CrisisComputing/TBCOV/blob/main/parsers/meta_file_parser.py) requires two arguments as input.
1. Country/Language IDs file
1. [meta_file_monthly_ids_range.tsv](https://github.com/CrisisComputing/TBCOV/blob/main/meta_data/meta_file_monthly_ids_range.tsv)

Sample to run the script is as follows:
`python meta_file_parser.py [IDs file] meta_data/meta_file_monthly_ids_range.tsv`

And it creates an output file name `required_monthly_files.txt`
The contents of the above file look something like this:
`february_2020_f3.tsv
february_2020_f2.tsv
february_2020_f1.tsv`

Each line indicates which monthly base file is required for download so that it can be used to extract tweet details with the help of the next script.

* [base_file_data_extractor.py](https://github.com/CrisisComputing/TBCOV/blob/main/parsers/base_file_data_extractor.py) requires three arguments as input.
1. `required_monthly_files.txt` which the output of the previous script
1. Country/Language IDs file
1. Base release files path  (expects '/' at the end - for example - /home/downloads/)

Sample to run the script is as follows:
`python base_file_data_extractor.py required_monthly_files.txt test_for_meta_parsing.txt '/some/path'`

The output will be a .tsv file which will have the same formate as montly base files.
