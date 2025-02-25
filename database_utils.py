import sqlite3

def save_feedback(user_name, product_name, feedback):
    # Bağlantıyı aç
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Veriyi ekle
    c.execute('''
        INSERT INTO user_history (user_name, product_name, feedback)
        VALUES (?, ?, ?)
    ''', (user_name, product_name, feedback))

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

    print("Yorum başarıyla kaydedildi.")
