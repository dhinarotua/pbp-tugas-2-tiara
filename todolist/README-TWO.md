## README Tugas 6
Nama: Dhina Rotua Mutiara
<br />NPM: 2106702182

### Perbedaan antara Asynchronous Programming dengan Synchronous Programming
Pada _synchronous programming_, program berjalan secara sequential, yaitu task akan dijalankan secara berurutan. Contoh: pada aplikasi Todolist, setelah melakukan penambahan task aplikasi akan reload terlebih dahulu, lalu menampilkan hasil penambahan task.

<br>

Pada _asynchronous programming_, program berjalan secara paralel, yaitu suatu task dapat berjalan tanpa harus menunggu antrian. Contoh: pada aplikasi Todolist, kita dapat langsung melihat perubahan task setelah menambahkan suatu task tanpa harus menunggu aplikasi reload.

### Paradigma Event-Driven Programming dalam Penerapan JavaScript dan AJAX
Paradigma _event-driven programming_ merupakan paradigma yang alurnya ditentukan oleh suatu event seperti tindakan pengguna atau pesan dari program lainnya. Pada aplikasi Todolist, _event-driven programming_ diterapkan pada saat menekan tombol `create` di modal `Tambah Task Baru`. Ketika tombol ditekan, function `add-task` akan dipanggil dan dijalankan untuk menambah task baru.

### Penerapan Asynchronous Programming pada AJAX
AJAX digunakan untuk melakukan request dan handling response. Pada AJAX, asynchronous programming diterapkan pada function `post` dan suatu function lainnya. Ketika user melakukan request (misalnya dengan menekan tombol), suatu method akan menjadi callback bagi function `post`. Response dari AJAX adalah output function callback akan langsung ditampilkan tanpa harus mereload halaman.

### Penjelasan Implementasi
1. Membuat function baru yang mengembalikan seluruh data task dalam bentuk JSON pada `views.py`.
2. Membuat function `add_task` pada `views.py` untuk menghandle penambahan task baru dan mengembalikannya dalam bentuk `JsonResponse`.
3. Melakukan routing dengan cara menambahkan path fungsi-fungsi tersebut ke dalam urlpatterns pada `urls.py`.
4. Menambahkan script AJAX (Jquery) pada `todolist.html`.
5. Melakukan pengambilan task dengan AJAX GET dengan cara membuat function untuk menge-GET data dari JSON dan melalukan mapping dengan function pembuatan task.
6. Menambahkan tombol `Tambah Task Baru` untuk membuka modal sebagai proses penambahan task baru.
7. Menambahkan `data-bs-dismiss="modal"` pada tag button di modal agar modal langsung tertutup ketika tombol di-klik (task berhasil ditambahkan).
8. Membuat method `post` untuk menampilkan hasil perubahan pada aplikasi (terdapat penambahan task baru).