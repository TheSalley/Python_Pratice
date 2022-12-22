try:
    f1 = open('03.apple.jpg', 'rb')
    data = f1.read()
    print(type(data))  # <class 'bytes'>
    f2 = open('03.apple_copy.jpg', 'wb')
    f1.seek(0)
    f2.write(f1.read())
except FileNotFoundError:
    print('指定的文件无法打开')
