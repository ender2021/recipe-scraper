import zlib
import urllib
import urllib.request

def get_recipe_html(url: str) -> bytearray:
    req = urllib.request.Request(url, headers={
        'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        'Pragma' : 'no-cache',
        'Cache-Control' : 'no-cache',
        'Accept-Language' : 'en-US,en;q=0.6',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
        }) 

    src = bytearray()

    try:
        response = urllib.request.urlopen(req)
        chunk = True
        while chunk:
            chunk = response.read()
            if len(chunk) > 0:
                src.extend(zlib.decompress(chunk, 16+zlib.MAX_WBITS))
        response.close()

    except IOError:
        print("Error retrieving page")
        return bytearray()
    
    return src