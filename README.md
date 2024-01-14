# Lalana-SQL-XSS
Approach:

Script ini dibuat untuk memeriksa potensi kerentanan XSS dan SQL Injection pada formulir di sebuah halaman web. Pendekatan yang digunakan adalah dengan mencari formulir dalam halaman, lalu mencoba menyuntikkan payload XSS dan SQL Injection ke dalam formulir tersebut untuk melihat apakah halaman rentan terhadap serangan tersebut.

Code Structure:

1.	Import Library:
•	Mengimpor library yang diperlukan: requests, BeautifulSoup, dan modul-modul terkait dari urllib.parse.
2.	Fungsi find_forms(url):
•	Mengambil konten halaman web dengan menggunakan requests.get.
•	Memparsing HTML halaman web menggunakan BeautifulSoup.
•	Menemukan dan mengembalikan semua elemen formulir (<form>).
3.	Fungsi submit_payload(form, url, payload, injection_type):
•	Mendapatkan atribut action dan method dari formulir.
•	Mengumpulkan data formulir yang diperlukan untuk menyertakan dalam permintaan.
•	Mengirimkan payload ke formulir menggunakan metode GET atau POST.
•	Mencetak pesan jika respons mengandung tanda bahwa payload dijalankan.
4.	Fungsi check_vulnerabilities(url):
•	Membuat payload XSS dan SQL Injection.
•	Mencari formulir di halaman dengan memanggil find_forms.
•	Mencoba menyuntikkan payload XSS dan SQL Injection ke dalam formulir yang ditemukan.
•	Memberikan feedback jika kerentanan ditemukan atau mencetak pesan jika tidak ada formulir.
5.	Fungsi main():
•	Meminta pengguna memasukkan URL aplikasi web target.
•	Memanggil check_vulnerabilities untuk memeriksa kerentanan pada halaman web tersebut.
6.	Menjalankan Skrip Utama:
•	Menggunakan blok if __name__ == "__main__": untuk menjalankan fungsi main() jika skrip dijalankan sebagai program utama.

Key Decisions:

•	Payload yang digunakan untuk menguji XSS: <script>alert("XSS")</script>

•	Payload yang digunakan untuk menguji SQL Injection: ' OR '1'='1' --

•	Penggunaan modul requests untuk melakukan permintaan HTTP.

•	Penggunaan modul BeautifulSoup untuk memparsing HTML halaman web.



Berikut langkah Langkah yang harus dilakukan terlebih dahulu:

pip install -r requirements.txt

Setelah semua terinstall lalu jalankan script dengan menggunakan:


python3 lalana.py
