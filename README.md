# jetsonrecycling
Project for NVIDIA Jetson AI Certificate

Jetson Recycling is a tool to identify which items are recycleble and which aren't. This helps people who struggle to identify which trash objects belong in which can.


# Installation

install jetson inference from github
```
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy nano scrot python3-pip
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make -j$(nproc)
ATTENTION YOU WILL GET WRITTEN ASKING FOR THE MODELS TO DOWNLOAD, YOU MUST CHOOSE ALL MODELS OBJECT DETECTION
sudo make install
sudo ldconfig
```

Clone Git Repository:

```
git clone https://github.com/johannesdiehm/jetsonrecycling/
```
This Code is written for a logitech USB-Camera. If you useanother camera type, you might have to change the code. (Replace /dev/video0)

# Run in command line

```
python3 my-detection.py
```

# Video Link

https://drive.google.com/drive/folders/1G419vxTTYxZy2EkdyRdokwCHDR7ri2f1?usp=sharing

Have fun with the Recycling Program :) 










