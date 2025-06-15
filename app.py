# app.py

import os
import tqdm
import numpy as np
import musdb
import random
import torch
import torchaudio
import torch.nn as nn
import sounddevice as sd
import torch.optim as optim
from IPython.display import Audio
from encodec import EncodecModel
from encodec.utils import convert_audio
import gradio as gr
import torchaudio
import io
import soundfile as sf
from inference import AudioTransformerPipeline

pipeline = AudioTransformerPipeline()



def run_inference(audio):
    # Read and immediately copy waveform from Gradio's temp file
    with open(audio, "rb") as f:
        data, sr = sf.read(io.BytesIO(f.read()))

    # Convert to (channels, samples)
    if data.ndim == 1:
        data = data[None, :]
    else:
        data = data.T

    waveform = torch.tensor(data, dtype=torch.float32)

    if sr != 24000:
        waveform = torchaudio.functional.resample(waveform, sr, 24000)
        sr = 24000

    output = pipeline.process(waveform)
    print("got here 4")
    return (sr, output.squeeze(0))



demo = gr.Interface(
    fn=run_inference,
    inputs=gr.Audio(type="filepath"),
    outputs=gr.Audio(label="Output Audio"),
    title="GPT-2 Audio Transformer Demo"
)

if __name__ == "__main__":
    demo.launch()
