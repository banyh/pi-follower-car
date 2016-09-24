# pi-follower-car

## Prerequisite

#### Automatically Load Camera Module

```shell-script
echo "bcm2835-v4l2" >> /etc/modules
```

#### Install Python modules

```shell-script
apt-get install python-picamera python3-picamera libopencv-dev
pip install readchar
```

#### Enable X11 Forwarding on Putty

