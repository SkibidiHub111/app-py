import requests

def handler(request):
    url = "https://raw.githubusercontent.com/SkibidiHub111/Ghoul/refs/heads/main/Ghoul"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            code = r.text
        else:
            code = f"Error loading file: HTTP {r.status_code}"
    except Exception as e:
        code = f"Error: {e}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": code
    }
