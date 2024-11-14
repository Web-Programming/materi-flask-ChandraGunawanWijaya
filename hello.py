from flask import Flask

# Membuat object flask
app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

# Menentukan route untuk halaman utama
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Membuat route baru
@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)