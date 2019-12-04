# Prudential Insurance Assessment
By Alvaro Amos H, Reynold Vinson, and Winly Williamdy

## Background
This repository is an attempt as well as a student project aimed to complete [a challenge posted on Kaggle with a similar title](https://www.kaggle.com/c/prudential-life-insurance-assessment/overview) . The challenge asks programmers to attempt to create a program that allows a prediction of responses from a given data set by creating and using statistical models. The challenge comes from a real life problem in which people in the US are turned off by the fact that identifying risk classifications and eligibility of applicants takes too much time to process. As such, the model aims to be able to predict the life insurance plan suitable for any applicant without needing as much time.

## Getting Started
This program uses the following programs to run:
- [Jupyter Notebook](https://jupyter.org/)
- [Python](https://www.python.org/downloads/) 
- [Dash](https://pypi.org/project/dash/) 

## Layout
![layout](https://github.com/reynoldvinson/prudential-insurance-assessment/blob/master/Dash%20Layout.png)
User expected to input their information then pressing the `See the Results` button to find out the prediction result.

## Data Cleansing
The data sets consists of 128 columns which represent various inputs and variables concerning the applicant. This includes age, weight, height, BMI, medical history, family data, and employment info. The columns can roughly be categorized as the following:

- Product Information ('A set of normalized variables relating to the product applied for')
- Personal Details (Age, Height, Weight, and BMI)
- Employment Information (Normalized variables relating to the employment of the applicant)
- Other Insured Information (Other variables relating to the applicant)
- Family History (Normalized variables related to the family of the applicant)
- Medical History (Normalized variables related to the personal medical history of the applicant)
- Medical Keywords (Dummy variables relating to the medical history of the applicant)

A problem arises in understanding the data sets given, since most of the data are either already normalized or are given without any background. This results in a vague understanding of the problem itself, particularly the variables given for us to use. As such, some assumptions are logically made and some exploratory data analyses are also done to better understand the problem at hand. Furthermore, in trying to make a simple interactive program for the purpose of learning, we simplified the columns to just consist of 10 columns, each representing a certain variable group from the original 128 columns. The responses are also simplified by changing the mulitclass characteristic of the problem into a binary problem. Further assumptions and simplifications can be read in the accompanying files.

## Modeling
Several models are used in initial phases of modelling. This includes random forest, decision tree, and SVM that is contained in `sklearn` library. However, after observing the various degrees of accuracy and precision of the models, it is decided that the `Random Forest` model will be used for the final program that will be used by the users because `Random Forest` yield a similar performance compared with other models. The performance for each models are also evaluated using `sklearn.metric` library which shows the model's accuracy, precission, f1-score and support. The confusion matrix for each models can also be viewed using `confusing_matrix` inside `sklearn.metrics library`. After fitting models for prediction, the models than saved into a `pickle` which can be called on `Dash`. All the `pickle` file can be found at `pickle_file`.

## Visualisation
Prediction visualisation developed using [Dash](https://plot.ly/dash/). `layout`,`components`, and `pickle` are integrated into one file `main.py`.

After running `main.py`, you will see this in your command prompt and will directed to the layout.
> Running on http://127.0.0.1:8050/
> Debugger PIN: 440-697-358
>  * Serving Flask app "main" (lazy loading)
>  * Environment: production
>    WARNING: This is a development server. Do not use it in a production deployment.
>    Use a production WSGI server instead.
>  * Debug mode: on
> Running on http://127.0.0.1:8050/
> Debugger PIN: 879-897-858

