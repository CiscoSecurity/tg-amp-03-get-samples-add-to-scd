import requests

# Threat Grid API Key
tg_api_key = 'asdf1234asdf1234asdf1234'

# AMP for Endpoint API Credentials
amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'
amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# Simple custom detection GUID that SHA256s will be added to
scd_guid = 'asdf1234-asdf-1234-asdf-12344asdf123'

# Instatiate a session to be used for the AMP for Endpoints API
amp_session = requests.session()
amp_session.auth = (amp_client_id, amp_api_key)

# Threat Grid URL used for collecting samples
tg_url = 'https://panacea.threatgrid.com/api/v2/search/submissions'

# Parameters for Threat Grid API query
tg_parameters = {'api_key': tg_api_key,
                 'advanced':'true',
                 'state':'succ',
                 'q':'analysis.threat_score:>=95'}

# Query Threat Grid for samples
request = requests.get(tg_url, params=tg_parameters)

# Decode the JSON response
json_response = request.json()

# Name the 'items' list in the JSON response
items = json_response['data']['items']

# Iterate over the items list
for sample in items:
    # Name the SHA256 for the sample
    sha256 = sample['item']['sha256']

    # Print the SHA256 about to be added to the Simple Custom Detectoin list
    print(sha256, end=' '),

    # Format the URL to add the SHA256 to the Simple Custom Detectoin list
    add_sha256_url = 'https://api.amp.cisco.com/v1/file_lists/{}/files/{}'.format(scd_guid, sha256)

    # Add the SHA256 to the Simple Custom Detection
    amp_request = amp_session.post(add_sha256_url)

    # Check the returned status code and print if it was sucessful or failed
    if amp_request.status_code == 201:
        print('- Successfully added to SCD')
    else:
        print('- Something went wrong!')