# OpenCVTX2
Build and install OpenCV on NVIDIA Jetson TX2. Jetpack 3.2 (L4T 28.2)

To run the build file 

```
$ cd OpenCVTX2

$ ./buildOpenCV.sh
```
After build

```
$ cd opencv/build

$ make

```

After this, you can install the new build

```
$ cd opencv/build

$ sudo make install
```

## Release Notes
May 2018
* L4T 28.2
* OpenCV 3.4
* python 2.7 and 3.5 
* gstreamer support added to build script
* gstreamer OpenCV examples using the Jetson onboard camera 



