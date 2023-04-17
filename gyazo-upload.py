#!/data/data/com.termux/files/usr/bin/python3
import sys
import base64
import requests
import os
from io import BytesIO
import subprocess

# Gyazo APIキーを入力
API_KEY = 'YOUR_API_KEY'
UPLOAD_URL = 'https://upload.gyazo.com/api/upload'

def main():
    file_path = sys.argv[1]

    # 画像を開く
    with open(file_path, 'rb') as f:
        im_data = f.read()

    # 画像をアップロード
    response = requests.post(
        UPLOAD_URL,
        headers={'Authorization': 'Bearer ' + API_KEY},
        files={'imagedata': im_data}
    )
    response.raise_for_status()

    # URLをクリップボードにコピー（アップロード後の拡張子付き）
    url = response.json()['url']
    print('Image URL with extension:', url)
    termux_set_clipboard(url)

def termux_set_clipboard(text):
    subprocess.run(['termux-clipboard-set', text], check=True)

if __name__ == '__main__':
    main()