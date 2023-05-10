import pickle
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

from flask import send_from_directory

@app.route('/images/<path:image_filename>')
def serve_image(image_filename):
    return send_from_directory('static/images', image_filename)

def recommend(name):
   
        index = new_df[new_df['name'] == name].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_product_names = []
        recommended_product_posters = []
        for i in distances[1:6]:
            recommended_product_posters.append(new_df.iloc[i[0]][2])
            recommended_product_names.append(new_df.iloc[i[0]][1])

        return recommended_product_names, recommended_product_posters


@app.route("/index.html")
def recommendAgain():
    return render_template('index.html', product_list=product_list)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_products = request.form['selected_products']
        recommended_product_names, recommended_product_posters = recommend(selected_products)

        return render_template('recommendation.html', names=recommended_product_names, posters=recommended_product_posters)
    else:
        return render_template('index.html', product_list=product_list)

if __name__ == '__main__':
    new_df = pd.read_pickle(open('artifacts/product_list.pkl', 'rb'))
    similarity = pd.read_pickle(open('artifacts/similarity.pkl', 'rb'))
    # num_values = 14264
    product_list = new_df['name'].values[:14000]
    app.run(debug=True)






