from flask import Flask, render_template, request
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# # Load the music.csv file
# file_path =  r'C:\Users\Vengatesan B\OneDrive\vengatesan-Devops\OneDrive\Desktop\InternalWorks\AI\PraticesOfAI\Music_gener\Dataset\music.csv'
# music_table = pd.read_csv(file_path)

# # Assuming 'genre' is the target variable
# X = music_table.drop(columns=['genre'])
# y = music_table['genre']

# # Create a LabelEncoder instance for 'gender'
# label_encoder_gender = LabelEncoder()

# # Encode 'gender' column
# X['gender'] = label_encoder_gender.fit_transform(X['gender'])

# # Initialize the Decision Tree Classifier
# model_alg = DecisionTreeClassifier()

# # Fit the model on the training data
# model_alg.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input features from the form
#         age = float(request.form['Age'])
#         gender = request.form['Gender']

#         # Check if age is positive
#         if age <= 0:
#             return render_template('index.html', prediction='Error: Age must be a non-negative number')

#         # Encode 'gender'
#         gender_encoded = label_encoder_gender.transform([gender])[0]

#         # Make a prediction
#         prediction = model_alg.predict([[age, gender_encoded]])

#         # Return the prediction result
#         return render_template('index.html', prediction=f'The predicted genre is: {prediction[0]}')

#     except ValueError:
#         return render_template('index.html', prediction='Error: Please enter a valid numeric value for age')
#     except Exception as e:
#         return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
