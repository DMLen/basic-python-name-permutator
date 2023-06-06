import os

# This is a program to quickly generate names from combinations of prefixes and suffixes.
# Useful for DnD, roleplays, creative writing, whatever.
# Prefixes and suffixes should each be in their own file and separated by commas.
# With the supplied prefix inputs "Da, Ma" and the supplied suffixes "vis, ley" the following names would be generated: Davis, Daley, Mavis, Maley

# Written by lambda#9004

prefixes_loaded = 0
suffixes_loaded = 0

# filepath inputs

while prefixes_loaded == 0:
    prefix_file_path = input('\nEnter the file path for the prefixes text file: ')
    if os.path.exists(prefix_file_path):
        print(f"File detected at {prefix_file_path}! Treating this as the prefixes file.")
        prefixes_loaded = 1
    else:
        print(f"File is missing or invalid, please try again.")

while suffixes_loaded == 0:
    suffix_file_path = input('\nEnter the file path for the suffixes text file: ')
    if os.path.exists(suffix_file_path):
        print(f"File detected at {suffix_file_path}! Treating this as the suffixes file.")
        suffixes_loaded = 1
    else:
        print(f"File is missing or invalid, please try again.")

# parsing and formatting

print('Generating names. This may take some time...')

prefixlist = []
suffixlist = []

with open(prefix_file_path, encoding='utf-8-sig') as f:
    for line in f.readlines():
        line = line.strip()
        # string delimiting
        split_line = line.split(', ')
        for word in split_line:
            # removing any commas if it was supplied at end of line
            word = word.replace(',', '')
            prefixlist.append(word)

with open(suffix_file_path, encoding='utf-8-sig') as f:
    for line in f.readlines():
        line = line.strip()
        # string delimiting
        split_line = line.split(', ')
        for word in split_line:
            # removing any commas if it was supplied at end of line
            word = word.replace(',', '')
            suffixlist.append(word)

#debug
print(f"List of parsed prefixes: {prefixlist}")
print(f"List of parsed suffixes: {suffixlist}")

# generating

namelist = []

for word in prefixlist:
    prefix = word
    for word in suffixlist:
        suffix = word
        namelist.append(prefix+suffix)

print(f"Generated namelist: {namelist}\n")

os.system('pause')


