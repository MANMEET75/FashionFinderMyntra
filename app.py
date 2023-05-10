# import pickle
# import streamlit as st
# import pandas as pd
# import requests


# def recommend(name):
#     index = new_df[new_df['name'] == name].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_product_names = []
#     recommended_product_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         # movie_id = new_df.iloc[i[0]].movie_id
#         recommended_product_posters.append(new_df.iloc[i[0]][2])
#         recommended_product_names.append(new_df.iloc[i[0]][1])

#     return recommended_product_names,recommended_product_posters


# st.header('Myntra Fashion Product Recommendation System')

# new_df = pd.read_pickle(open('artifacts/product_list.pkl','rb'))
# similarity = pd.read_pickle(open('artifacts/similarity.pkl','rb'))


# product_list = new_df['name'].values

# selected_movie = st.selectbox(
#     "Type or select a product from the dropdown",
#     product_list
# )

# if st.button('Show Recommendation'):
#     recommended_product_names,recommended_product_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_product_names[0])
#         st.image(recommended_product_posters[0])
#     with col2:
#         st.text(recommended_product_names[1])
#         st.image(recommended_product_posters[1])

#     with col3:
#         st.text(recommended_product_names[2])
#         st.image(recommended_product_posters[2])
#     with col4:
#         st.text(recommended_product_names[3])
#         st.image(recommended_product_posters[3])
#     with col5:
#         st.text(recommended_product_names[4])
#         st.image(recommended_product_posters[4])


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






