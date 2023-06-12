import base64

# 读取WAV文件并转换为Base64字符串
with open("CantinaBand3.wav", "rb") as wav_file:
    wav_data = wav_file.read()
    base64_data = base64.b64encode(wav_data).decode()

# 读取原始JPEG图像数据
with open("input.jpg", "rb") as f:
    f_bytes = f.read()
    print(f_bytes[:2])
    print(f_bytes[-2:])

# 编码
with open("input.jpg", "rb") as f:
    with open("output.jpg", "wb") as output:
        output.write(f.read())
        output.write(base64_data.encode())

# 解码
with open("output.jpg", "rb") as f:
    content = f.read()
    eoi = content.find(b'\xff\xd9')
    base64_str = content[eoi+2:].decode()
    wav_data = base64.b64decode(base64_str)

# 将Base64字符串转换为WAV文件
with open("output.wav", "wb") as wav_file:
    wav_file.write(wav_data)
