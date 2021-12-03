from pytube import YouTube

url = input("Masukkan link video : ") 
if url == '': print("Masukkan link video!!!") 
yt = YouTube(url) 

yt.streams.get_highest_resolution().download("download") 

print(" Selesai, Silahkan cek folder download!") 