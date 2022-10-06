## README Tugas 5
Nama: Dhina Rotua Mutiara
<br />NPM: 2106702182

### Perbedaan Inline, Internal, dan External CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut element HTML. Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan ditulis di header file. External CSS adalah kode CSS yang ditulis terpisah dengan kode HTML, yaitu pada file berformat `.css`.
<br />Kelebihan dan kekurangan:

- Inline CSS: Kelebihannya adalah proses load website dan HTTP request lebih cepat. Kekurangannya adalah tidak efisien karena hanya dapat diterapkan pada satu elemen HTML.
- Internal CSS: Kelebihannya adalah perubahan pada file hanya berlaku pada satu halaman saja sehingga cocok untuk membuat halaman web dengan tampilan berbeda. Kekurangannya adalah tidak efisien jika ingin menggunakan CSS yang sama pada beberapa file dan performa website akan lebih lambat.
- External CSS: Kelebihannya adalah load website lebih cepat, 1 CSS dapat digunakan di beberapa halaman web, dan ukuran file HTML lebih kecil. Kekurangannya adalah tidak cocok untuk halaman website yang membutuhkan halaman custom dan halaman menjadi berantakan ketika CSS gagal di-call oleh HTML.

### Tag HTML5
* Tag `<title>...</title>` merupakan tag yang mendeskripsikan judul dokumen HTML.
* Tag `<body>...</body>` merupakan isi dari file HTML yang akan ditampilkan pada browser.
* Tag `<p>...</p>` merupakan tag untuk membuat paragraf.
* Tag `<br>` merupakan tag untuk memberikan enter antar line.
* Tag `<div>` merupakan penanda bagian dari suatu kode.

### Tipe-Tipe CSS Selector
* Selector tag: Melakukan modifikasi pada bagian elemen dengan memilih elemen berdasarkan nama tag.
* Selector class: Selektor yang memilih elemen berdasarkan nama class.
* Selector universal: Memilih elemen pada suatu scope.

### Penjelasan Implementasi
1. Mengaktifkan bootstrap dengan cara menambahkan link pada `base.html`.
2. Menggunakan free template pada login dan signup dan memodifikasi secara mandiri.
3. Menambahkan navigation bar pada laman utama Todo List.
4. Membuat card baru saat mengiterasi data todolist agar jumlah card bertambah seiring dengan pertambahan task baru.
5. Tidak mengatur responsive karena sudah otomatis pada bootstrap.