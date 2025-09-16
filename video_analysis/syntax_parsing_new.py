import requests, json
text = "Come join us for our back-to-campus event to connect with other HSM members and learn more about what we do!"
r = requests.post(
    "http://localhost:9000/",
    params={'annotators': 'parse', 'outputFormat': 'json'},
    data=text.encode('utf-8')
)
tree = r.json()['sentences'][0]['parse']
print(tree)