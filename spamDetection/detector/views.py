from django.shortcuts import render

# Create your views here.

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer # to convert text data to numerical data
from sklearn.model_selection import train_test_split # split data
from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import accuracy_score
from .forms import MessageForm

dataset=pd.read_csv('D:/Programs/emails.csv')

vectorizer=CountVectorizer()
X=vectorizer.fit_transform(dataset['text'])

X_train, X_test, y_train, y_test=train_test_split(X, dataset['spam'], test_size=0.2)

model=MultinomialNB()
model.fit(X_train, y_train)

def predictMessage(message):
    messageVector=vectorizer.transform([message])
    prediction=model.predict(messageVector)
    return 'Spam' if prediction[0]==1 else 'Ham'

def Home(request):
    result=None
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            message=form.cleaned_data['text']
            result=predictMessage(message)

    else:
        form=MessageForm()

    return render(request, 'home.html',{'form': form, 'result': result})