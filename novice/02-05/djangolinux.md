jalankan di terminal
langkah berikut dijalankan jika sudah menginstal python, virtualenv dan Django

buat folder untuk menyimpan project:
    1. mkdir (nama folder)
    2. cd (nama folder yg telah di buat)
setelah masuk ke folder -- tujuannya untuk buat direktori baru virtual agar tidak tercampur:
    virtualenv (nama virtual)
aktifkan direktori virtual tsb:
    . venv/bin/activate
akan muncul nama direktori virtual tsb didepan alamat direktori asli
install django dalam direktori virtual:
    pip install django==(versi yang diinginkan)

mulai project baru:
    django-admin startproject (nama project)

masuk kefolder project dan jalankan:
    python manage.py runserver
buka link yang muncul di browser anda
jika sudah berhasil lanjut langkah berikut

mulai buat project anda