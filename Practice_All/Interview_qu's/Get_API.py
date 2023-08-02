import requests

response = requests.get("https://reqres.in/api/users?page=2")

URL = response.url
print(URL)
assert URL == "https://reqres.in/api/users?page=2", "URL is not Matched"

status_code = response.status_code
print(type(status_code))
print(status_code)
assert status_code == 200, "status_code is not Matched"

list_headers = response.headers
print(type(list_headers))
print(len(list_headers))
print()

print(list_headers)
print()

for header in list_headers:
    print("{} -->> key and it's value is -->> {}".format(header, list_headers.get(header)))

assert list_headers.get("Content-Type") == "application/json; charset=utf-8", "Content-Type key header value is not " \
                                                                              "matched"
assert list_headers.get("Connection") == "keep-alive", "Connection key header value is not matched"
assert list_headers.get("CF-Cache-Status") == "HIT", "CF-Cache-Status key header value is not matched"

res_payload = response.json()
print(res_payload)

page = res_payload['page']
assert page == 2, "page field value is not Matched"

per_page = res_payload['per_page']
assert per_page == 6, "per_page field value is not Matched"

support = res_payload['support']
print(type(support))
for key,  value in support.items():
    print(key, ":", value)

assert support.get("url") == "https://reqres.in/#support-heading", "support dict url key value is not Matched"

data = res_payload['data']
print(type(data))
print(len(data))
print(data[len(data) - 1])

email = res_payload['data'][5]['email']
assert email.endswith("reqres.in"), "email is not ends with reqres.in"










