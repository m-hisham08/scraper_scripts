import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["POST"]
)

# Create configured session
session = requests.Session()
session.mount('https://', HTTPAdapter(max_retries=retry_strategy))

# Critical headers from curl command
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.6',
    'authorization': 'undefined',
    'content-type': 'application/json',
    'origin': 'https://biz.sosmt.gov',
    'priority': 'u=1, i',
    'referer': 'https://biz.sosmt.gov/search/business',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Brave";v="133.0.0.0", "Chromium";v="133.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Nexus 5"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"6.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
}

# Initial request to establish session cookies
init_response = session.get(
    'https://biz.sosmt.gov/search/business',
    headers={k: v for k, v in headers.items() if k.lower() != 'content-type'}
)

# API request payload
payload = {
    "SEARCH_VALUE": "Microsoft",
    "QUERY_TYPE_ID": 1010,
    "FILING_TYPE_ID": "0",
    "FILING_SUBTYPE_ID": "0",
    "STATUS_ID": "0",
    "STATE": "",
    "COUNTY": "",
    "CRA_SEARCH_YN": False,
    "FILING_DATE": {"start": None, "end": None},
    "EXPIRATION_DATE": {"start": None, "end": None}
}

# Make the search request
try:
    response = session.post(
        'https://biz.sosmt.gov/api/Records/businesssearch',
        json=payload,
        headers=headers,
        timeout=10
    )
    
    # Check for successful response
    if response.status_code == 200:
        print("Success! Retrieved API response")
        results = response.json()
        # Process the JSON data here
        print(f"Found {len(results.get('rows', {}))} results")
        
    elif response.status_code == 403:
        print("Blocked by Cloudflare - consider adding:")
        print("- Rotating proxies")
        print("- Browser-like headers randomization")
        print("- Cloudscraper integration")
        
    else:
        print(f"Unexpected response: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Request failed: {str(e)}")