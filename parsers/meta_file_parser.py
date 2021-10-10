import sys
from tqdm import tqdm

#Sample output run
#python meta_file_parser.py test_for_meta_parsing.txt meta_data/meta_file_monthly_ids_range.tsv


#Pass the country/lang file that you want to extract
opened_file = open(sys.argv[1])

#Pass the meta-file as provided in the repo
meta_file_opened = open(sys.argv[2])

meta_file_dict = {}

output_file = open(str(sys.argv[1].split('.')[0]) + "_required_monthly_files.txt", "w+")


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


#start from the second line
next(meta_file_opened)

#Loading the meta-file in a dictionary
for meta_line in meta_file_opened:

	meta_array = meta_line.strip().split('\t')

	#print(meta_array)
	
	insert_in_dict(meta_file_dict, meta_array[0], [int(meta_array[1]), int(meta_array[2])])

meta_file_opened.close()

print("\n")
print("File 'required_monthly_files.txt' is being generated, please wait...")
print("\n")

#Which files need to be used
files_to_be_downloaded = set()

num_lines = sum(1 for line in open(sys.argv[1],'r'))

# num_lines = sum(1 for line in opened_file)
#To check which files are needed to be downloaded, run this part.
# with Bar('Processing...') as bar:
# for i in tqdm(range(100)):
for line in tqdm(opened_file, total=num_lines):

	tweet_id = int(line.strip())

	for key in meta_file_dict:
		start_id = meta_file_dict[key][0]
		end_id = meta_file_dict[key][1]

		if(tweet_id >= start_id and tweet_id <= end_id):
			#files_to_be_downloaded.add(key.split('_')[0].capitalize()  + " "+ key.split('_')[1])
			files_to_be_downloaded.add(key)
		# bar.next()

#list of all files
list_files = []

#output file names and then take input from reader
for value in files_to_be_downloaded:
	list_files.append(value)

list_files.sort()

for i in range(0, len(list_files)):
	#output in a text file
	output_file.write(list_files[i] + '\n')

opened_file.close()
output_file.close()




