from pytube import Playlist
import os
from unidecode import unidecode
import re

logo = """ _____ __  _____     _____ _____ 
|  _  |  ||_   _|___|     |  _  |
|   __|  |__| | | . | | | |   __|
|__|  |_____|_| |___|_|_|_|__|   """

print(f"""{logo}   v0.1 
      
Feito por https://www.lexpdev.xyz
Github 
      
--------------------------""")

def download_playlist(url, fileformat):
    playlist = Playlist(url)
    
    playlist_title = unidecode(re.sub(r'[^\w\-_\. ]', '_', playlist.title))
    
    if not os.path.exists(unidecode(re.sub(r'[^\w\-_\. ]', '_', playlist.title))):
        os.makedirs(unidecode(re.sub(r'[^\w\-_\. ]', '_', playlist.title)))

    f = open(f"{unidecode(playlist_title)}/info.txt", "a", encoding="utf-8")
    f.write(f"""{logo}   v0.1
Feito por https://www.lexpdev.xyz/       
--------------------------------------------- 

Informações da playlist:

Link da playlist: {playlist_url}
Nome da playlist: {playlist_title} 
Views da playlist: {playlist.views}""")
    
    if fileformat == '1':
        f.write("""\n \nBaixando em MP3...
                
---------------------------------------------""")
    if fileformat == '2':
        f.write("""\n \nBaixando em MP4...
                
---------------------------------------------""")
    counter = 1
    for video in playlist.videos:
            try:
                if fileformat == "1":
                    videofilename = f"{counter} - {re.sub(r'[^\w\-_\. ]', '_', video.title)}.mp3"
                    video.streams.filter(only_audio=True).first().download(output_path=playlist_title, filename=unidecode(videofilename))

                    f.write(f"""\n{video.title} 
                            
Informações da música

Link da música: {video.watch_url}
Dono da música: {video.author}
Views da música: {video.views}
Tamanho da música: {video.length} segundos
Link da thumbnail da música: {video.thumbnail_url}

---------------------------------------------
    """)
                if fileformat == "2":
                    videofilename = f"{counter} - {re.sub(r'[^\w\-_\. ]', '_', video.title)}.mp4"
                    video.streams.filter().first().download(output_path=playlist_title, filename=unidecode(videofilename))
                    f.write(f"""\n{counter} - {video.title}
                            
Informações do vídeo

Link do vídeo: {video.watch_url}
Dono do vídeo: {video.author}
Views do vídeo: {video.views}
Tamanho do vídeo: {video.length}
Link da thumbnail do vídeo: {video.thumbnail_url}

---------------------------------------------""")

                print(f"{video.title} baixado \n")
                counter = counter + 1
            except Exception as e:
                f.write(f"Ocorreu um erro baixando {video.title}:\n{e}\n---------------------------------------------")
                print(f'Ocorreu um erro baixando {video.title}, talvez ele esteja indisponivel ou tem copyright.\nVeja o arquivo info.txt para saber o que aconteceu em detalhes.\nContinuando... \n')
                pass

    input('Download terminado! Foi criado um arquivo chamado info.txt dentro da pasta com informações sobre a playlist. (aperte enter pra sair)')
    f.close()
if __name__ == "__main__":
    fileformat = input('Você quer baixar que tipo de mídia? (1. Música ou 2. Vídeo): ')
    playlist_url = input("Insira o link da playlist do YouTube: ")
    print(f'---------Download iniciado---------')
    download_playlist(playlist_url, fileformat)
