# UAS-Pemerograman-Asinkron
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





 
 
   


 

