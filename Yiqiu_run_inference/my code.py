# Create a virtual environment
$ python3 -m venv venv-stt

#mkvirtualenv
pip install virtualenv
pip install virtualenvwrapper
pip install virtualenvwrapper-win
mkvirtualenv coqui-stt-venv

# Install 🐸STT model manager
$ python -m pip install -U pip
$ python -m pip install coqui-stt-model-manager

#download the stt model from https://coqui.ai/english/coqui/v1.0.0-huge-vocab#download

#Then installing the stt to virtual environment
python -m pip install -U pip
python -m pip install stt

#Use the command below to test your inference
stt --model model.tflite --scorer huge-vocabulary.scorer --audio my_audio_file.wav

