# Image-retrieval using AutoEncoders
The data set can be found in this link</br>
https://drive.google.com/file/d/1VT-8w1rTT2GCE5IE5zFJPMzv7bqca-Ri/view?usp=sharing
</br>
- The features from images were extracted using VGG16 and split into clusters using KMeans clustering.
- The images after clustering were trained using autoencoders, consisting of 5 CNN layers during encoding phase and similarly in the decoding phase.
- The features obtained from autoencoders are flattened then trained on KNN to obtain the distance with metric as cosine similarity.
- The output for testing will be as follows

![alt text](https://github.com/saiprasathgopinathan/Image-retrieval/blob/main/output/output.png?raw=true)
