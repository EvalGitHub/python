import hashlib
def get_md5(url):
    # py3中都是unicode ,但是上面这个函数不接受，因此需要进行转码
    if isinstance(url,str):
        url =url.encode("utf-8")

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ =='__main__':
    print(get_md5("hht://jobbole.com"))