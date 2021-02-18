postgresql
panduan:
masuk akun : sudo -i -u (masukkan nama usernya tanpa kurung)
masuk ke psql : psql
buat database : createdb (nama database tanpa kurung)
cek info lokasi : \conninfo

buat tabel = CREATE TABLE table_name (
    		column_name1 col_type (field_length) column_constraints,
		 column_name2 col_type (field_length),
    		column_name3 col_type (field_length)
		);

contoh = CREATE TABLE playground (
    equip_id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (25) NOT NULL,
    location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date
);

lihat tabel = \d
lihat data tabel = \dt

input data= INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2014-04-28');
INSERT INTO playground (type, color, location, install_date) VALUES ('swing', 'yellow', 'northwest', '2010-08-16');

lihat data yg diinput = SELECT * FROM playground;
hapus data =DELETE FROM playground WHERE type = 'slide';

tambah kolom = ALTER TABLE playground ADD last_maint date;
hapus kolom = ALTER TABLE playground DROP last_maint date;
update data = UPDATE playground SET color = 'red' WHERE type = 'swing';


