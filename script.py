import os 
import json
import subprocess

file = "film.mkv"

if not os.path.exists("./assets"): 
    os.makedirs("./assets") 
if not os.path.exists("./output"): 
    os.makedirs("./output") 
if not os.path.exists("./result"): 
    os.makedirs("./result") 

def ffprobe(file_path):
    f = open("info.json", "w")
    command_array = ["ffprobe",
                     "-v", "quiet",
                     "-print_format", "json",
                     "-show_format",
                     "-show_streams",
                     file_path]
    result = subprocess.run(command_array, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    f.write(result.stdout)

ffprobe(f'./assets/{file}')

with open('info.json') as f:
   data = json.load(f)

last_command = ["ffmpeg", "-i", "./result/video.mp4" ]
mid_command = ["-map","0:v"]
end_command = ["-c:v","copy" ,"-c:a" ,"aac" ,"-ac" ,"2" ,"-f","dash","./output/output.mpd"]

subtitle = 0
video = 0
audio = 0

for k in data['streams']:
    if k['codec_type'] == "subtitle":
        print("=========================================================================================================")
        print(f"./result/{k['tags']['language']}_{k['tags']['title']}")
        subprocess.run(["ffmpeg", "-v", "quiet", "-stats", "-i", f"./assets/{file}", "-map", f"0:{k['index']}", f"result/{k['tags']['language']}_{k['tags']['title']}.srt", "-map", f"0:{k['index']}", f"result/{k['tags']['language']}_{k['tags']['title']}.vtt"])

    elif k['codec_type'] == "video":
        print("=========================================================================================================")
        print(f"video")
        subprocess.run(["ffmpeg", "-v", "quiet", "-stats", "-i", f"./assets/{file}", "-map", f"0:v:0", "-c:v", "libx264", "-profile:v", "high", "-level:v", "4", "-pix_fmt", "yuv420p", "-f", "mp4", "result/video.mp4"])
        
    elif k['codec_type'] == "audio":
        audio +=1
        print("=========================================================================================================")
        print(f"./result/audio{k['index']}.mp4")
        subprocess.run(["ffmpeg", "-v", "quiet", "-stats", "-i", f"./assets/{file}", "-c:a", "aac", "-map", f"0:{k['index']}", "-b:a" , "256000", f"./result/audio{k['index']}.m4a"])
        last_command.append("-i")
        last_command.append(f"./result/audio{k['index']}.m4a")
        mid_command.append("-map")
        mid_command.append(f"{audio}:a")
        

command = last_command + mid_command + end_command
print(command)
subprocess.run(command)