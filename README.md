# FashionFinderMyntra - Content Based Recommendation System

## Research Environment
In the Research environment, I collected a dataset from Kaggle. To ensure data quality, I performed essential data preprocessing tasks, including handling missing values, removing duplicates, and eliminating unnecessary HTML elements from features using regular expressions and Python. Subsequently, I created a dataframe containing only with the relevant features required for my recommendation system.

To enhance text analysis, I employed the NLTK library for stemming, which aids in reducing words to their root form. Additionally, I utilized the CountVectorizer from scikit-learn to determine the frequency of occurrences for each word or token in the dataset. This step is crucial for building a content-based recommendation system.

To measure the similarity between documents based on their content, I employed cosine similarity. This metric helps determine the resemblance between two documents, which is vital for our recommendation system.

After implementing the recommendation function, I saved the necessary files as pickle files using the pickle module. These files will be utilized in creating a web application in the development environment, ensuring a smooth and interactive user experience.


## Development Environment
In the Development environment, I crafted a highly interactive web application utilizing Flask as the backend framework. Leveraging my web development expertise, I designed a visually appealing user interface inspired by Myntra's official website. To achieve this, I employed HTML, CSS, Bootstrap, and JavaScript. By integrating Flask, I seamlessly incorporated my FashionFinderMyntra recommendation system into the application's backend.

To facilitate collaboration with team members, I initiated a repository on GitHub, adhering to best practices. Additionally, I established a virtual environment using Anaconda, ensuring a clean and isolated development environment. Within this environment, I created various files, such as setup.py to store metadata, requirements.txt to document package dependencies, and directories like templates and static for constructing a dynamic and engaging user interface. Moreover, I utilized .gitignore to exclude certain files, such as the virtual environment folder and data folder, from version control.

Overall, by employing Flask and integrating frontend technologies, I created an immersive web application with an interactive UI, closely resembling Myntra's official website. The project's well-organized structure, collaboration-ready repository, and usage of a virtual environment contribute to a streamlined and efficient development process.
