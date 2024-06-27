# utils/quicknode.py

import requests
import json

def get_fee_estimate(quicknode_url):
    headers = {
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getFees",
        "params": []
    })

    response = requests.post(quicknode_url, headers=headers, data=payload)
    if response.status_code == 200:
        result = response.json().get('result', {})
        if result:
            fee_estimate = result.get('value', {}).get('feeCalculator', {}).get('lamportsPerSignature', 0)
            return fee_estimate
        else:
            print("No fee information found")
            return 0
    else:
        print("Failed to fetch fee information")
        return 0
