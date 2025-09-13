import requests

URL = "https://stockpicker-crew.streamlit.app/"

try:
    resp = requests.get(URL, timeout=10)
    print(f"Pinged {URL}, status: {resp.status_code}")
except Exception as e:
    print("Error:", e)
