txt = '你好 PyHub!'

# 读取原始JPEG图像数据
with open("input.jpg", "rb") as f:
    f_bytes = f.read()
    print(f_bytes[:2])
    print(f_bytes[-2:])

# 编码
with open("input.jpg", "rb") as f:
    with open("output.jpg", "wb") as output:
        output.write(f.read())
        output.write('你好 PyHub!'.encode())

# 解码
with open("output.jpg", "rb") as f:
    content = f.read()
    eoi = content.find(b'\xff\xd9')
    print(content[eoi+2:].decode())
