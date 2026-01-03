import urllib.request
import json

# 请将下面的YOUR_API_KEY_HERE替换为您的实际API密钥
api_key = "YOUR_API_KEY_HERE"
url = "https://api.siliconflow.cn/v1/user/info"

headers = {"Authorization": "Bearer " + api_key}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        status = response.getcode()
        data = response.read().decode()
        
        with open("balance_result.txt", "w", encoding="utf-8") as f:
            f.write("Status: " + str(status) + "\n")
            f.write("Response:\n")
            f.write(data)
            
            try:
                json_data = json.loads(data)
                f.write("\n\nFormatted:\n")
                f.write(json.dumps(json_data, indent=2, ensure_ascii=False))
            except:
                f.write("\n\nJSON parse failed")
                
except Exception as e:
    with open("balance_result.txt", "w", encoding="utf-8") as f:
        f.write("Error: " + type(e).__name__ + "\n")
        f.write(str(e))
