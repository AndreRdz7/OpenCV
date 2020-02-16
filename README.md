# OpenCV

This repository covers the basics of OpenCV for computer vision, the code in here is based on tutorials/instructions (as well as the
images) from [Pieran Data](https://www.pieriandata.com/) (by Jose Portilla]) [Udemy's](https://www.udemy.com/course/python-for-computer-vision-with-opencv-and-deep-learning/) course

To execute notebooks and some scripts, you just need to install [Anaconda](https://www.anaconda.com/distribution/) in your system, and create an environment using the *opencv.yml* specification provided in the repository.
**Be sure to decompress the .zip folder file, this is where all images are stored.**

Once downloaded, lauch the Anaconda prompt and type:
```bash
conda env create -f opencv.yml
```  
To verify environment creation:  
```bash
conda env list
```
And should display: 'opencv' in the list.  
To activate the environment:
```bash
conda activate opencv
```  
Inside this repository run the notebooks replacing 'x' by the name:  
```bash
jupyter notebook x.ipynb
```
Inside this repository run the scripts replacing 'x' by the name:  
```bash
python x.py
```
