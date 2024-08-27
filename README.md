sudo apt update
sudo apt upgrade

sudo apt install python3 python3-pip python3-venv ffmpeg

python3 -m venv cartoonenv
source cartoonenv/bin/activate

pip install opencv-python moviepy numpy

