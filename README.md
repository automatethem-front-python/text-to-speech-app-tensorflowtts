# text-to-speech-app-tensorflowtts

https://pypi.org/project/TensorFlowTTS/  

models  
https://huggingface.co/tensorspeech

git  
Download for Windows  
https://git-scm.com/download/win

```
conda config --env --set subdir osx-64
```
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


===========

https://github.com/tensorflow/tensorflow/issues/60243
```
I had the same problem with python 3.11 on OS X. I don't think I have a GPU. I commented out the tensorflow-gpu lines in requirements.txt, and everything installed.
Now maybe nothing will work well without a GPU, we'll see
```
https://github.com/TensorSpeech/TensorFlowTTS/blob/master/setup.py
```
requirements = {
    "install": [
        #"tensorflow-gpu==2.7.0",
```
```
git clone https://github.com/TensorSpeech/TensorFlowTTS
cd TensorFlowTTS
pip install .
```

https://anaconda.org/hcc/tensorflow

======

```
conda config --env --set subdir osx-arm64
#conda config --env --set subdir osx-64

```
```
conda create -n text-to-speech-app-tensorflowtts python=3.8.17
conda activate text-to-speech-app-tensorflowtts

#conda install --file requirements_conda.txt -y
#TensorFlow Dependencies 설치
#For TensorFlow v2.6 
conda install -c apple tensorflow-deps==2.6.0
#TensorFlow & Plugin 설치
#python -m pip install tensorflow-macos
#python -m pip install tensorflow-metal
pip install tensorflow-macos
pip install tensorflow-metal

pip install -r requirements.txt
pip install -r requirements_reinstall.txt --upgrade --force-reinstall
```

```
python predict.py
```

======

```
python -m pip install tensorflow
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
```
