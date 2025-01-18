import requests

# Endpoint URL
url = 'https://enterpriseapi.cathoven.com/cefr/process_text'
url_difficulty = 'https://enterpriseapi.cathoven.com/catile/difficulty'

# Your credentials
client_id = '41b95a1e-89cf-4194-ad44-da6a542da143'
client_secret = '313f758a-a846-4e25-8656-b80e012f7216'

# Text to analyze
text = ('Hi everyone, welcome back to the channel! Today, we’re going to talk '
        'about how to take care of houseplants. Houseplants are a great way '
        'to bring life and color into your home, but they do need proper care '
        'to thrive. First, let’s talk about watering. Most houseplants only '
        'need water when the top inch of soil feels dry. Overwatering is a '
        'common mistake, so always check the soil before adding more water. '
        'Next, let’s discuss sunlight. Some plants need bright, indirect '
        'light, while others can survive in low-light conditions. Be sure to '
        'research what kind of light your plant prefers and place it in the '
        'right spot. Finally, remember to clean the leaves occasionally. Dust '
        'can block sunlight and slow down growth. That’s it for today’s tips! '
        'Thanks for watching, and don’t forget to subscribe for more plant '
        'care advice. See you next time!')

# process_text endpoint...

# Request payload
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'text': text,
    'title': 'Optional Title',
    'v': 2,  # Version of the CEFR Analyser
    'propn_as_lowest': True,
    'intj_as_lowest': True,
    'keep_min': True,
    'custom_dictionary': {},  # Add custom vocabulary levels if needed
    'return_final_levels': True,
    "outputs": [
        "sentences",
        "wordlists",
        "vocabulary_stats",
        "tense_count",
        "tense_term_count",
        "tense_stats",
        "clause_count",
        "clause_stats",
        "final_levels"
    ]
}

# Make the request
response = requests.post(url, data=payload)

# Check the response
if response.status_code == 200:
    analysis_result = response.json()
    print(analysis_result)
else:
    print(f'Error: {response.status_code}')


# difficulty endpoint...

payload_difficulty = {
    'client_id': client_id,
    'client_secret': client_secret,
    'text': text
}

# Make the request
response = requests.post(url_difficulty, data=payload)

# Check the response
if response.status_code == 200:
    analysis_result = response.json()
    print(analysis_result)
else:
    print(f'Error: {response.status_code}')
