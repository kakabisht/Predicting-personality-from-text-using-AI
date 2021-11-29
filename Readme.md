This repository contains machine learning and deep learning algorithms used to predict personality of a person using text. We used MBTI Personality types,

1. Introversion vs extroversion (I vs E)
2. Sensing vs intuition (S vs N)
3. Thinking vs feeling (T vs F)
4. Perception vs judging (P vs J)

### Various Machine learning algorithms, we implemented

1. Logistic regression: 62 % accuracy
2. Support vector Classifier: 64 % accuracy
3. XGBoost Classifier: 66 % accuracy
4. CatBoost Classifier: 67 % accuracy

We then used We use a distilled version of the BERT base model. As BERT uses bidirectionaltraining of Transformer. The accuracy is not great, as the dataset is very imbalanced. As some personality types are more rare than other personality types such as ESFJ or ESTJ . Which causes it to be an overfitted model. Hence, the difference between training score and testing score is significant.

### We used Flask framework, to create an API from our Model by using Model.pickle file in our code.

To run and test our application ,

1. cd API
2. run python app.py (This is now the server)
3. You could either use postman or test.py to send data, just remember to change the content in test.py
