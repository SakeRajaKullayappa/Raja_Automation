import requests

p = {'page': 2}
URL = "https://reqres.in/api/users"

res_payload = requests.get(url=URL, params=p)

print("Type of res_payload is :: ", type(res_payload))

current_URL = res_payload.url
print("current_URL of Get Method is :: ", current_URL)

status_code = res_payload.status_code
print("status_code for Get Method is :: ", status_code)
assert status_code == 200, "status_code is not matching"

encoding = res_payload.encoding
print("encoding is :: ", encoding)
assert encoding == "utf-8", "encoding does not matching"

headers = res_payload.headers
print("No.Of Headers are :: ", len(headers))
print("Headers are :: ", headers)

for header in headers:
    print(header)
    if header == "Content-Encoding":
        print("act and exp header is matched :: ", header)

cookies = res_payload.cookies
print("No.Of Cookies are :: ", len(cookies))

res_payload_content = res_payload.json()
print("res payload content is :: ", res_payload_content)
print("type of res payload content is :: ", type(res_payload_content))

pages = res_payload_content["page"]
print(pages)
assert pages == 2, "pages count is not matching"

per_page = res_payload_content["per_page"]
print(per_page)
assert per_page == 6, "per_pages count is not matching"

total = res_payload_content["total"]
print(total)
assert total == 12, "total count is not matching"

total_pages = res_payload_content["total_pages"]
print(total_pages)
assert total_pages == 2, "total_pages count is not matching"

json_obj_data = res_payload_content['data']
print(len(json_obj_data))

for i in range(0, len(json_obj_data)):
    print("id :: ", json_obj_data[i].get('id'))
    print("email :: ", json_obj_data[i].get('email'))
    print("first_name :: ", json_obj_data[i].get('first_name'))
    print("last_name :: ", json_obj_data[i].get('last_name'))
    print("avatar :: ", json_obj_data[i].get('avatar'))
    print()

data_id = res_payload_content["data"][0]["id"]
print("", data_id)
assert data_id == 7, "total count is not matching"

data_email = res_payload_content["data"][4]["email"]
print("", data_email)
assert data_email.endswith("reqres.in"), "data_email is not ending with reqres.in"



