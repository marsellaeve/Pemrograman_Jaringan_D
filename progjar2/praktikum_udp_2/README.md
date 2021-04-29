#### Made by Evelyn Tjitrodjojo 05111840000099

Soal Tugas Praktikum UDP-2
-	Loadlah file tersebut di simulator. Dalam praktikum ini lakukan broadcast dari sebuah client udp di alpine-1 agar dapat membroadcast pengiriman ke alpine-2 dan alpine-3 sekaligus, tambahkan  host alpine-4 dan alpine-5 yang dapat dikirimi broadcast juga.
-	Gunakan file progjar2/udpclient_broadcast.py dan progjar2/udpserver_broadcast.py. Sesuaikan parameter dan variabel program agar sesuai dengan lingkungan jaringan,
-	Jalankan dengan urutan, server dan kemudian client
-	Jalankan dengan urutan client, baru kemudian server 
-	Apakah perbedaan yang terjadi ?
-	Buatlah dokumen PDF yang berisikan screenshot dari 
-	Modifikasi program yang dilakukan, dan hasil menjalankan dengan urutan berbeda tadi

Jawaban:

1. Buat Alpine-4 dan Alpine-5.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/alpine.png)

2. Karena Alpine-4 dan Alpine-5 belum terhubung internet, maka masukkan code berikut.

Alpine-4
- ifconfig eth0 192.168.122.97 netmask 255.255.255.0 up
- route add default gw 192.168.122.1
- echo "nameserver 192.168.122.1" > /etc/resolv.conf

Alpine-5
- ifconfig eth0 192.168.122.113 netmask 255.255.255.0 up
- route add default gw 192.168.122.1
- echo "nameserver 192.168.122.1" > /etc/resolv.conf

Nameserver 192.168.122.1 didapatkan dari alpine lainnya.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/nameserver.png)

3. Cek Alpine-4 dan Alpine-5 dengan ping google.com. Jika sudah terhubung, lakukan git clone repository Pemrograman-Jaringan-D. Ubah code udpserver_broadcast.py yang akan digunakan pada Alpine 2-5. Pusatkan pada 1 IP server, agar tidak perlu mengganti code pada semua server.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/udpserver.PNG)

4. Untuk IP pada client, biarkan 255.255.255.255. 

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/udpclient.PNG)

Selanjutnya, jalankan semua server terlebih dahulu (Alpine 2-5), kemudian jalankan client (Alpine 1). Berikut hasilnya.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/server_alphine2.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/server_alphine3.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/server_alphine4.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/server_alphine5.PNG)

Berikut Hasil Client.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/hasil_client.PNG)

#### Kesimpulannya bila dijalankan dengan urutan, server dan kemudian client, maka isi broadcast yang disampaikan ke semua server (alpine 2-5) berurutan mulai dari awal hingga akhir (Broadcast ini angka 1-selesai). Isi Broadcast tersampaikan dengan lengkap.

Selanjutnya, jalankan client (Alpine 1) terlebih dahulu, kemudian jalankan semua server (Alpine 2-5). Berikut hasilnya.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/2_hasil_client.PNG)

Berikut hasil semua server (Alpine 2-5).

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/2_server_alphine2.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/2_server_alphine3.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/2_server_alphine4.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_2/gambar_praktikum_udp_2/2_server_alphine5.PNG)

#### Kesimpulannya, bila dijalankan dengan urutan client, baru kemudian server, maka isi broadcast yang tersampaikan pada server sesuai dengan pesan yang dikirimkan setelah server berjalan (tidak dari awal). Contoh: Client mulai angka 1-40, server baru dijalankan setelah client mengirimkan pesan angka 10, maka pesan yang didapatkan server mulai dari angka 11. Begitu juga seterusnya dengan server lainnya, sesuai dengan waktu berjalannya server.
