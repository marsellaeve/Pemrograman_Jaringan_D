from file_client_cli import remote_get
import time
import datetime
from multiprocessing import Process

def download_100():
    texec = dict()
    catat_awal = datetime.datetime.now()
    filename = 'pokijan.jpg'
    for k in range(100):
        print(f"download get {k}")
        waktu = time.time()
        # bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        texec[k] = Process(target=remote_get, args=(filename,))
        texec[k].start()
    # setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in range(100):
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


# fungsi download_gambar akan dijalankan secara multi process
if __name__ == '__main__':
    download_100()
