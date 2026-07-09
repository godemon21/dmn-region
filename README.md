# OpenID Username  API

A simple Flask-based API that fetches a Free Fire player's **nickname**, **region**, and **open_id** using their **UID**.

---

##  Usage

## Endpoint
GET /username?uid=PLAYER_UID

## Example
http://127.0.0.1:5000/username?uid=305000592



## Response
  ```sh
  
    "account_id": "305000592",
    "nickname": "ᴀᴋᴜᴍᴀ¿?",
    "open_id": "3c77e6056a49d2efa54b5dbdd6a8e7ca",
    "region": "ME"
   ```

## 📦 Installation
   ```sh
   git clone https://github.com/paulafredo/OpenID-Username-API
   cd OpenID-Username-API
   pip install requirements.txt
   python app.py
   ```

## ⚠️ Important: Cookie Required

This API uses a Shop2Game cookie.
If the API stops working or returns errors, you must generate a NEW cookie and replace it in the code.
Without a valid cookie → the API cannot retrieve any data.

## ❗ Disclaimer

This project is intended for educational purposes only.

## Credits
is it needs??



