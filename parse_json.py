from requests import *
import json
# with open('states.json') as f:
#     data = json.load(f)
#     print(data['states'])
# for person in data['states']:
#     del(person['area_codes'])
# new_data = json.dumps(data, indent=2, sort_keys=True)
# with open ("new_states.json", 'w') as w:
#     json.dump(data, w, indent=2)
resp=get('http://api.open-notify.org/astros.json')
print("status_code=",resp.status_code)
# print("output response=",resp)
#we use dumps to convert python dict to json object
data=resp.json()
data= json.dumps(data, indent=1)
print(type(data))
json_data=json.loads(data)
print(type(json_data))

#dump the json into a file
with open ("files.json", 'w') as w:
    json.dump(json_data, w, indent=1)

if json_data['message'].lower()=='success':
    print('the api is successful')
else:
    print("fuck you")
#here we are going to print the people in the given string
len_people=len(json_data['people'])
print(len_people)
if len_people==json_data['number']:
    print("accurate")
else:
    print("not works accurate")
people_name=[]
for i in range(0,len_people):
    people_name.insert(0,json_data['people'][i]['name'])
print("names are ",people_name,"and the length is ",len(people_name))




