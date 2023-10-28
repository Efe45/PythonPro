# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    with open('form.txt', 'a',) as f:
        f.write(name + '/')

    email = request.form['email']
    with open('form.txt', 'a',) as f:
        f.write(email + '/')

    date = request.form['date']
    with open('form.txt', 'a',) as f:
        f.write(date + '/')

    address = request.form['address']
    with open('form.txt', 'a',) as f:
        f.write(address + '/')




    return render_template('form_result.html',
                        name=name,
                        email=email,
                        date=date,
                        address=address


                        )
                                    
                                   

                    
app.run(debug=True)
