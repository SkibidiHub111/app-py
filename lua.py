import requests

def handler(request):
    
    url = "https://raw.githubusercontent.com/SkibidiHub111/Ghoul/refs/heads/main/Ghoul"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            lua_code = response.text
        else:
            lua_code = f"Error: Không thể tải file Lua (status {response.status_code})"
    except Exception as e:
        lua_code = f"Error: {str(e)}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": lua_code
    }
