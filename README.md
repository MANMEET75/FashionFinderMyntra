# FashionFinderMyntra - Content Based Recommendation System

## Research Environment
In the Research environment, I collected a dataset from Kaggle. To ensure data quality, I performed essential data preprocessing tasks, including handling missing values, removing duplicates, and eliminating unnecessary HTML elements from features using regular expressions and Python. Subsequently, I created a dataframe containing only with the relevant features required for my recommendation system.

To enhance text analysis, I employed the NLTK library for stemming, which aids in reducing words to their root form. Additionally, I utilized the CountVectorizer from scikit-learn to determine the frequency of occurrences for each word or token in the dataset. This step is crucial for building a content-based recommendation system.

To measure the similarity between documents based on their content, I employed cosine similarity. This metric helps determine the resemblance between two documents, which is vital for our recommendation system.

After implementing the recommendation function, I saved the necessary files as pickle files using the pickle module. These files will be utilized in creating a web application in the development environment, ensuring a smooth and interactive user experience.

[I invite you to explore the research environment.](https://github.com/MANMEET75/FashionFinderMyntra/blob/main/Myntra%20Fashion%20Product%20Content%20Based%20Recommendation%20System.ipynb)


## Development Environment
In the Development environment, I crafted a highly interactive web application utilizing Flask as the backend framework. Leveraging my web development expertise, I designed a visually appealing user interface inspired by Myntra's official website. To achieve this, I employed HTML, CSS, Bootstrap, and JavaScript. By integrating Flask, I seamlessly incorporated my FashionFinderMyntra recommendation system into the application's backend.

To facilitate collaboration with team members, I initiated a repository on GitHub, adhering to best practices. Additionally, I established a virtual environment using Anaconda, ensuring a clean and isolated development environment. Within this environment, I created various files, such as setup.py to store metadata, requirements.txt to document package dependencies, and directories like templates and static for constructing a dynamic and engaging user interface. Moreover, I utilized .gitignore to exclude certain files, such as the virtual environment folder and data folder, from version control.

Overall, by employing Flask and integrating frontend technologies, I created an immersive web application with an interactive UI, closely resembling Myntra's official website. The project's well-organized structure, collaboration-ready repository, and usage of a virtual environment contribute to a streamlined and efficient development process.

## Please take a look at the elegantly designed user interface of Myntra, which I have created utilizing my web development expertise.
```bash
https://replit.com/@MANMEET75/WrithingImaginaryInstitutions-1?v=1
```

## Let's put our recommendation system to the test!
<img src="appdemo.gif" alt="testing-of-recommendation-system">


## Here are some ways you can use this model to improve the business and increase profit:
The content-based recommendation system that I have developed using the Myntra dataset for women can significantly contribute to the growth of Myntra company. Here's how it can help:

1) Enhanced Customer Experience: By employing advanced data preprocessing techniques and leveraging the power of text analysis, the recommendation system can deliver accurate and relevant product suggestions. This helps users in discovering new and trendy items that align with their preferences, ultimately enhancing their overall shopping experience on Myntra.

2) Increased User Engagement: The highly interactive web application I've developed, featuring a visually appealing user interface reminiscent of Myntra's official website, creates an immersive experience for users. This captivating platform keeps users engaged, increasing their time spent on the website and reducing bounce rates. This, in turn, leads to improved customer retention and loyalty.

3) Competitive Advantage: Implementing a content-based recommendation system with a focus on women's fashion provides Myntra with a unique selling point. It sets them apart from competitors by offering a highly tailored and curated selection of products that resonate with their female customer base. This differentiation strengthens Myntra's position in the market and attracts new customers.

4) Data-Driven Insights: The recommendation system generates valuable insights into customer behavior and preferences. Myntra can leverage this information to make data-driven business decisions, such as identifying popular trends, optimizing inventory management, and tailoring marketing strategies to target specific customer segments effectively.

Overall, the content-based recommendation system I have developed can help Myntra drive growth by providing personalized recommendations, increasing user engagement, enhancing the customer experience, gaining a competitive edge, and leveraging valuable data-driven insights.


## To utilize the recommendation system on your local system, kindly follow the provided instructions.

1) To proceed, open the command prompt on your system and navigate to the desired directory where you wish to store the model. Then, execute the following command.
```bash
git clone https://github.com/MANMEET75/FashionFinderMyntra.git
```

2) Kindly download the "similarity.pkl" file from the provided link, as it exceeds the file size limit for GitHub storage.
```bash
https://drive.google.com/file/d/1TiME7B9SpiMz6p-UtWzyYRYuKefup4Tj/view?usp=share_link
```
3) Please open your preferred integrated development environment (IDE), such as PyCharm or Visual Studio Code (VScode). For optimal performance, we recommend using VScode. Once opened, navigate to the "artifacts" folder within the IDE and paste the "similarity.pkl" file into it.
4) To create and activate the virtual environment, execute the provided command in your command prompt.
```bash
cd FashionFinderMyntra
py -3 -m venv venv
venv\Scripts\activate

```
5) Install all the necessary packages and libraries by executing the following pip command.
```bash
pip install -r requirements.txt
```
7) To utilize the recommendation system, simply enter the command "python app.py" in your command prompt.
```bash
python app.py
```


Enjoy Coding!!
