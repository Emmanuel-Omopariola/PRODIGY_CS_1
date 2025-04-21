Caesar Cipher Web App

This app demonstrates a basic Caesar Cipher, one of the oldest and simplest forms of encryption.

 What it does:
- You enter a message and a number (shift value).
- The app shifts each letter by that number in the alphabet.
  For example, if you shift "A" by 3 → you get "D".

 Example:
- Message: HELLO
- Shift: 3
- Encrypted: KHOOR

Use the Decrypt button to reverse the process!

📌 Notes:
- Letters only shift alphabetically. Symbols and spaces are left unchanged.
- Shift value wraps around. For example, shifting "Z" by 1 becomes "A".

Perfect for learning the basics of encryption and how web apps work!



                                     USER INPUT
                                         ↓
                                  [Message: "HELLO"]
                                      [Shift: 3]
                              [Action: Encrypt or Decrypt]
                                          ↓
                                 FLASK WEB APP (Python)
                                          ↓
                               [Caesar Cipher Algorithm]
                                          ↓
                               ENCRYPTED/DECRYPTED MESSAGE
                                          ↓
                                  DISPLAYED ON SCREEN

TO run this locally first install requirements by running:
 "pip install requirements.txt"
And next run:
  "Caesar_cipher.py"