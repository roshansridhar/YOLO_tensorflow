EL-GY 6123 - IMAGE AND VIDEO PROCESSING Spring 2017  
Retail Store Usage Analysis  
Abhishek Vasu av1912  
Roshan Sridhar rs5788  

This directory contains   
1. python code 'YOLO_small_tf.py'  
2. weights file pre-trained on Pascal VOC  
3. own_dataset.mp4 input file supplied by advisor Yilin Song  
3. Output.avi output video after detection  
4. heatmap.png generated heatmap  


INSTRUCTIONS  
For default functioning, execute  on console:  

python YOLO_small_tf.py -fromfile own_dataset.mp4 -tofile_img output.avi  

(Already executed. Files generated are 'output.avi'(To reduce depository size, shortened to 25s to reduce size from 700MB to 60MB), 'heatmap.png')  

Important arguments include:  
-fromfile (input video filename) : input video file  
-tofile_img (output video filename) : output video file  
-disp_console (0 or 1) : to display results on terminal or not  
-imshow (0 or 1) : to display result video or not  

REQUIREMENTS:  
Python 2.7  
Numpy library  
Tensorflow library  
Opencv library  
Seaborn library  
Scipy library  
Scikit-learn library  

REFERENCES:  
Modified 'YOLO_tensorflow' by Choi. Original code found here: https://github.com/gliese581gg/YOLO_tensorflow   
