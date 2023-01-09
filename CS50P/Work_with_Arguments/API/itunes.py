import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

# here we just avoid to hardcode the word of the band 'weezer' in the end, which instead we pass in the file argument:
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

# version 1 - by returning the whole dump print statement of the data for the band 'weezer':
# print(json.dumps(response.json(), indent=2))

# version 2 - returns a dictionary with the data of 50 songs (because limit is set to 50 in the above GET request):
data = response.json()

for result in data["results"]:
    print(result["trackName"])
