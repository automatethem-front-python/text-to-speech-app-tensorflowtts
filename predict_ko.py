import numpy as np
import soundfile as sf
import yaml
import tensorflow as tf
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor

import python_supporter
import random
from pydub import AudioSegment

# initialize fastspeech2 model.
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")
# initialize mb_melgan model
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-kss-ko")
# inference
processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-kss-ko")

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

if __name__ == "__main__":
    text = "안녕하세요. 테스트입니다."
    save_file = './audio_after.wav'
    text_to_speech(text, save_file)
