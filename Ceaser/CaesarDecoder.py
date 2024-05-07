def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Karakter bir harf mi kontrol ediyoruz
            shifted = ord(char) - shift  # Karakterin ASCII değerinden kaydırma miktarını çıkarıyoruz
            if char.islower():  # Küçük harf mi kontrol ediyoruz
                if shifted < ord('a'):  # 'a' karakterinin ASCII değerini aşmışsa
                    shifted += 26  # 26 harf ileri sarıyoruz 
                elif shifted > ord('z'):  # 'z' karakterinin ASCII değerinden büyükse
                    shifted -= 26  # 26 harf geri sarıyoruz 
            elif char.isupper():  # Büyük harf mi kontrol ediyoruz
                if shifted < ord('A'):  # 'A' karakterinin ASCII değerini aşmışsa
                    shifted += 26  # 26 harf ileri sarıyoruz 
                elif shifted > ord('Z'):  # 'Z' karakterinin ASCII değerinden büyükse
                    shifted -= 26  # 26 harf geri sarıyoruz 
            decrypted_text += chr(shifted)  # Kaydırılmış karakteri şifreli metne ekliyoruz
        elif char.isspace():  # Boşluk karakteri mi kontrol ediyoruz
            decrypted_text += char  # Boşluk karakterini doğrudan ekliyoruz
        else:
            print("Error: Non-alphabetic character detected!")  # Harf veya boşluk değilse hata mesajı yazdırıyoruz
            return None  # None döndürerek fonksiyonu sonlandırıyoruz
    return decrypted_text

def main():
    text = input("Enter the text to decrypt: ")  # Kullanıcıdan çözülecek metni alıyoruz
    shift = int(input("Enter the shift value (positive integer): "))  # Kaydırma miktarını alıyoruz
    decrypted_text = decrypt(text, shift)
    if decrypted_text is not None:
        print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
