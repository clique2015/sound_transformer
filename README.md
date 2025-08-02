 Installation
1. System Dependencies

Before you begin, install system-level packages:

sudo apt update
sudo apt install -y python3-venv libportaudio2 libportaudiocpp0 portaudio19-dev ffmpeg

2. Set Up Python Virtual Environment

It’s recommended to use a virtual environment to avoid conflicts:

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools

3. Install Python Dependencies

Use the provided requirements.txt file:

pip install -r requirements.txt

Or install packages manually:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tqdm numpy musdb ffmpeg-python==0.2.0 sounddevice ipython encodec soundfile gradio

4. Optional: Use Bleeding-Edge Encodec

To install the latest version of Encodec from source:

pip install git+https://github.com/facebookresearch/encodec#egg=encodec

    ⚠️ This may include experimental changes not in the stable release.

5. Launch the App

Once everything is installed, start the app:

python app.py
