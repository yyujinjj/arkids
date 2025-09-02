import qrcode

season = 45  

num_sessions = 5

base_url = f"https://yyujinjj.github.io/arkids/season{season}/"

for i in range(1, num_sessions + 1):
    session = f"{i}st" if i == 1 else f"{i}nd" if i == 2 else f"{i}rd" if i == 3 else f"{i}th"
    url = f"{base_url}{session}/"

    img = qrcode.make(url)
    filename = f"season{season}_{session}_qr.png"
    img.save(filename)
    print(f"QR 코드 저장 완료: {filename} → {url}")