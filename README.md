# text-to-speech-app-tensorflowtts

https://pypi.org/project/TensorFlowTTS/  

models  
https://huggingface.co/tensorspeech

## 윈도우

pause1s = AudioSegment.from_mp3("predict_inputs/pause_05second.mp3")  
FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다    
압푹 풀어 bin 폴더내 실행 파일을 복사해보기  
https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip  
https://ffmpeg.org/download.html  
https://stackoverflow.com/questions/68247327/cannot-find-a-solution-to-winerror-2-file-not-found-by-audiosegment-from-mp3

```
ffmpeg
ffplay
ffprobe
```

git  
Download for Windows  
https://git-scm.com/download/win

```
conda create -n text-to-speech-app-tensorflowtts python=3.7.16
conda activate text-to-speech-app-tensorflowtts

conda install --file requirements_conda.txt -y
conda install --file requirements_conda_esri.txt -y -c esri
pip install -r requirements.txt
pip install -r requirements_reinstall.txt --upgrade --force-reinstall
```

```
python predict.py
```

참고) 무음 mp3 만들기
```
#create-a-silent-mp3-from-the-command-line
#https://stackoverflow.com/questions/5276253/create-a-silent-mp3-from-the-command-line
#ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t <seconds> -q:a 9 -acodec libmp3lame pause_1second.mp3
ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 0.5 -q:a 9 -acodec libmp3lame pause_05second.mp3
ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 1 -q:a 9 -acodec libmp3lame pause_1second.mp3
```

참고) 언어

https://jiyeonseo.github.io/2020/10/13/py-lang-detection/

참고 자료)

You’re able to add commas that will add a “natural pause” in the speech.  
https://towardsdatascience.com/text-to-speech-lifelike-speech-synthesis-demo-part-1-f991ffe9e41e

