import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Merhaba hos geldiniz asagıdaki linke tıklayarak teknoloji ile rastgele bir bilgi öğrene bilirsin!<a href="/rastgele_gercek">Iste link!</a>''Sarkı dinnemek için tıklayınız<a href="/sarki">Iste link!</a>'
@app.route("/sarki")
def Web_sitesi():
    return'Biraz şarkı güzel olur işte benim sevdiğim bir kaç şarkı'
'<a href="https://www.youtube.com/watch?v=srY3Y6r1-VY">diamonds</a>'
'<a href="https://www.youtube.com/watch?v=13F1O8kuAGY">woo</a>'
'<a href="https://www.youtube.com/watch?v=50VNCymT-Cs">let me down slowly</a>'
'<a href="https://www.youtube.com/watch?v=60ItHLz5WEA">faded</a>'
def Web_sitesi():
    facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."
,"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
,"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
,"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."
,"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."
,"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor."
,"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."
,"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)

