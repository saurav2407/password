import pyqrcode
s = 'https://www.instagram.com/pathak_jii2407/'
url = pyqrcode.create(s)
url.svg("instagram_account", scale = 8)