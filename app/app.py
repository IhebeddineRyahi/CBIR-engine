from flask import Flask, render_template, request, jsonify
import pickle
from pymongo import MongoClient
import gridfs
import time
import numpy as np
import codecs

#Define distance function
def euclidean(p1, p2):
  return np.sum(np.abs(p2 - p1))


#Connect to database
MongoURL = 'mongodb://localhost:27017/' #HERE YOU SPECIFY YOUR MONGODB URL
db = MongoClient(MongoURL).CBIR
fs = gridfs.GridFS(db)
print("[INFO] Loading VP-Tree and Principal Components from database...")
start = time.time()
hashes = fs.find_one({'filename': 'pca_df.pkl'})
hashes = pickle.load(hashes)
tree = fs.find_one({'filename': 'vptree.pkl'})
tree = pickle.loads(tree.read())
end = time.time()
print("[INFO] Loading VP-Tree and Principal Components from database took {} seconds".format(end - start))

#Create flask instance
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


#Main route
@app.route('/')
def index():
    return render_template('index.html')

#Search route
@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        RESULTS_ARRAY = []
        #Get image url
        image_url = (request.form.get('img').split('/'))[4]
        print("[INFO] Query Image : " + image_url)

        try:
            qindex = int(image_url.split('.')[0])
            query = hashes.iloc[qindex].values
            print("[INFO] EHD Query : {} ".format(query))
            print("[INFO] Performing search...")
            start = time.time()
            results = tree.get_n_nearest_neighbors(query, 5)
            results = sorted(results)
            end = time.time()
            print("[INFO] Search took {} seconds".format(end - start))

            index = np.zeros(len(results))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            for x in range(0,len(results)):
                index[x] = (hashes.loc[hashes['PC1'] >= results[x][1][0]]).sort_values(by=['PC1']).index[0]
                img = fs.find_one({'filename': str(index[x]).split('.')[0] +'.jpg'})
                img = img.read()
                base64_data = codecs.encode(img, 'base64')
                img = base64_data.decode('utf-8')
                RESULTS_ARRAY.append({"image": str(index[x]).split('.')[0] +'.jpg', "score": str(round(results[x][0],2)), "URL": img})
            #Return results
            return jsonify(results=(RESULTS_ARRAY[:]))
        except:
            return jsonify({"sorry": "Sorry, no results! Please try again."}), 500

#Run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
