import os
import argparse

#PARSE ARGUMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-td", "--thumbnails_dir", required = True,
	help = "Path to the directory that contains the thumbnails (should end with '/')")
ap.add_argument("-id", "--pkl_dir", required = True,
	help = "Path to the directory that contains the Principal components (pca_df.pkl) and the VP-Tree (vptree.pkl) (should end with '/')")
args = vars(ap.parse_args())

thumbnails_path = args["thumbnails_dir"]
pkl_path = args["pkl_dir"]


#DUMP THUMBNAILS TO GRIDFS
for i in range(0,100):
    os.chdir(thumbnails_path+str(i))
    for j in range((i*10000),(i*10000+10000)):
        cmd = "mongofiles -d CBIR put "+str(j)+".jpg"
        os.system(cmd)
        print('image ' +str(j)+'.jpg is dumped')

#DUMP PRINCIPAL COMPONENTS AND VP-TREE TO GRIDFS
os.chdir(pkl_path)

cmd_pca = "mongofiles -d CBIR put pca_df.pkl"
os.system(cmd_pca)
print('pca_df.pkl is dumped')

cmd_vptree = "mongofiles -d CBIR put vptree.pkl"
os.system(cmd_vptree)
print('vptree.pkl is dumped')
