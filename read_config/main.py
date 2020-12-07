import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

configuration = data['configuration']
folder_to_monitor = configuration['folder_to_monitor']
recursive = configuration['recursive']
print('folder: {}'.format(folder_to_monitor))
print('recursive: {}'.format(recursive))

