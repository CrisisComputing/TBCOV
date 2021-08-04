import sys

#Sample output run
#python base_file_data_extractor.py required_monthly_files.txt test_for_meta_parsing.txt '/some/path'


#Pass the output of the previous script to this script
meta_parser_output = open(sys.argv[1])



#Pass the IDs file through which you want to extract all the tweets/full details
ids_file = open(sys.argv[2])

#base release files path #expects '/' at the end
base_release_file_path = sys.argv[3]

#output_file
output_file = open(sys.argv[2].replace('.txt', '') + "_detailed.tsv", "w+")


#This function is for inserting a value in a dictionary
def insert_in_dict(dictionary, key, value):
    #check key
    # key
    # value
    if key in dictionary:
        dictionary[key] = value
    else:
        if key != None:
            dictionary[key] = value

    return dictionary


ids_dict = {}

for line in ids_file:
	insert_in_dict(ids_dict, line.strip(), True)

ids_file.close()

output_file.write("tweet_id	date_time	lang	user_id	retweeted_id	quoted_id	in_reply_to_id	sentiment_conf	sentiment_label	user_type	gender_label	tweet_text_named_entities	geo_coordinates_lat_lon	geo_country_code	geo_state	geo_county	geo_city	place_bounding_box	place_country_code	place_state	place_county	place_city	user_loc_toponym	user_loc_country_code	user_loc_state	user_loc_county	user_loc_city	User_profile_description_toponyms	user_profile_description_country_code	user_profile_description_state	user_profile_description_county	user_profile_description_city	tweet_text_toponyms	tweet_text_country_code	tweet_text_state	tweet_text_county	tweet_text_city")
output_file.write('\n')


#Extract the required full items
for key in meta_parser_output:

	file_to_be_read = open(base_release_file_path + key.strip())

	for full_info_line in file_to_be_read:

		data = full_info_line.split('\t')

		if(ids_dict.get(data[0]) != None):
			output_file.write(full_info_line)

output_file.close()

meta_parser_output.close()

