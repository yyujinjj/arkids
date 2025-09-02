import qrcode

url = "https://yyujinjj.github.io/arkids/season45/1st/"

img = qrcode.make(url)

img.save("season45_1st_qr.png")

print("QR 코드 저장 완료: season45_1st_qr.png")