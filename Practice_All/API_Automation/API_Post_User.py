import requests
import json

my_jsonFile = open("Post_User_ReqPayload.json", "r")
jsonData = my_jsonFile.read()

json_obj = json.loads(jsonData)
print(json_obj)
print(json_obj['page'])
assert json_obj['page'] == 2, "page count Not Matching"

print(json_obj['per_page'])
assert json_obj['per_page'] == 6, "per_page count Not Matching"

print(json_obj['total'])
assert json_obj['total'] == 12, "total count Not Matching"

print(json_obj['total_pages'])
assert json_obj['total_pages'] == 2, "total_pages count Not Matching"

data_lst = json_obj['data']
print(data_lst)
print("data count is :: ", len(data_lst))

for i in range(0, len(data_lst)):
    print("id ::", data_lst[i].get("id"))
    print("email ::", data_lst[i].get("email"))
    print("first_name ::", data_lst[i].get("first_name"))
    print("last_name ::", data_lst[i].get("last_name"))
    print("avatar ::", data_lst[i].get("avatar"))
    print()

URL = "https://reqres.in/api/users"

res_payload = requests.post(url=URL )