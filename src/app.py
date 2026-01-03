from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import urllib.request
import json
import os

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

@app.route('/')
def index():
    """返回主页面"""
    return send_from_directory('.', 'index.html')

@app.route('/api/balance', methods=['POST'])
def get_balance():
    """查询余额的API端点"""
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        
        if not api_key:
            return jsonify({
                'success': False,
                'error': 'API密钥不能为空'
            }), 400
        
        # 调用SiliconFlow API
        url = "https://api.siliconflow.cn/v1/user/info"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                response_data = response.read().decode('utf-8')
                result = json.loads(response_data)
                
                if result.get("status") == True:
                    info = result.get("data", {})
                    return jsonify({
                        'success': True,
                        'data': {
                            'id': info.get('id', 'N/A'),
                            'name': info.get('name', 'N/A'),
                            'email': info.get('email', 'N/A'),
                            'status': info.get('status', 'N/A'),
                            'balance': info.get('balance', 'N/A'),
                            'chargeBalance': info.get('chargeBalance', 'N/A'),
                            'totalBalance': info.get('totalBalance', 'N/A')
                        }
                    })
                else:
                    return jsonify({
                        'success': False,
                        'error': result.get('message', '未知错误')
                    }), 400
                    
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8', errors='ignore')
            return jsonify({
                'success': False,
                'error': f'HTTP错误 {e.code}: {error_body}'
            }), 400
        except urllib.error.URLError as e:
            return jsonify({
                'success': False,
                'error': f'网络连接错误: {str(e.reason)}'
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器错误: {str(e)}'
        }), 500

@app.route('/health')
def health():
    """健康检查端点"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("=" * 60)
    print("SiliconFlow 余额查询工具 - 网页版")
    print("=" * 60)
    print("服务器启动中...")
    print("请在浏览器中访问: http://localhost:5000")
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)
