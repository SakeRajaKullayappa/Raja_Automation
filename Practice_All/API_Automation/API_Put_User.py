import requests
import json

my_jsonFile = open("Put_User_ReqPayload.json", "r")
jsonData = my_jsonFile.read()

json_obj = json.loads(jsonData)
print("Before Changes :: ", json_obj)

json_obj_data = json_obj['data']
print("No.Of Lists are :: ", len(json_obj_data))
#
# for i in range(0, len(json_obj_data)):
#     # print("id :: ", json_obj_data[i].get("id"))
#     # print("email :: ", json_obj_data[i].get("email"))
#     # print("first_name :: ", json_obj_data[i].get("first_name"))
#     # print("last_name :: ", json_obj_data[i].get("last_name"))
#     # print("avatar :: ", json_obj_data[i].get("avatar"))
#     # print()
#     if i == len(json_obj_data) - 1:
#         print("Before Changes :: ", json_obj_data[i].get("email"))
#
# # need to change few values in Json file without going to file location, we need to do it from here itself
#
# json_obj['data'][5]['email'] = 'raja.sake@reqres.in'
# for i in range(0, len(json_obj_data)):
#     # print("id :: ", json_obj_data[i].get("id"))
#     # print("email :: ", json_obj_data[i].get("email"))
#     # print("first_name :: ", json_obj_data[i].get("first_name"))
#     # print("last_name :: ", json_obj_data[i].get("last_name"))
#     # print("avatar :: ", json_obj_data[i].get("avatar"))
#     # print()
#     if i == len(json_obj_data) - 1:
#         print("After Changes :: ", json_obj_data[i].get("email"))

# for first name

for i in range(0, len(json_obj_data)):
    # print("id :: ", json_obj_data[i].get("id"))
    # print("email :: ", json_obj_data[i].get("email"))
    # print("first_name :: ", json_obj_data[i].get("first_name"))
    # print("last_name :: ", json_obj_data[i].get("last_name"))
    # print("avatar :: ", json_obj_data[i].get("avatar"))

    if i == 0:
        print("Before Changes :: ", json_obj_data[i].get("first_name"))

json_obj_data[0]['first_name'] = "Raja S"

for i in range(0, len(json_obj_data)):
    # print("id :: ", json_obj_data[i].get("id"))
    # print("email :: ", json_obj_data[i].get("email"))
    # print("first_name :: ", json_obj_data[i].get("first_name"))
    # print("last_name :: ", json_obj_data[i].get("last_name"))
    # print("avatar :: ", json_obj_data[i].get("avatar"))

    if i == 0:
        print("After Changes :: ", json_obj_data[i].get("first_name"))


