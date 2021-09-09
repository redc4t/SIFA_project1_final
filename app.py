from flask import Flask

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def character_sheet():
    if request.method == 'POST':
        return home.html
    else:
        return about.html

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@192.162.0.1:3306/mydb'
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')



