sudo apt update
sudo apt upgrade

sudo apt install python3 python3-pip python3-venv ffmpeg

python3 -m venv cartoonenv
source cartoonenv/bin/activate

pip install opencv-python moviepy numpy

git clone https://github.com/vishala5000/Video-to-cartoon.git

cd Video-to-cartoon
python3 vc.py

