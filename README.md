# text-to-speech-app-tensorflowtts

https://pypi.org/project/TensorFlowTTS/  

git  
Download for Windows  
https://git-scm.com/download/win

```
conda create -n text-to-speech-app-tensorflowtts python=3.7.16
conda activate text-to-speech-app-tensorflowtts

conda install --file requirements_conda.txt -y
pip install -r requirements.txt
```

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
