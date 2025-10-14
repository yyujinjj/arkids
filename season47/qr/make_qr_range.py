import qrcode
from PIL import Image, ImageDraw, ImageFont

season = 47  
start_session = 6
end_session = 15
base_url = f"https://yyujinjj.github.io/arkids/season{season}/"

font_path = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
font = ImageFont.truetype(font_path, 20)

for i in range(start_session, end_session + 1):
    if i % 10 == 1 and i != 11:
        session = f"{i}st"
    elif i % 10 == 2 and i != 12:
        session = f"{i}nd"
    elif i % 10 == 3 and i != 13:
        session = f"{i}rd"
    else:
        session = f"{i}th"
    
    label = f"매말매기 시즌 {season} - {i}일차"
    
    url = f"{base_url}{session}/"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    
    w, h = img.size
    new_h = h + 40
    new_img = Image.new("RGB", (w, new_h), "white")
    new_img.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(new_img)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    draw.text(((w - text_w) / 2, h + (40 - text_h) / 2),
              label, font=font, fill="black")
    
    filename = f"season{season}_{session}_qr.png"
    new_img.save(filename)
    print(f"QR 코드 저장 완료: {filename} → {url}")
