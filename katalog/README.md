## Link deploy: https://pbp-tugas-2-tiara.herokuapp.com/katalog/
Nama: Dhina Rotua Mutiara
<br />NPM: 2106702182

### Bagan request client ke web aplikasi berbasis Django beserta responnya
![Untitled - Frame 1 (1)](https://user-images.githubusercontent.com/100504894/190307069-0072fb7d-4c65-457e-b0be-5ad18298420c.jpg)
Pada Django, terdapat 2 fase, yaitu fase request dan fase response. Pada fase request, request client akan diterima oleh web server yang selanjutnya disalurkan ke WSGI. WSGI akan memetakan HTTP request ke python objects dan mengeksekusi stack aplikasi. Setelah Django mengeksekusi request process dari stack, Django akan memuat konfigurasi URL project yang dibuat dalam file urls.py. Tahap akhir dari request adalah view. Jika urls.py berguna untuk menunjukkan lokasi informasi, views.py berguna untuk menampilkan informasi. Ketika route match, view akan menerima HTTP request/request data yang dibutuhkan ke model.
Selanjutnya adalah fase response. Setelah model menerima request dari views, terjadi komunikasi antara model dengan database. Kemudian, database akan mengirimkan data ke model. Data models dan entity & relationship antar data akan disimpan di models.py. Setelah itu, model akan mengirimkan data ke views. Setalah data diterima oleh views, views akan memilih template HTML yang akan didisplay ke client (HTTP response). Django akan mengkonversi HTTP response ke WSGI response yang sesuai dan mengirimnya ke web server. Web Server akan mengubah WSGI response ke format aslinya dan mengirimnya ke client.

### Virtual Environment
Virtual environment perlu digunakan karena project Django yang dibuat memiliki dependencies yang berbeda-beda sehingga dibutuhkan suatu environment yang tertutup dari luar. Misalnya, kita memiliki project yang menggunakan 2 versi library yang berbeda. Tanpa virtual environment, ada kemungkinan kita perlu melakukan downgrade pada project yang menggunakan versi yang lebih tinggi. Downgrade pada project dapat memicu terjadi error. Oleh karena itu, virtual environment dibutuhkan agar setiap project memiliki environmentnya sendiri dan dapat menggunakan modul yang berbeda-beda versi. Sesungguhnya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environtment. Namun, konsekuensinya adalah semua project kita akan menggunakan 1 package yang sama sesuai dengan yang install dan kemungkinan terjadi error akan meningkat.

### Penjelasan Implementasi
1. Membuat fungsi yang berparameter (request) dan mereturn render dengan parameter (request, “katalog.html”, context), serta memanggil fungsi query ke model database. Context berisikan data/hasil query yang disimpan dalam suatu variabel yang kemudian akan ditampilkan ke dalam HTML. Data tersebut diambil dari models.py sehingga saya mengimport CatalogItem terlebih dahulu.
2. Mengisi file urls.py dengan melakukan routing terhadap views sehingga HTML dapat ditampilkan di browser (import path & fungsi show_katalog) dan mendaftarkan aplikasi katalog.
3. Melakukan iterasi pada list_barang untuk memetakan data item_name, item_price, item_stock, rating, description, dan item_url. Data ini diload dari file .json pada folder fixtures.
4. Menge-push project ke akun github (membuat repository) dan menyambungkan ke heroku, melakukan konfigurasi (API key & name), dan menjalankan ulang workflow.
