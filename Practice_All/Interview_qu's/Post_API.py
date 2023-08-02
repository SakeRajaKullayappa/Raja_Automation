import requests

req_payload_json = open("Req_Payload", "r").read()

res = requests.post("https://reqres.in/api/users", data=req_payload_json)

print("-----------URL of an API-----------")
URL = res.url
print("URL of an API is :: ", URL)
print()

print("-----------Post Req API Status Code-----------")
status_code = res.status_code
print("status_code return type is :: => ", type(status_code))
print("status_code is :: ", status_code)
assert status_code == 201, "status_code doesn't Matched"
print()

print("--------------Headers---------------")
headers = res.headers
print("header return type is :: => ", type(headers))
for header in headers:
    print("{} -->> key and it value is -->> {}".format(header, headers.get(header)))

Value_CT_key = res.headers.get("Content-Type")
print("Content-Type header key value is :: ", Value_CT_key)
assert Value_CT_key == "application/json; charset=utf-8", "Content-Type doesn't Matched"
print()

print("--------------Cookies---------------")
cookies = res.cookies
print("cookies return type is :: => ", type(cookies))
print(cookies)
print()

print("------------Res Payload-------------")
res_payload_json = res.json()
print("res_payload content json file format is :: ", type(res_payload_json))

