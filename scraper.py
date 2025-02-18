import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure proxy from environment variables
PROXY_URL = os.environ.get('PROXY_URL')
if not PROXY_URL:
    raise ValueError("No proxy configured. Set PROXY_URL in .env file")

proxies = {
    'http': PROXY_URL,
    'https': PROXY_URL
}

# Corrected headers with proper casing
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.6',
    'Authorization': 'undefined',
    'Content-Type': 'application/json',
    'Origin': 'https://biz.sosmt.gov',
    'Priority': 'u=1, i',
    'Referer': 'https://biz.sosmt.gov/search/business',
    'Sec-Ch-Ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'Sec-Ch-Ua-Arch': '""',
    'Sec-Ch-Ua-Bitness': '"64"',
    'Sec-Ch-Ua-Full-Version-List': '"Not(A:Brand";v="99.0.0.0", "Brave";v="133.0.0.0", "Chromium";v="133.0.0.0"',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Model': '"Nexus 5"',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Sec-Ch-Ua-Platform-Version': '"6.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
}

# Create a new session to maintain cookies
session = requests.Session()

# Initial request to establish session cookies
try:
    init_response = session.get(
        'https://biz.sosmt.gov/search/business',
        # Remove Content-Type header for GET request
        headers={k: v for k, v in headers.items() if k != 'Content-Type'},
        proxies=proxies,
        timeout=10
    )
    init_response.raise_for_status()
except Exception as e:
    print(f"Initial request failed: {str(e)}")
    exit()

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
        proxies=proxies,
        timeout=10
    )
    
    # Check for successful response
    if response.status_code == 200:
        print("Success! Retrieved API response")
        results = response.json()
        print(f"Found {len(results.get('rows', {}))} results")
        
    elif response.status_code == 403:
        print("Blocked by Cloudflare - consider rotating proxies or handling CAPTCHA")
        print(response.text)
        
    else:
        print(f"Unexpected response: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Search request failed: {str(e)}")