def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Karakter bir harf mi kontrol ediyoruz
            shifted = ord(char) + shift  # Karakterin ASCII değerine kaydırma miktarını ekliyoruz
            if char.islower():  # Küçük harf mi kontrol ediyoruz
                if shifted > ord('z'):  # 'z' karakterinin ASCII değerini aşmışsa
                    shifted -= 26  # 26 harf geri sarıyoruz 
                elif shifted < ord('a'):  # 'a' karakterinin ASCII değerinden küçükse
                    shifted += 26  # 26 harf ileri sarıyoruz 
            elif char.isupper():  # Büyük harf mi kontrol ediyoruz
                if shifted > ord('Z'):  # 'Z' karakterinin ASCII değerini aşmışsa
                    shifted -= 26  # 26 harf geri sarıyoruz 
                elif shifted < ord('A'):  # 'A' karakterinin ASCII değerinden küçükse
                    shifted += 26  # 26 harf ileri sarıyoruz 
            encrypted_text += chr(shifted)  # Kaydırılmış karakteri şifreli metne ekliyoruz
        elif char.isspace():  # Boşluk karakteri mi kontrol ediyoruz
            encrypted_text += char  # Boşluk karakterini şifrelemiyoruz, doğrudan ekliyoruz
        else:
            print("Error: Non-alphabetic character detected!")  # Harf veya boşluk değilse hata mesajı yazdırıyoruz
            return None  # None döndürerek fonksiyonu sonlandırıyoruz
    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ")  # Kullanıcıdan şifrelenecek metni alıyoruz
    shift = int(input("Enter the shift value (positive integer): "))  # Kaydırma miktarını alıyoruz
    encrypted_text = encrypt(text, shift)  # Metni şifreliyoruz
    if encrypted_text is not None:
        print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
