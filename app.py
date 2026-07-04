from flask import Flask, request, jsonify
import requests
from urllib.parse import urlparse


app = Flask(__name__)

# -----------------------------
#  credits : https://great.thug4ff.com/
# -----------------------------


def _get_openid_headers(base_url):
    host = urlparse(base_url).netloc
    return {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": (
            '_ga': 'GA1.1.2123120599.1674510784',
            '_fbp': 'fb.1.1674510785537.363500115',
            '_ga_7JZFJ14B0B': 'GS1.1.1674510784.1.1.1674510789.0.0.0',
            'source': 'mb',
            'region': 'MA',
            'language': 'ar',
            '_ga_TVZ1LG7BEB': 'GS1.1.1674930050.3.1.1674930171.0.0.0',
            'datadome': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
            'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y'
        )
        "Host": host,
        "Origin": base_url,
        "Referer": base_url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'",
        "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        'x-datadome-clientid': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0'
    }


def get_openid_data(account_id):
    payload = {
        "app_id": 100067,
        "login_id": str(account_id)
    }

    base_url = "https://shop2game.com"
    url = f"{base_url}/api/auth/player_id_login"
    headers = _get_openid_headers(base_url)

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        data = response.json()
        print(data)
        open_id = data.get("open_id")
        if open_id:
            return {
                "nickname": data.get("nickname"),
                "region": data.get("region"),
                "account_id": account_id,
                "open_id": open_id,
            }
        else:
            return data

    except Exception as e:
        print("Error:", e)

    return {"error": "Failed to get nickname and open_id"}


@app.route("/region", methods=["GET"])
def api_openid():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({"error": "Missing 'uid' parameter"}), 400

    result = get_openid_data(uid)
    if not result.get("open_id"):
        return jsonify(result), 404
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




# Demo : http://127.0.0.1:5000/username?uid=305000592
