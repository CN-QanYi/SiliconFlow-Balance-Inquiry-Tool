import urllib.request
import json

# 请将下面的YOUR_API_KEY_HERE替换为您的实际API密钥
api_key = "YOUR_API_KEY_HERE"

url = "https://api.siliconflow.cn/v1/user/info"
headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req, timeout=10) as response:
    data = response.read().decode()
    result = json.loads(data)
    
    print("\n" + "=" * 60)
    print("SiliconFlow Balance Query Result")
    print("=" * 60)
    
    if result.get("status") == True:
        info = result.get("data", {})
        print(f"Account ID: {info.get('id', 'N/A')}")
        print(f"Account Name: {info.get('name', 'N/A')}")
        print(f"Status: {info.get('status', 'N/A')}")
        print("-" * 60)
        print(f"Available Balance: {info.get('balance', 'N/A')} CNY")
        print(f"Charge Balance: {info.get('chargeBalance', 'N/A')} CNY")
        print(f"Total Balance: {info.get('totalBalance', 'N/A')} CNY")
        print("=" * 60)
    else:
        print(f"Error: {result.get('message', 'Unknown error')}")
        print("=" * 60)
