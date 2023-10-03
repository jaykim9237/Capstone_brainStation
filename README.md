# Apartment Building Standartds in Toronto (RentSafeTO)

## About Project
Predicting RentSafeTO: A Machine Learning Solution for Safer Housing Evaluation

## Team
- Author : Hyunjung Kim
- Date : JUL 23, 2023 ~ Sep 9, 2023
- Affiliatoin : brainStation

## Index
**1. Introduction**
 -  Introduction
 -  Big Idea
 -  Impact

**2. RentSafeTO**
 - What is RentSafeTO (will contain when why who)
 - Evaluation Categories
 - Audits
 - Fine

**3. Analytical data**
 - Data Source
 - Data Shape Analysis
 - Data thresholds

**4. Models**
 - Model Methods
 - Model Conclusion

**5. Conclusions**
 - Conclusion
 - Threshholds

 ----

## 1. Introduction

**1) Introductio**<br>
In the ever-evolving landscape of real estate, ensuring the safety and security of residential buildings is of paramount importance for both tenants and prospective property owners. With the aim of providing a reliable and proactive approach to building safety evaluation, our capstone project focuses on predicting RentSafeTO - an innovative solution that leverages the power of machine learning to forecast the safety assessment of apartment buildings in Toronto.

Aspiring homeowners and current tenants face the challenge of ensuring the safety and well-being of their living spaces. Landlords, too, bear the responsibility of conducting safety inspections regularly. RentSafeTO aims to revolutionize this process by offering a predictive model that anticipates the outcomes of safety inspections before they even take place, empowering all stakeholders with valuable insights.

**2) The Big Idea**<br>
The core concept behind RentSafeTO revolves around analyzing the correlation between various factors and building safety. By considering crucial variables such as building height (number of floors), construction year, acceptable population density, the presence of laundry facilities, and garbage disposal units, our predictive model aims to forecast the potential outcomes of safety evaluations.

**3) The Impact**<br>
The impact of RentSafeTO extends to multiple stakeholders in the real estate realm. Prospective property buyers seeking to make informed decisions can benefit from a comprehensive risk assessment before purchasing an apartment building. Current tenants planning to move to new residences can access valuable safety information, helping them choose safer living environments. Moreover, landlords can proactively address any potential safety concerns, fostering a more secure and transparent rental market.

By harnessing the power of machine learning and data analysis, RentSafeTO streamlines the evaluation process, reducing the time taken to receive safety test results. This efficiency not only saves time and resources but also ensures timely actions to address any identified safety issues, ultimately contributing to the overall well-being of residents.

## 2. RentSafeTO

RentSafeTO is a comprehensive program introduced by the City of Toronto to ensure the safety and quality of rental apartment buildings within the city. The program aims to protect the rights and well-being of tenants while also holding landlords accountable for maintaining safe and habitable living conditions. RentSafeTO encompasses a range of initiatives and evaluations that help identify and address potential issues in rental properties, enhancing the overall living experience for tenants.

**1) What is RentSafeTO**<br>
    a. When: RentSafeTO was introduced as part of the city's ongoing efforts to improve rental housing standards and address concerns related to building safety and tenant welfare.

    b. Why: The program was launched to respond to the increasing demand for rental properties in Toronto, particularly after the post-COVID-19 surge in housing prices. As more people opt for rental housing, ensuring the safety and livability of rental units has become crucial.

    c. Who: RentSafeTO is designed to benefit both tenants and landlords. It aims to provide tenants with safe, healthy, and well-maintained living spaces while helping landlords meet their responsibilities in maintaining high-quality rental properties.

**2) Evaluation Categories**<br>
The RentSafeTO evaluation process covers various aspects of rental buildings to ensure they meet the city's safety and maintenance standards. Some of the key evaluation categories include:<br>

    a. Building Safety: This category assesses the overall safety features of the building, including fire safety measures, structural integrity, and emergency exits.

    b. Maintenance and Repairs: Evaluators inspect the condition of the building and its amenities to check for any necessary repairs or maintenance requirements.

    c. Pest Control: The presence of pests can significantly impact the living conditions. This evaluation category assesses the effectiveness of pest control measures.

    d. Waste Management: Evaluators check the availability and proper functioning of waste disposal facilities, promoting cleanliness and hygiene within the building.

    e. Security: The evaluation includes examining security features such as locks, intercoms, and surveillance systems to enhance the safety and security of residents.

