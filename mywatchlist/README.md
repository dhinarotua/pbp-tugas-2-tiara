## Link deploy: https://pbp-tugas-2-tiara.herokuapp.com/mywatchlist/
### JSON: https://pbp-tugas-2-tiara.herokuapp.com/mywatchlist/json/
### XML: https://pbp-tugas-2-tiara.herokuapp.com/mywatchlist/xml/
### HTML: https://pbp-tugas-2-tiara.herokuapp.com/mywatchlist/html/

Nama: Dhina Rotua Mutiara
<br />NPM: 2106702182

### Perbedaan antara JSON, XML, dan HTML
JSON merupakan format pertukaran data yang berfungsi untuk mengirimkan data dengan cara mengurai data. JSON juga lebih mudah dibaca oleh manusia dan dapat diakses oleh berbagai bahasa pemrograman. JSON menyimpan data dalam format map (key/value). JSON hanya mendukung beberapa tipe data. Transmisi data JSON cenderung lebih cepat karena menggunakan sedikit memori.
XML merupakan bahasa markup yang memiliki fungsi yang sama dengan JSON, yaitu untuk menyimpan dan mengirimkan data. Namun, XML cenderung lebih rumit. XML menyimpan data sebagai tree structure. XML mendukung berbagai tipe data yang kompleks. Transmisi data XML cenderung lebih lambat.
HTML berbeda dengan JSON dan XML. HTML lebih berfungsi untuk menampilkan data, bukan pengiriman data. Oleh karena itu, HTML tidak memiliki informasi mengenai isi data. HTML juga memiliki sintaks yang lebih sederhana dan mudah dimengerti. Tidak seperti XML yang wajib menggunakan end tag, end tag pada HTML bersifat opsional.

### Alasan Penggunaan Data Delivery
Data delivery diperlukan dalam pengimplementasian sebuah platform karena data delivery berfungsi untuk penyimpanan dan pengiriman data sehingga kita dapat melakukan pertukaran data antar platform dengan lebih cepat dan mudah.

### Penjelasan Implementasi
1. Membuat django-app bernama mywatchlist dengan syntax: python manage.py startapp mywatchlist
2. Menambahkan path mywatchlist pada file settings.py dan urls.py pada folder project_django.
3. Membuat model MyWatchList dengan atribut watched, title, rating, release-date, dan review pada file models.py. Setelah itu, melakukan migrate untuk menerapkan skema model yang dibuat ke database Django lokal.
4. Membuat file initial_mywatchlist_data.json pada folder fixtures untuk membuat 10 data dengan objek MyWatchList. Setelah itu, melakukan loaddata untuk menambahkan data ke database Django lokal.
5. Membuat beberapa fungsi sebagai implementasi data delivery HTML, XML, dan JSON pada views.py.
6. Melakukan routing dengan cara menambahkan path fungsi-fungsi tersebut ke dalam urlpatterns pada urls.py.
7. Menambahkan unit test pada test.py berdasarkan sumber di internet.
8. Melakukan push ke repositori dan sudah auto deploy.

### Screenshot Postman
1. JSON
<img width="636" alt="json" src="https://user-images.githubusercontent.com/100504894/191659470-163e2d3d-87ee-4ef3-96b4-764cc78c23af.png">
2. XML
<img width="633" alt="xml" src="https://user-images.githubusercontent.com/100504894/191659439-fac3720d-63b2-4be3-b91e-9fbec3c1e1ef.png">
3. HTML
<img width="633" alt="html" src="https://user-images.githubusercontent.com/100504894/191657186-ed540125-10bb-461b-9ec5-13a334e89cb3.png">
