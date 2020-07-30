import requests


# get method
response = requests.get("https://foofish.net")
print(response.status_code)

print(response.reason)

for name, value in response.headers.items():
    print("%s:%s" % (name, value))

print(response.content)
