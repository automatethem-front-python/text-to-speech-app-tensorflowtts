import numpy as np
import soundfile as sf
import yaml
import tensorflow as tf
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor
import python_supporter
import random
from pydub import AudioSegment

'''
# initialize fastspeech2 model.
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")
# initialize mb_melgan model
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")
# inference
processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")
'''
#'''
# initialize fastspeech2 model.
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")
# initialize mb_melgan model
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-kss-ko")
# inference
processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")
#'''

def text_to_speech(text, save_file):
    input_ids = processor.text_to_sequence(text)

    # fastspeech inference
    mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
        input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
        energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    )
    # melgan inference
    audio_before = mb_melgan.inference(mel_before)[0, :, 0]
    audio_after = mb_melgan.inference(mel_after)[0, :, 0]
    
    # save to file
    #sf.write('./audio_before.wav', audio_before, 22050, "PCM_16")
    #sf.write('./audio_after.wav', audio_after, 22050, "PCM_16")
    sf.write(save_file, audio_after, 22050, "PCM_16")

#https://stackoverflow.com/questions/59819936/adding-a-pause-in-google-text-to-speech
#pydub-concatenate-mp3-in-a-directory
#https://stackoverflow.com/questions/26363558/pydub-concatenate-mp3-in-a-directory
def test_to_speech_break(text, save_file):
    #contents = "Hello with <break><break> 1 seconds pause"
    parts = text.split("<break>") # I have chosen this symbol for the pause.
    pause1s = AudioSegment.from_mp3("predict_inputs/pause_1second.mp3") 
    cnt = 0
    combined = AudioSegment.empty()
    for p in parts:
        # The pause will happen for the empty element of the list
        if not p:
            combined += pause1s
        else:
            tmpFileName = "predict_inputs/tmp"+str(cnt)+".wav"
            text_to_speech(p, tmpFileName)
            combined+=AudioSegment.from_mp3(tmpFileName) 
        cnt+=1     
    combined.export(save_file, format="mp3") 
    
if __name__ == "__main__":
    #text = "Hello with <break><break> 2 seconds pause"
    #text = "안녕하세요 <break><break> 반갑습니다"
    text = python_supporter.file.read_file("predict_inputs/inputs.txt")
    test_to_speech_break(text, "predict_outputs/outputs.mp3")
