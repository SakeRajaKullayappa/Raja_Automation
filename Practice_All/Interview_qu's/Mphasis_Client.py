import requests
auth = requests.post("url")
res = requests.post("url", auth)

status_code = res.status_code
print(type(status_code))
assert status_code == 201, "not Matched"

list_headers = res.headers
print(len(list_headers))

for header in list_headers:
    print("{} and its value {}".format(header, list_headers.get(header)))

assert list_headers.get("header key ") == "header value", "not Matched"

encoding = res.encoding
print(type(encoding))

cookies = res.cookies
print(cookies)

res_payload = res.json()
page = res_payload['page']
assert page == 2, "not Matched"

email = res_payload['data'][5]['email']
assert email.endswith("reqres.in"), "not Matched"

id_2 = res_payload['data'][2]['id']
assert id_2 == 9, "not Matched"
