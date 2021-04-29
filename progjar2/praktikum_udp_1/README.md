Soal Tugas Praktikum UDP 1
1.	Loadlah file tersebut di simulator
2.	Jalankan program progjar2/udpserver.py di alpine-1
3.	Jalankan program progjar2/udpclient.py di alpine-2
4.	Untuk nomor 2 dan 3 sesuaikan parameter dan variabel program agar sesuai dengan lingkungan jaringan,
5.	Buatlah screenshot dari hasil nomor 2 dan 3 
6.	Untuk screenshot harap diletakkan di sebuah dokumen PDF dan disubmit

Jawaban:
1. Pertama, cek terlebih dahulu IP Address dari server yaitu Alpine-1 dengan mengetik ifconfig.
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_1/gambar_praktikum_udp_1/ifconfig_server.PNG)
2. Kemudian ubah code udpclient.py dengan ip address server.
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_1/gambar_praktikum_udp_1/alphine2_client.PNG)
3. Kemudian ubah code udpserver.py dengan ip address server.
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_1/gambar_praktikum_udp_1/alphine1_server.PNG)
4. Kemudian jalankan udpserver.py pada alpine-1.
5. Jalankan juga udpclient.py pada alpine-2. Berikut hasilnya.
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_1/gambar_praktikum_udp_1/udpclient.PNG)
6. Berikut hasil yang muncul pada server Alpine-1
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar2/praktikum_udp_1/gambar_praktikum_udp_1/udpserver.PNG)
