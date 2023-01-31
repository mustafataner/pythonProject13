# basit bir atm uygulaması

print("""\t***Merhabalar Taner bank'a hoş geldiniz.***
\t\t lütfen kartınızı takınız...""")

veritabanı = {"rumethesap": {

    "isim": "rumet",
    "soyisim": "taner",
    "kartsifresi": "1234",
    "hesapbakiye": "50000",
    "kredikartborc": "4200",
    "kredkartborctarih": "31.01.2023"},

    "mustafahesap": {
        "isim": "mustafa",
        "soyisim": "taner",
        "kartsifresi": "4321",
        "hesapbakiye": "20000",
        "kredikartborc": "1200",
        "kredkartborctarih": "25.02.2023"}}

takilanKart = dict(veritabanı["rumethesap"])

hak = 2

for i in range(0, 3):

    sifre = input("lütfen 4 haneli şifrenizi giriniz: ")

    if sifre == takilanKart.get("kartsifresi"):

        print("""merhaba hoş geldiniz {} {} 
        lütfen yapmak istediğiniz işlemi seçin...""".format(takilanKart.get("isim"), takilanKart.get("soyisim")))

        sec = input('''

        [1] bakiye sorgulama
        [2] kredi kartı borcu sorgulama
        [3] para çekme
        [4] para yatırma
        [5] kart iade\n''')

        break

    elif sifre != takilanKart.get("kartsifresi") and hak != 0:
        print("hatalı şifre girdiniz! kalan hakkınız {}".format(hak))
        hak = hak - 1


    elif sifre != takilanKart.get("kartsifresi") and hak == 0:
        print("şifrenizi 3 defa hatalı girdiniz! kartınız bloke olmuştur lütfen en yakın şubeye başvurunuz.")
        exit()

if sec == "1":
    print("hesap bakiyeniz {} TL'dir".format(takilanKart.get("hesapbakiye")))


elif sec == "2":
    print("kredi kartı borç bakiyeniz: {} TL'dir son ödeme tarihi {} ".format(takilanKart.get("kredikartborc"),
                                                                              takilanKart.get("kredkartborctarih")))

elif sec == "3":
    miktar1 = int(input("lütfen çekilecek tutarı giriniz:"))
    if takilanKart.get("hesapbakiye") < miktar1:
        print("yetersiz bakiye")
    else:
        print("lütfen önce paranızı sonra kartınızı alınız.")
        yenibakiye = takilanKart.get("hesapbakiye") - miktar1
        print("kalan bakiyeniz: {}".format(yenibakiye))

elif sec == "4":
    miktar2 = int(input("lütfen yatıralacak tutarı giriniz:"))
    print("paranız hesabınıza yatırılmıştır.")
    yenibakiye2 = takilanKart.get("hesapbakiye") + miktar2
    print("kalan bakiyeniz: {}".format(yenibakiye2))

elif sec == "5":
    print("iyi günler dileriz.")

    exit()

else:
    print("lütfen geçerli bir giriş yapınız.")
