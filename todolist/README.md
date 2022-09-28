## Link deploy: https://pbp-tugas-2-tiara.herokuapp.com/todolist/
Nama: Dhina Rotua Mutiara
<br />NPM: 2106702182

### Kegunaan `{% csrf_token %}` pada Elemen <form>
Pada elemen `<form>`, `{% csrf_token %}` digunakan untuk membuat token pada setiap pengiriman data. Dengan menambahkan potongan kode tersebut, form yang diisi oleh pengguna akan memiliki nilai token yang unik dan akan dihapus dari session saat pengiriman data selesai. Token ini dibuat untuk mencegah adanya serangan CSRF (Cross Site Request Forgery) seperti pengiriman request lain/lintas web saat pengguna mengisi form. Jika tidak menggunakan `{% csrf_token %}`, form yang disediakan akan lebih berbahaya bagi user karena adanya serangan CSRF.

### Pembuatan Elemen <form> secara Manual
Kita dapat membuat elemen form secara manual. Secara garis besar, untuk membuat form manual kita harus membuat tag form terlebih dahulu. Di dalam tag form, kita tambahkan atribut action dan method. Selanjutnya, barulah kita tambahkan tag input sebagai field pengisian form dan `<input type=”submit” />` untuk menampilkan tombol submit yang berfungsi untuk mengirim form.

### Proses Alur Data
Mula-mula, user akan mengisi form dan mengirimnya melalui button submit. Setelah form tersubmit, akan terbentuk HTTP request. Request ini akan dikirimkan ke views dan akan melakukan aksi sesuai dengan function pada views. Setelah views menerima request tersebut, views akan meneruskannya ke model dan database, lalu mengembalikannya dalam bentuk HTTP response. HTTP response akan disesuaikan dengan template HTML. Untuk menampilkan data pada laman HTML, kita hanya perlu menuliskan kode untuk mengakses database (misalnya `{{ user.get_username }}`) atau mengiterasi data yang disimpan dalam list.

### Penjelasan Implementasi
1. Membuat django-app bernama todolist dengan syntax `python manage.py startapp todolist`.
2. Menambahkan path todolist pada file `settings.py` dan `urls.py` pada folder `project_django`.
3. Membuat model Task dengan atribut user, date, title, description, dan is_finished pada file `models.py`. Setelah itu, melakukan migrate untuk menerapkan skema model yang dibuat ke database Django lokal.
4. Menambahkan function show_todolist, register, login_user, logout_user, dan create_task pada `views.py`. Isi dari setiap function disesuaikan dengan kegunaan dan restrictionnya (misalnya login required).
5. Membuat template `login.html`, `register.html`, `todolist.html`, dan `create-task.html` yang desainnya disesuaikan dengan perintah soal. Pembuatan tampilan HTML ini dilakukan dengan cara membaca dokumentasi HTML di internet.
6. Membuat file `create_form.py` untuk menghandle pembuatan task baru pada form.
7. Melakukan routing dengan cara menambahkan path fungsi-fungsi tersebut ke dalam urlpatterns pada `urls.py`.
8. Melakukan push ke repositori dan sudah auto deploy.
9. Membuat 2 akun yang masing-masing memiliki 3 task.