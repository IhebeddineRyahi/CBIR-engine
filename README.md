# Content-based Image Retrieval Engine

In this job, I collaborated with <a href="https://github.com/ChaymaBouzaidii">Chayma Bouzaidi</a>   

## Table of contents
1. [Overview](#Overview)
2. [Requirements](#Requirements)
3. [Setting up MongoDB/GridFS](#Setup)  
4. [Start the App](#StartApp)


<a name="Overview"/>  

## Overview
In this project, we built a content-based image retrieval engine that allows users to send a request image in order to display similar images from 1M images database stored in GridFs (MongoDB).🧐  

To build this app, we followed this main steps:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Building feature vectors using `Principal Component Analysis`      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Storing feature vectors and thumbnail images in `MongoDB`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Building a `VP-Tree` to optimize searching time    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Setting an interactive web app using `Flask`   

**NB** : You can get 1M thumbnail images database and corresponding edge histogram descriptors from <a href="http://press.liacs.nl/mirflickr/mirdownload.html">here</a>  

<a name="Requirements"/>

## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • MongoDB (version 4.2.1).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Python (version 2.7.15+).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Create a MongoDB database called `CBIR`.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Specify your MongoDB connection URL in the script `app/app.py`.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `app/` directory and install the requirements via pip :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • `pip install flask numpy scipy matplotlib scikit-image gunicorn`.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • `pip freeze > requirements.txt`.  


<a name="Setup"/>

## Setting up MongoDB/GridFs
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Go to `scripts/` directory and run toGridFs.py script in order to dump the Thumbnails, the Principal Components and the VP-Tree into GridFs :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • `python toGridFs.py -td <YOUR_THUMBNAILS_DIRECTORY> -id <YOUR_PC_VPTREE_DIRECTORY>`.  
**NB** : You can get the Principal Components and the VP-Tree files from <a href="https://www.dropbox.com/s/rni799mkys56zph/pca_df.pkl?dl=0">here</a> and <a href="https://www.dropbox.com/s/dwg0x6csi4cthw3/vptree.pkl?dl=0">here</a>  

<a name="StartApp"/>

## Start the App  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Run `python app/app.py` to start the App.  
**NB** : The list of query images is static. You can change it by hosting the thumbnails on a <a href="https://fr.imgbb.com/">Free server</a> and specifying the image URL in `img` tag in `app/templates/index.html`.     
