# mkv-to-dash

## Description
Le but de ce script est de convertir un fichier au format "mkv" avec n'importe quel codec vidéo ou audio au format dash ".mpd" pour être dans la suite lisible dans un navigateur web.

## Prérequis
- ffmpeg
- Python 3+
  - Lib: os
  - Lib: json
  - Lib: subprocess

## FFMPEG commande
- Lors de la division:
  - VIDEO:
    - codec: **x264**
    - format: **mp4**
    - level: **4**
    - profile: **high**
    - pix_fmt: **YUV 4:2:0 planaire**
  - AUDIO:
    - codec: **AAC**
    - format: **m4a**
    - bitrate: **256k**
    - canaux audio: **2**
  - SOUS-TITRES
    - format: **VTT**
 
- Lors de la construction:
  - VIDEO
    - format: **dash / .mpd**

![schema](https://github.com/Oreo81/mkv-to-dash/assets/65022558/2ae8affa-f4d5-46af-9544-db3db3d6ce79)

## License
Ce projet est placé sous la licence MIT. Pour plus d'informations, voir le fichier LICENSE-MIT.
