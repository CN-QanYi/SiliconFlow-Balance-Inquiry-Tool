import urllib.request
import json
import sys

# 请将下面的YOUR_API_KEY_HERE替换为您的实际API密钥
api_key = "YOUR_API_KEY_HERE"

url = "https://api.siliconflow.cn/v1/user/info"
headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = response.read().decode()
        result = json.loads(data)
        
        output = []
        output.append("=" * 60)
        output.append("SiliconFlow Balance Query Result")
        output.append("=" * 60)
        
        if result.get("status") == True:
            info = result.get("data", {})
            output.append(f"Account ID: {info.get('id', 'N/A')}")
            output.append(f"Account Name: {info.get('name', 'N/A')}")
            output.append(f"Status: {info.get('status', 'N/A')}")
            output.append("-" * 60)
            output.append(f"Available Balance: {info.get('balance', 'N/A')} CNY")
            output.append(f"Charge Balance: {info.get('chargeBalance', 'N/A')} CNY")
            output.append(f"Total Balance: {info.get('totalBalance', 'N/A')} CNY")
            output.append("=" * 60)
        else:
            output.append(f"Error: {result.get('message', 'Unknown error')}")
            output.append("=" * 60)
        
        output_text = "\n".join(output)
        
        with open("balance_output.txt", "w", encoding="utf-8") as f:
            f.write(output_text)
            
except Exception as e:
    with open("balance_output.txt", "w", encoding="utf-8") as f:
        f.write(f"Error: {type(e).__name__}: {str(e)}\n")
