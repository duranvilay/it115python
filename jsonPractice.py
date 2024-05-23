#Import file
import json

data = {
    'name': 'Darius Miles',
    'age': 27,
    'city': 'Portland, OR'
    'interests': ['Basketball'],
    'is_student': False
}

with open ('data.json','w') as json_files:

    json.dump(data,json_file,indent=4)

print("Data has been written to data2.json")



with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)


print("Successfully able to read data.json")
print(loaded_data)

loaded_data['age'] = 27