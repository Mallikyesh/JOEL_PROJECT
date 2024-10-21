# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report

# # Load the CSV file into a DataFrame
# df = pd.read_csv('edited3.csv')

# # Display the first few rows of the DataFrame to understand the structure
# print(df.head())

# # Separate the features (X) and the target (y)
# X = df[['N', 'P', 'K', 'temperature', 'ph']]
# y = df['label']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize the feature values (optional but recommended for many algorithms)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train a RandomForestClassifier (you can choose other algorithms as well)
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')
# print('Classification Report:')
# print(classification_report(y_test, y_pred))

# # Save the trained model (optional)
# import joblib
# joblib.dump(model, 'crop_prediction_model.pkl')

################################################### DIFFERENT MODEL TRAINING


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the CSV file into a DataFrame
df = pd.read_csv('edited3.csv')

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Separate the features (X) and the target (y)
X = df[['N', 'P', 'K', 'temperature', 'ph']]
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the feature values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the models
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Support Vector Machine': SVC(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

# Train and evaluate each model, save the best performing one
best_model = None
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'{name} Accuracy: {accuracy:.2f}')
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    print('-' * 60)
    
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save the best model
joblib.dump(best_model, 'best_crop_prediction_model.pkl')
# Save the scaler
joblib.dump(scaler, 'scaler.pkl')
