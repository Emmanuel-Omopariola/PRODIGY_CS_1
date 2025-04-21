# cipher_tool.py
from flask import Flask, request, render_template

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted = decrypted = ''
    if request.method == 'POST':
        message = request.form['message']
        shift = int(request.form['shift'])
        action = request.form['action']

        if action == 'Encrypt':
            encrypted = caesar_cipher(message, shift, 'encrypt')
        elif action == 'Decrypt':
            decrypted = caesar_cipher(message, shift, 'decrypt')

    return render_template('index.html', encrypted=encrypted, decrypted=decrypted)

if __name__ == '__main__':
    app.run(debug=True)
