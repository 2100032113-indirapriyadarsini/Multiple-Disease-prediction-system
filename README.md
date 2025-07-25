# Multiple-Disease-prediction-system

🧑‍⚕️ Multiple Disease Prediction System Using Machine Learning
This project is a Streamlit-based web application that predicts the likelihood of three major diseases — Diabetes, Heart Disease, and Parkinson’s — using pre-trained machine learning models. It provides a user-friendly interface for medical prediction based on health parameters.

📁 About the Project
This project enables real-time health condition predictions for:

Diabetes

Heart Disease

Parkinson’s Disease

Users can input medical data and receive immediate diagnostic results powered by machine learning models.

🧪 Technologies Used
Frontend & Deployment:
Streamlit, Streamlit Option Menu, Base64 (for background image embedding)

Backend ML Models:
Trained using Scikit-learn with algorithms like:

Support Vector Machine (SVM)

Logistic Regression

Languages & Tools:
Python, Pandas, NumPy, Pickle, Anaconda (Spyder IDE), Google Colab (for training & testing)

🧠 Workflow
1. Model Building
Used Google Colab to preprocess data, perform EDA, train ML models, and evaluate accuracy.

Exported trained models as .sav using pickle.

2. Model Deployment
Built the web interface using Streamlit.

Integrated models to handle real-time prediction from user input.

Ran and tested deployment locally using Anaconda Navigator's Spyder IDE.

📊 Prediction Pages
🔹 Diabetes Prediction
Input Features:

Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DPF, Age

Output: Diabetic or Not Diabetic

🔹 Heart Disease Prediction
Input Features:

Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach, Exang, Oldpeak, Slope, CA, Thal

Output: Has Heart Disease or Healthy Heart

🔹 Parkinson’s Prediction
Input Features:

22 biomedical voice measurements like MDVP:Fo(Hz), Shimmer, NHR, RPDE, DFA, etc.

Output: Positive or Negative Parkinson’s result

🌐 How to Run
Clone the repository.

Install dependencies:
pip install streamlit pandas numpy scikit-learn
Place the .sav models in the correct folder (/savedmodels).


streamlit run Mutiple_disease_predcition.py
Enter medical values and get real-time predictions.

🎯 Model Accuracy (Approx.)
Disease	Accuracy (Test Data)
Diabetes	~77%
Heart	~82%
Parkinson’s	~85%

📷 UI Snapshot
Includes a full-screen background image for a better user experience. Powered with base64 embedding in CSS via Streamlit.
