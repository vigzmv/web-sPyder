# Lets Crawl! <vigzmv/>

import os

# New Dir for New Project

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Starting Project' + directory)
        os.makedirs(directory)


#create_project_dir('New_Project')


# create 'em files

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# appending data

def append_to_file(path,data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# cleaning it up

def delete_file_contents(path):
    with open(path, 'w'):
        pass


# set builder

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return  results


# iterator

def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
        








