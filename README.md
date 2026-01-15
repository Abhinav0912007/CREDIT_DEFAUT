

---

# Credit Card Default Prediction

## Project Overview

This project aims to predict whether a credit card customer will default on their payment next month based on historical data. The prediction helps banks and financial institutions in risk assessment, improving decision-making for credit approvals, and managing financial losses.

The model is built using **Machine Learning techniques** and is deployed as a **web application** for interactive predictions.

---

## Dataset

The dataset contains information about credit card clients, including demographic data, credit history, payment behavior, and bill statements. Key features include:

* `LIMIT_BAL`: Credit limit (NT dollar)
* `SEX`: Gender (1=male, 2=female)
* `EDUCATION`: Education level
* `MARRIAGE`: Marital status
* `AGE`: Age of the client
* `PAY_0` to `PAY_6`: Repayment status in past months
* `BILL_AMT1` to `BILL_AMT6`: Bill statements for past months
* `PAY_AMT1` to `PAY_AMT6`: Previous payments
* `default.payment.next.month`: Target variable (0=No default, 1=Default)

**Source:** Publicly available credit card dataset (e.g., UCI Machine Learning Repository)

---

## Features

1. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical variables (Label Encoding)
   * Feature scaling (StandardScaler/MinMaxScaler)
   * Train-test split (e.g., 80%-20%)

2. **Exploratory Data Analysis (EDA)**

   * Visualization of distribution of features
   * Correlation analysis
   * Identifying patterns in default behavior

3. **Machine Learning Models**

   * Logistic Regression
   * Decision Tree
   * Random Forest
   * XGBoost (optional)
   * Model evaluation using accuracy, precision, recall, F1-score, and ROC-AUC

4. **Model Deployment**

   * Flask or Streamlit web app for predicting credit default
   * Users can input client data and get prediction (Default / No Default)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd credit-default-prediction
```

2. Create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the web application:

```bash
streamlit run app.py
# or for Flask
python app.py
```

2. Input customer details in the interface.

3. Get prediction:

   * **0** → No Default
   * **1** → Default

---

## Evaluation Metrics

* Accuracy: Measures overall correctness
* Precision: Correctness of predicted defaults
* Recall: Ability to detect actual defaults
* F1-score: Balance between precision and recall
* ROC-AUC: Overall model performance

---

## Folder Structure

```
credit-default-prediction/
│
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks for EDA & modeling
├── models/                # Saved trained models
├── app.py                 # Flask or Streamlit app
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Future Enhancements

* Add **Hyperparameter tuning** for better model performance
* Integrate **real-time API** for automatic predictions
* Add **feature importance dashboard** for explainability

---

## Authors

* **Abhinav Singh** – [Your GitHub Profile](https://github.com/yourprofile)

---

## License

This project is licensed under the MIT License.

---

If you want, I can also generate a **ready-to-use `requirements.txt`** file and a **Streamlit-ready `app.py`** template for your credit default project.

Do you want me to do that?