**3) Audits**<br>
Under RentSafeTO, regular audits are conducted on rental properties to ensure ongoing compliance with safety and maintenance standards. These audits help identify any issues or violations that need to be addressed by landlords promptly. The frequency of audits may vary based on various factors, including the building's history of compliance and the severity of any previous violations.

**4) Fine**<br>
In cases where landlords fail to meet the required safety and maintenance standards, fines and penalties may be imposed. The fines are meant to incentivize landlords to take the necessary actions to rectify any issues and maintain a safe and healthy living environment for their tenants.

RentSafeTO plays a vital role in protecting the rights and well-being of tenants while promoting responsible landlord practices. By ensuring rental buildings meet high standards of safety and maintenance, the program contributes to a healthier and more sustainable rental housing market in Toronto.

For more detailed information about RentSafeTO, you can refer to the official website: https://www.toronto.ca/community-people/housing-shelter/rental-housing-tenant-information/rental-housing-standards/apartment-building-standards/

## 3. Analytical data

**1) The Data Source**<br>
Our project relies on the rich dataset provided by the Toronto open data site, encompassing a diverse range of variables related to apartment building evaluations. By analyzing this comprehensive dataset, we aim to unearth hidden patterns and correlations, enabling our predictive model to make accurate assessments of building safety.

**2) Data Shape Analysis**<br>
The dataset comprises 11,760 rows and 40 columns. This dataset is characterized by a substantial number of rows and columns, with various data types (integers, floats, and objects) representing different aspects of the buildings and properties under evaluation.

**3) Data thresholds**<br>
It is important to note that the dataset contains missing values (NaN) in several columns, which may affect the quality of predictions. Additionally, the dataset undergoes regular updates, leading to potential challenges for predictive modeling due to evolving column names and potential changes in data distribution over time.

## 4. Models

**1) Model Methods**<br>
- Linear Regression Model:

R-squared: 0.98<br>
Mean Absolute Error: 8.15<br>
Mean Squared Error: 100.26<br>
Root Mean Squared Error (RMSE): 10.01<br>

- Random Forest Regression Model:

R-squared: 0.96<br>
Mean Absolute Error: 1.53<br>
Mean Squared Error: 4.18<br>
RMSE: 2.04<br>

- Decision Tree with SMOTE (Synthetic Minority Over-sampling Technique):

Accuracy: 0.8256387270282385

- K-Nearest Neighbor

Mean Cross-Validation Score: 0.6706<br>
Standard Deviation of Cross-Validation Scores: 0.004265

**2) Model Conclusion**<br>

The analysis employed three different regression models to predict outcomes. The linear regression model achieved a high R-squared value of 0.98, indicating a strong fit to the data. However, it had a relatively higher mean absolute error (MAE) and root mean squared error (RMSE), suggesting some variability in prediction accuracy.

In contrast, the random forest regression model yielded a slightly lower R-squared value of 0.96 but demonstrated lower MAE and RMSE, indicating improved prediction accuracy.

Lastly, the decision tree model, enhanced with SMOTE to address data imbalance, achieved an accuracy of 0.83. The classification report shows that it performed well in classifying different categories, especially for class 3.

Additionally, the K-Nearest Neighbors (KNN) model was evaluated using cross-validation, resulting in a mean cross-validation score of 0.6706380968239112 with a standard deviation of 0.0042657268177913295.

## 5. Conclusions
**1) Conclusion**<br>
In the dataset, there is a specific sample that consistently scored 3 points in all evaluations, resulting in a perfect evaluation score of 100. This seems to go beyond a mere calculation of evaluation indices and likely reflects considerations related to the registration year, building year, and location. However, in the regression model, machine learning appears to have generated its own formula, resulting in an exceptionally high accuracy that may seem more like a perfect match than a prediction.

As a result, in this particular case, it can be argued that a classification model is more appropriate for making predictions. Among the classification models, the decision tree model stands out as the most accurate option and is, therefore, the preferred choice for our analysis.

**2) Threshholds**<br>
Logistic regression is indeed known as a powerful classification model. However, in our specific case, the binary classification approach presented challenges due to the extremely low occurrence rate of cases where evaluations resulted in disqualification (approximately 1%). This imbalance in the dataset made it difficult to effectively use logistic regression as it tends to perform poorly when the classes are heavily imbalanced.

To address this data imbalance issue, we employed SMOTE (Synthetic Minority Over-sampling Technique). While it helped improve the model's performance, it still faced challenges in handling the imbalance effectively.

It's important to note that having more data related to disqualifications, if collected in future research, could lead to better results. This would allow for a more balanced dataset and potentially enhance the performance of classification models like logistic regression.
