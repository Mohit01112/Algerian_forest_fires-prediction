# 🌲 Algerian Forest Fires Prediction

## 📌 Project Overview
This project focuses on predicting forest fire occurrences in Algeria using historical weather and fire data. By applying machine learning techniques, the system analyzes environmental conditions to determine whether a forest fire is likely to occur.

The project uses the **Algerian Forest Fires Dataset**, which contains data collected from two regions in Algeria (Bejaia and Sidi Bel-Abbes) during the summer months.

---

## 🎯 Project Objectives
- Perform **Exploratory Data Analysis (EDA)** to understand data patterns
- Clean and preprocess the dataset
- Build and evaluate **machine learning models**
- Predict forest fire occurrence based on weather conditions
- Identify key factors contributing to forest fires

---

## 📂 Dataset Description
The dataset contains **244 records** with the following features:

| Feature | Description |
|-------|-------------|
| Temperature | Maximum temperature (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind Speed (km/h) |
| Rain | Rainfall (mm) |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| DC | Drought Code |
| ISI | Initial Spread Index |
| BUI | Buildup Index |
| FWI | Fire Weather Index |
| Classes | Fire / Not Fire (Target Variable) |

---

## 🔍 Exploratory Data Analysis (EDA)
- Checked missing values and data consistency
- Analyzed distributions of weather variables
- Visualized correlations between features
- Identified important factors influencing fire occurrence

Libraries used for EDA:
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🤖 Machine Learning Models Used
- Logistic Regression  
- Random Forest Classifier  

### Workflow:
1. Data cleaning and preprocessing  
2. Feature selection  
3. Train-test split  
4. Model training  
5. Model evaluation  

---

## 📊 Model Evaluation
Models were evaluated using:
- Accuracy score
- Confusion matrix

The Random Forest model showed strong performance in classifying fire and non-fire events.

---

## 🛠 Technologies & Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📁 Project Structure
Algerian_forest_fires-prediction/
│
├── data/ # Dataset files
├── notebooks/ # EDA and model training notebooks
├── models/ # Trained models (if saved)
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Mohit01112/Algerian_forest_fires-prediction
Install dependencies:

pip install -r requirements.txt
Run the Jupyter notebook to explore the analysis and model training.

🔮 Future Enhancements
Deploy the model using Streamlit or Flask

Integrate real-time weather data

Apply advanced models like XGBoost or Deep Learning

Improve model performance with hyperparameter tuning

📚 Conclusion
This project demonstrates how data science and machine learning can be applied to environmental problems like forest fire prediction. The insights gained can help in early detection and prevention strategies.

👨‍💻 Author
Mohit
Artificial Intelligence and Data Science


---


If you want, I can:
- Add **badges** (Python, ML, GitHub)
- Make it **resume-optimized**
- Convert it into a **portfolio description**

Just tell me 👍
