# MFE Applied Financial Project
In this project, we would like to use data to predict the defaulting of consumer. The
methodologies we may use include linear regression, logistic regression, neutral
network and support vector machine. 

# Current Achivement
1. clean data and seperate to training data and testing data
2. run logistic regression on training data, the accuracy on training is about 0.74 and
the accuracy on testing data is about 0.65.
3. reduce feature according to the f value and reduce it to 50 features. The accuracy 
becomes about 0.71.
4. run random forest on training dataset and the accuracy is about 0.65
5. use 10 fold cross validation for logistic regression and the accuracy is about 0.71 when 
we reduce the feature size to around 100
6. before using logistic regression we normalize the data which means that for each feature
we minus the value by mean of the feature and devided by sd of the feature.
7. after normalization, the accuracy of using all data becomes 0.77 and the AUC is about 0.73.
you can see the result from logistic_regression_ROC.ipynb or html file. 
8. We try to use feature selection by the build-in library or PCA method. None of the methods
can increase the accuracy and AUC.
9. The best AUC we get is about 0.730 and the accuracy is 0.769.

# Future improvement
1. we may try higher order feature or interactive features.
2. compared with the article in literature review, the AUC he got for logistic regression is 
0.779 and used about 25000 data point. Therefore, it's reasonable that the AUC we got is smaller 
than him because we have only about 3000 data point after we deleted the data with null value. In 
Order to solve this problem, we may require more data point.
3. we may apply other techniques in machine learning
# ML_Project
