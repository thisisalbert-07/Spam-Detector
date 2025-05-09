# Spam Message Classifier Web App

This project is a Django-based web application that classifies input text messages as **Spam** or **Ham** using a **Naive Bayes classifier** trained on an email dataset. The classifier uses scikit-learn's `CountVectorizer` to transform input text into feature vectors and is trained on a labeled dataset of email messages.

## Features

- Web form to enter a message
- Machine learning model to classify the message
- Output label: Spam or Ham
- Built using Django, pandas, scikit-learn

## Project Structure

- `views.py`: Contains the core logic for loading data, training the model, predicting messages, and handling HTTP requests.
- `forms.py`: Defines the `MessageForm` to accept input messages.
- `home.html`: Template to render the form and prediction result.
- `emails.csv`: Dataset used to train the spam classifier.

## Requirements

- Python 3.x
- Django
- pandas
- scikit-learn

You can install the required Python libraries using:

```bash
pip install django pandas scikit-learn
```

## Dataset

The app uses a CSV file named `emails.csv` located at:
```
D:/Programs/emails.csv
```

Make sure to update the path if you move the dataset.

## How to Run

1. Clone the repository.
2. Ensure `emails.csv` is in the correct location.
3. Start the Django server:

```bash
python manage.py runserver
```

4. Open a browser and go to `http://127.0.0.1:8000/`.
5. Enter a message and submit to see if it's spam or not.

## Functionality Overview

- `predictMessage(message)`: Uses the trained model to classify input text.
- `Home(request)`: Handles form rendering and message classification.

## License

This project is open-source and available under the MIT License.
