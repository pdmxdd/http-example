import requests

print("-" * 60)
print("")

"""
Example of HTTP Request: http://localhost:7777/
Method: GET
URI protocol: http
URI domain: localhost
URI path: /
"""
index_get_response = requests.get("http://localhost:7777/")

"""
HTTP Response
"""
# Status Code
print(f'HTTP RESPONSE STATUS CODE: {index_get_response}')

# Headers
print(f'HTTP RESPONSE HEADERS: {index_get_response.headers}')

# Body
print(f'HTTP RESPONSE BODY: {index_get_response.text}')
print("-" * 60)
print("")

"""
Example of HTTP Request: http://localhost:7777/json
Method: GET
URI protocol: http
URI domain: localhost
URI path: /json
"""
json_get_response = requests.get("http://localhost:7777/json")

"""
HTTP Response
"""
# Status Code
print(f'HTTP RESPONSE STATUS CODE: {json_get_response}')

# Headers
print(f'HTTP RESPONSE HEADERS: {json_get_response.headers}')

# Body
print(f'HTTP RESPONSE BODY: {json_get_response.text}')
print("-" * 60)
print("")

"""
Example of HTTP Request: http://localhost:7777/json
Method: POST
URI protocol: http
URI domain: localhost
URI path: /json
"""
json_post_response = requests.post("http://localhost:7777/json", json={
    "title": "POST JSON",
    "body": "I changed the JSON via a HTTP POST request"
})

"""
HTTP Response
"""
# Status Code
print(f'HTTP RESPONSE STATUS CODE: {json_post_response}')

# Headers
print(f'HTTP RESPONSE HEADERS: {json_post_response.headers}')

# Body
print(f'HTTP RESPONSE BODY: {json_post_response.text}')
print("")
print("-" * 60)
