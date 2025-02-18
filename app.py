from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

alphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 52
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 52
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    return plain_text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        text = request.form.get("text")
        try:
            shift = int(request.form.get("shift"))
            if action == "encrypt":
                return encryption(text, shift)  # Directly return result for AJAX
            elif action == "decrypt":
                return decryption(text, shift)
        except ValueError:
            return "Invalid shift key. Please enter an integer."
        except TypeError:
            return "Please fill in all the fields."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
