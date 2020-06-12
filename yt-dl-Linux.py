#!/usr/bin/python3

#Importar librerias necesarias: yt_dl para descargar, sys para los argumentos.
import youtube_dl
import argparse
import os

#Esta función mediante varios truquis te acaba creando y devolviendo una carpeta 'yt_downloads' dentro de descargas
def check_dir():
        user = os.environ['HOME']
        ruta = user + '/Downloads/'
        down_fin = os.path.dirname(ruta + 'yt_downloads/')
        if not os.path.exists(down_fin):
            os.mkdir(down_fin)
        return down_fin


def main():
    #Crear instancia de parseo de argumentos
    parser = argparse.ArgumentParser(usage='yt_downloader.py [-a] [-g <género>] -u <URL|VIDEO_ID>',description='El unico argumento obligatorio es -u, para indicar el recurso a descargar. Por defecto descargara el video, pero tienes opcion de indicar para descargar tanto audio como video. La opción de genero la recomiendo para luego poder organizar los archivos que descargues en base a este u otro tag que se te imagine. Con este programa tienes opcion de descargar basicamente lo que quieras: playlist, canales, posiblemente "me gusta"; aqui tienes una lista de sitios admitidos: https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md')

    #Define las opciones de argumentos y sus acciones
    parser.add_argument('-u',dest='url',help='Url/id a descargar, esta es obligatoria (evidentemente xd)',required=True)
    parser.add_argument('-a',dest='audio',action='store_true',help='Descarga el audio')
    parser.add_argument('-g',dest='genero',help='Te permite indicar el genero')
    #Parsea argumentos
    args = parser.parse_args()

    if args.genero == None:
        args.genero = ''
    else:
        args.genero = '-' + args.genero

    downs_dir = str(check_dir())

    #Descargar el audio/video
    if args.audio:
        ydl_opts = {
            'outtmpl': downs_dir + '/%(title)s' + args.genero +'.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }]
            }
    else:
        ydl_opts = {
            'outtmpl': downs_dir + '\%(title)s' + args.genero +'.%(ext)s',
        }

    #Descargar el archivo
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])

main()
