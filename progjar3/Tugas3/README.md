#### Made by Evelyn Tjitrodjojo 05111840000099

### Deskripsi Kasus

Terdapat 2 server dan 1 client, dimana client tersebut mendownload terlebih dahulu 2 file gambar, kemudian melakukan pengiriman file kepada 2 server tersebut menggunakan protokol transport UDP. Terdapat 2 file gambar yang diunduh client, dengan 1 file gambar tersebut diberikan kepada server 1, dan 1 file gambar lainnya diberikan kepada server 2. Pengiriman dari client kepada kedua server dilakukan dengan 5 program yang berbeda yaitu multi thread, multi process, multi thread async, multi process async, dan single thread.

### Gambar Arsitektur Jaringan (Dalam Simulator Gns3)

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/arsitektur_gns3.PNG)

Note: Alpine-1 sebagai server 1, Alpine 2 sebagai client, Alpine-3 sebagai server 2

### Hasil

Cek IP Alpine-1 (Server 1) -> ifconfig

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/alpine1_ipserver1.PNG)

Cek IP Alpine-2 (Client) -> ifconfig
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/alpine2_ipclient.PNG)

Cek IP Alpine-3 (Server 2) -> ifconfig
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/alpine1_ipserver2.PNG)

#### HASIL OUTPUT MULTI PROCESS

Client:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/multiprocess_client.PNG)

Server 1:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server1_multiprocess.PNG)

Server 2:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server2_multiprocess.PNG)

#### HASIL OUTPUT MULTI PROCESS ASYNC

Client:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/multiprocessasync_client.PNG)

Server 1:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server1_multiprocessasync.PNG)

Server 2:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server2_multiprocessasync.PNG)

#### HASIL OUTPUT MULTI THREAD

Client:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/multithread_client.PNG)

Server 1:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server1_multithread.PNG)

Server 2:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server2_multithread.PNG)

#### HASIL OUTPUT MULTI THREAD ASYNC

Client:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/multithreadasync_client.PNG)

Server 1:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server1_multithreadasync.PNG)

Server 2:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server2_multithreadasync.PNG)

#### HASIL OUTPUT SINGLE THREAD

Client:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/singlethread_client.PNG)

Server 1:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server1_singlethread.PNG)

Server 2:
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/server2_singlethread.PNG)

#### HASIL

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/list_client.PNG)

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/list_server1.PNG)

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar3/Tugas3/tugas3_screenshot/list_server2.PNG)
