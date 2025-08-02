<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>

  <h2>🛠️ Installation</h2>

  <h3>1. System Dependencies</h3>
  <p>Before you begin, install the required system-level packages:</p>
  <pre><code>sudo apt update
sudo apt install -y python3-venv libportaudio2 libportaudiocpp0 portaudio19-dev ffmpeg</code></pre>

  <h3>2. Set Up Python Virtual Environment</h3>
  <p>Use a virtual environment to isolate your project's dependencies:</p>
  <pre><code>python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools</code></pre>

  <h3>3. Install Python Dependencies</h3>
  <p>Install all required Python packages using the <code>requirements.txt</code>:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <p>Or, you can install them manually:</p>
  <pre><code>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tqdm numpy musdb ffmpeg-python==0.2.0 sounddevice ipython encodec soundfile gradio</code></pre>

  <h3>4. Optional: Use Bleeding-Edge Encodec</h3>
  <p>To install the latest (unreleased) version of <strong>Encodec</strong> from GitHub:</p>
  <pre><code>pip install git+https://github.com/facebookresearch/encodec#egg=encodec</code></pre>
  <p><strong>⚠️ Note:</strong> This may include experimental changes not present in the stable release.</p>

  <h3>5. Launch the App</h3>
  <p>Once everything is set up, you can run the application using:</p>
  <pre><code>python app.py</code></pre>

</body>
</html>
