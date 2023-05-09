# This is a practice file that contains codes from Coursera.

# Part 1: Json
import json

# list containing dictionary of people
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

# Serialize the people object into a JSON file called people.json
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# Serializes Python objects, but returns a string instead of writing directly to a file.
people_json = json.dumps(people)
print(people_json)

# The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects.
# The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.
with open('people.json', 'r') as people_json:
    people = json.load(people_json)
print(people)

# In json,
# objects are key-value pair structures like Python dictionaries,
# arrays, are like Python lists.
# JSON elements are always comma-delimited
# The json library will help us turn Python objects into JSON, and turn JSON strings into Python objects.
# JSON elements can only represent simple data types:
# dict, list, tuple, str, int, float, int- & float-derived Enums, True, False, None


# part 2 Python Requests
import requests
response = requests.get('https://www.google.com')
# first 300 characters of the Response.text
print(response.text[:300])

# In python Requests, the response and was decompressed decoded to form html
response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])
# Requests module told the web server that it was okay to compress the content
print(response.request.headers['Accept-Encoding'])
# Server told us that the content had actually been compressed.
print(response.headers['Content-Encoding'])

# If python request is successful
print(response.ok)
# Get the response status code
print(response.status_code)

# Get the response and raise an HTTPError exception only if the response wasn’t successful
response.raise_for_status()

# HTTP GET: retrieves or gets the resource specified in the URL
# GET request can have parameters
p = {"q": "grey kitten", "num": 15}
response = requests.get("https://www.google.com/search", params=p)
print(response.request.url)

# HTTP POST: Fill a web form and press a button to submit, using POST method to send data back to the web server
p = {"description": "white kitten", "name": "Snowball","age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
# Generated URL
print(response.request.url)
# Parameters are in the body of the HTTP message
print(response.request.body)
# Turn our data into dictionaries and then pass that as the data attribute of a POST request. The Json parameter will
# auto convert the data into json format
response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.url)
print(response.request.body)
