#!/usr/bin/env python
import requests
from . import define
from os import path

# Latest app version can be found using GET /v1/application-info/android
USER_AGENT = "PixivAndroidApp/5.0.155 (Android 6.0; Pixel C)"
AUTH_TOKEN_URL = "https://oauth.secure.pixiv.net/auth/token"
CLIENT_ID = "MOBrBDS8blbauoSck0ZfDbtuzpyT"
CLIENT_SECRET = "lsACyCD94FhDUtGTXi3QzcFE2uU1hqtDaKeqrdwj"


def refresh(hosts, refresh_token):
    response = requests.post(
        '%s/auth/token' % hosts,
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "refresh_token",
            "include_policy": "true",
            "refresh_token": refresh_token,
        },
        headers={
            "User-Agent": USER_AGENT,
            "host": 'oauth.secure.pixiv.net',
        },
        verify=False,
    )
    data = response.json()
    refresh_token = data["refresh_token"]
    with open(path.join(define.PATHDIR, "token"), 'w') as f:
        f.write(refresh_token)
    return refresh_token
