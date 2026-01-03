#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import argparse

def get_siliconflow_balance(api_key):
    """
    查询硅基流动账户余额

    Args:
        api_key: 硅基流动API密钥

    Returns:
        dict: 包含余额信息的字典，失败时返回None
    """
    import urllib.request
    import urllib.error
    
    url = "https://api.siliconflow.cn/v1/user/info"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        print(f"正在查询API端点: {url}")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            print(f"HTTP状态码: {response.status}")
            data = response.read().decode("utf-8")
            print(f"响应内容: {data}")
            
            import json
            result = json.loads(data)
            print(f"解析的JSON数据: {json.dumps(result, indent=2, ensure_ascii=False)}")
            
            if result.get("status") == True:
                return result.get("data", {})
            else:
                print(f"API返回错误: {result.get('message', '未知错误')}")
                return None

    except urllib.error.URLError as e:
        print(f"网络请求错误: {e}")
        return None
    except Exception as e:
        print(f"请求异常: {e}")
        return None

def display_balance_info(balance_info):
    """格式化显示余额信息"""
    if not balance_info:
        return

    print("\n" + "=" * 50)
    print("硅基流动账户信息")
    print("=" * 50)

    if "name" in balance_info:
        print(f"账户名称: {balance_info['name']}")

    if "email" in balance_info and balance_info['email']:
        print(f"邮箱: {balance_info['email']}")

    print("-" * 50)

    if "balance" in balance_info:
        print(f"可用余额: {balance_info['balance']} 元")

    if "chargeBalance" in balance_info:
        print(f"充值余额: {balance_info['chargeBalance']} 元")

    if "totalBalance" in balance_info:
        print(f"总余额: {balance_info['totalBalance']} 元")

    print("=" * 50 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="查询硅基流动账户余额",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python check_siliconflow_balance.py -k YOUR_API_KEY
  python check_siliconflow_balance.py --api-key YOUR_API_KEY
        """
    )
    parser.add_argument("-k", "--api-key", 
                        type=str, 
                        help="硅基流动API密钥")
    parser.add_argument("-i", "--interactive",
                        action="store_true",
                        help="交互式输入API密钥")

    args = parser.parse_args()

    if args.interactive or not args.api_key:
        print("硅基流动余额查询工具")
        print("请输入您的API密钥（将显示为明文）")

        api_key = input("API密钥: ").strip()

        if not api_key:
            print("错误: API密钥不能为空")
            sys.exit(1)

        if len(api_key) < 10:
            print("警告: API密钥长度过短，请确认是否输入正确")
    else:
        api_key = args.api_key
        if len(api_key) < 10:
            print("警告: API密钥长度过短，请确认是否输入正确")

    balance_info = get_siliconflow_balance(api_key)

    if balance_info:
        display_balance_info(balance_info)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
