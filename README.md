# text-to-speech-app-tensorflowtts

https://pypi.org/project/TensorFlowTTS/  

models  
https://huggingface.co/tensorspeech

## 윈도우

git  
Download for Windows  
https://git-scm.com/download/win

```
conda create -n text-to-speech-app-tensorflowtts python=3.7.16
conda activate text-to-speech-app-tensorflowtts

conda install --file requirements_conda.txt -y
pip install -r requirements.txt
pip install -r requirements_reinstall.txt --upgrade --force-reinstall
```

```
python predict.py
```

참고 자료)

You’re able to add commas that will add a “natural pause” in the speech.  
https://towardsdatascience.com/text-to-speech-lifelike-speech-synthesis-demo-part-1-f991ffe9e41e

