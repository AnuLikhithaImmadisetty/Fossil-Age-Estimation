# Fossil Age Estimation" 🌍🦴
Welcome to the "Fossil Age Estimation" Repository! Here, we've explored around 4 machine learning models to predict fossil ages, utilizing a diverse set of geological and biological features! This project demonstrates the power of different machine learning techniques in estimating the age of fossils with remarkable precision, contributing to the understanding of Earth's ancient history.

Dive in to discover the models, analyses, and insights that emerged from this fascinating exploration!

## Table of Contents 
 - [Overview](#overview)
 - [Project Structure](#project-structure)
 - [Dataset and Description](#dataset-and-description)
 - [Features](#features)
 - [Tools and Technologies](#tools-and-technologies)
 - [Results](#results)
 - [Getting Started](#getting-started)
 - [Usage](#usage)
 - [Contributing](#contributing)
 - [License](#license)

## Overview 
In the intricate world of paleontology, estimating fossil ages with precision is crucial for understanding Earth's ancient history. The **Fossil Age Estimation** project leverages advanced machine learning techniques to predict the ages of fossils based on a diverse set of geological and biological features. This project aims to analyze these characteristics, identify key factors influencing fossil dating, and develop a predictive model capable of forecasting fossil ages with high accuracy. By combining data-driven insights with scientific inquiry, this project supports researchers in uncovering the timeline of life on Earth.

## Project Structure 
Here's an overview of the project's structure
```bash
│
├── Datasets/ : Contains datasets used for training, validation and testing.
├── Models/ : Code snippets for preprocessing, model training and evaluation.
├── Results/ : Contains output screenshots of performance metrics.
├── README.md : Explains an overview of the repository.
└── requirements.txt : Required the list of dependencies for this project.
```

## Dataset and Description 
This dataset consists of 24 columns and records the details of fossil specimens, with 9302 observations, representing a variety of geological and biological characteristics. The data captures vital attributes such as geographic locations, taxonomic classifications, dating techniques, and various stratigraphic and taphonomic details, all contributing to estimating fossil ages accurately.

The [Dataset](https://github.com/AnuLikithaImmadisetty/Fossil-Age-Estimation/blob/main/Datasets/fossil_data.csv) is available here! Below are the Descriptions of the columns available in the dataset:

- **ID:** A unique identifier assigned to each fossil specimen.
- **Latitude:** Latitude coordinates indicating the north-south position where the fossil was discovered.
- **Longitude:** Longitude coordinates indicating the east-west position of the fossil discovery.
- **Genus:** The genus classification of the fossilized organism.
- **Species:** The species classification of the fossilized organism.
- **Family:** The family to which the fossilized organism belongs.
- **Class:** The class of the fossilized organism in the biological taxonomy.
- **Infra-Class:** A subclassification within the broader class of the organism.
- **Order:** The order in the taxonomic hierarchy of the fossilized organism.
- **Status:** The current research status of the fossil specimen (e.g., whether it has been confirmed, pending, etc.).
- **Megafauna:** A binary indicator (Yes/No) showing whether the fossil belongs to a megafauna species.
- **Age ID:** A unique identifier for the fossil's estimated age.
- **Dated Remain:** The specific fossil remain that was dated (e.g., bone, tooth, etc.).
- **Dated Material:** The type of material that was used to determine the fossil’s age.
- **Age:** The estimated age of the fossil, usually in years.
- **Age Type:** The classification of the age (e.g., estimated, exact, etc.).
- **Dating Technique:** The technique used to date the fossil (e.g., radiocarbon dating, stratigraphy).
- **Overall Region:**  The broad geographic region where the fossil was discovered.
- **Administrative Division:** The administrative region or division (e.g., country, state) where the fossil was found.
- **Specific Region:** A more precise geographical description of where the fossil was located.
- **Cave/Site/Deposit:** The cave, site, or deposit in which the fossil was discovered.
- **Chamber/Provenance:** Specific chamber or location within the site from where the fossil was excavated.
- **Stratigraphy/Taphonomy:** Details about the fossil’s stratigraphy or taphonomic history.
- **Species abundances:** The number of fossils or abundance of the species in the excavation site.
- **Year:** The year the fossil was excavated or analyzed.
  
## Features 
The Fossil Age Estimation project incorporates the following components:
1. **🧪 Data Analysis**: Analyze fossil datasets to extract meaningful features for accurate age prediction.
2. **🧠 Machine Learning Models**: Implement, train, and optimize various around 4 machine learning models to estimate the age of fossils.
3. **📈 Evaluation Metrics**: Evaluate model performance using metrics like RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), R² and Explained Variance.

## Tools and Technologies
This project employs a diverse array of machine learning models to predict fossil ages. 

### Machine Learning Models:

🗳 **LinearRegression:** A fundamental regression technique that models the relationship between input features and a continuous target variable using a linear equation.  
🌳 **Random Forest Regression:** An ensemble method that constructs multiple decision trees and averages their predictions to enhance accuracy and control overfitting.  
🧠 **SVR (Support Vector Regression):** A regression technique that uses support vector machines to fit the best line within a specified margin, capable of handling non-linear relationships.   
🔍 **SVR with GridSearchCV:** A support vector regression model optimized using grid search to find the best hyperparameters for improved predictive performance.   

The [Models](https://github.com/AnuLikithaImmadisetty/Fossil-Age-Estimation/tree/main/Models) used here is available here!

## Results
Refer to the [Results](https://github.com/AnuLikithaImmadisetty/Fossil-Age-Estimation/tree/main/Results) here!

## Getting Started 
To get started with the Fossil Age Estimation project, follow these steps:
1. **Clone the Repository:** Clone the repository to your local machine using Git: (`git clone https://github.com/AnuLikithaImmadisetty/Fossil-Age-Estimation.git`)
2. **Navigate to the Project Directory:** Change to the project directory: (`cd Fossil-Age-Estimation`)
3. **Install Dependencies:** Install the required dependencies using pip: (`pip install -r requirements.txt`)
4. **Prepare the Data:** Download the dataset and place it in the `/Datasets` folder and ensure the data is in the expected format as described in the data documentation.
5. **Run the Analysis:** Open the Jupyter notebooks in Google Collab or Visual Studio Code located in the `/Models` folder, here you can explore various models and run the corresponding scripts to process the data, train the models, and make predictions.
6. **Evaluate the Models:** Review the evaluation metrics and results in the `/Results` folder. Metrics which will analyze the performance of the models.
  
## Usage 
To use the trained models for **Fossil Age Estimation**🌍:
1. Format and preprocess your text data to align with the training data specifications.
2. Utilize the provided notebooks in the `/Models` directory to load the trained model and generate predictions.
3. Examine the output to identify the age of the fossils.

## Contributing 
Contributions are welcome to this project. To contribute, please follow these steps:
1. Fork the Repository.
2. Create a New Branch (`git checkout -b feature/YourFeature`).
3. Make Your Changes.
4. Commit Your Changes (`git commit -m 'Add new feature'`).
5. Push to the Branch (`git push origin feature/YourFeature`).
6. Create a Pull Request.

## License 
This project is licensed under the MIT License. Refer to the LICENSE file included in the repository for details.
