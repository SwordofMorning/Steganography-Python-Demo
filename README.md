# Steganography Python Demo

本项目通过在jpeg图像的EOI标识符之后隐写字符串来实现图片+文件的组合方式，目的是为了实现图片加语音注释的功能。

对于二进制文件（wav），则需要通过base64转换之后再写入（避免EOI标志`FFD9`冲突）。