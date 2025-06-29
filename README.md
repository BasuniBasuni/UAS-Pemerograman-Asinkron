# UAS-Pemerograman-Asinkron
1. Buat program async untuk mengambil data dari 3 URL secara parallel
1.	Import Pustaka:
-	asyncio digunakan untuk menjalankan fungsi asinkron.
-	aiohttp adalah pustaka yang memungkinkan kita untuk melakukan permintaan HTTP secara asinkron.
2.	Fungsi fetch(url):
-	Fungsi ini adalah fungsi asinkron yang bertugas untuk mengambil konten dari URL yang diberikan.
-	aiohttp.ClientSession() digunakan untuk membuat sesi HTTP. Menggunakan sesi ini memungkinkan kita untuk melakukan beberapa permintaan dengan lebih efisien.
-	session.get(url) melakukan permintaan GET ke URL yang diberikan.
-	await response.text() mengembalikan konten respons sebagai teks.
3.	Fungsi main():
-	Di dalam fungsi ini, kita mendefinisikan daftar URL yang ingin kita ambil datanya.
-	tasks = [fetch(url) for url in urls] membuat daftar tugas asinkron untuk setiap URL.
-	await asyncio.gather(*tasks) menjalankan semua tugas secara bersamaan dan menunggu hingga semuanya selesai.
-	Setelah semua hasil diperoleh, kita mencetak setiap hasil ke konsol.
4.	Menjalankan Program:
-	if __name__ == '__main__': memastikan bahwa kode di bawahnya hanya dijalankan jika file ini dieksekusi sebagai program utama.
-	asyncio.run(main()) memulai eksekusi fungsi main().
Dengan menggunakan pendekatan ini, kita dapat mengambil data dari beberapa sumber secara efisien dan cepat. Ini sangat berguna dalam aplikasi yang memerlukan pengambilan data dari banyak API atau situs web secara bersamaan.
![image](https://github.com/user-attachments/assets/9f1f2594-3da1-491b-be45-11216be638ee)
![image](https://github.com/user-attachments/assets/5532434a-14fb-4fa8-9121-1725bbf3a19a)
2. Buatlah program FastAPI yang menangani permintaan POST async.
Saya telah membuat program FastAPI lengkap yang menangani berbagai jenis         permintaan POST async! Program ini mencakup:
Fitur Utama:
-	5 endpoint POST berbeda dengan use case yang berbeda
-	Async/await patterns yang proper
-	Pydantic models untuk validasi data
-	Error handling dengan HTTPException
-	Simulasi operasi database dan API eksternal
Endpoint yang tersedia:
1. 	/users - Membuat user baru dengan validasi async
2.	/tasks - Membuat task dengan notifikasi async
3.	/process-data - Memproses data dengan concurrent operations
4.	/external-api - Memanggil API eksternal menggunakan httpx
5.	/batch-process - Memproses data dalam batch secara async
  ![image](https://github.com/user-attachments/assets/fda15546-29e6-4f2c-a454-2138d9fce723)
 





 
 
   


 

