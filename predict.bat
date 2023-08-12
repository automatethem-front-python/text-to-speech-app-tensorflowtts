::windows anaconda / reflex path
set path=%path%;C:\ProgramData\Anaconda3\Scripts
set path=%path%;%UserProfile%\Anaconda3\Scripts
call activate.bat
::call conda activate base
::call conda create -n virtualenv python=3.10.11
::call conda activate virtualenv
call conda activate text-to-speech-app-tensorflowtts
python predict.py