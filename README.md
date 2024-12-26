# Stock Analysis Tool

## Overview
The Stock Analysis Tool is a powerful application designed to analyze stock price data using advanced machine learning techniques, specifically Long Short-Term Memory (LSTM) networks. This tool allows users to fetch, clean, and visualize stock data, providing insights into stock price trends and predictions.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Parameters](#model-parameters)
- [Data Cleaning](#data-cleaning)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Fetch stock data from Yahoo Finance.
- Clean and preprocess data by removing missing values and outliers.
- Train an LSTM model to predict stock prices.
- Visualize training and testing results with interactive plots.
- User-friendly interface built with Streamlit.

## Technologies Used
- **Python**: The primary programming language used for development.
- **Streamlit**: For creating the web application interface.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For data preprocessing and model evaluation.
- **TensorFlow**: For building and training the LSTM model.
- **yfinance**: For fetching stock data from Yahoo Finance.

## Installation
To set up the Stock Analysis Tool on your local machine, follow these steps:

1. **Clone the repository:**
   - Clone the repository using the command: `git clone https://github.com/yourusername/Stock-Analysis-Tool.git`
   - Navigate into the cloned directory: `cd Stock-Analysis-Tool`

2. **Create a virtual environment (optional but recommended):**
   - Create a virtual environment using the command: `python -m venv venv`
   - Activate the virtual environment. On macOS/Linux, use: `source venv/bin/activate`. On Windows, use: `venv\Scripts\activate`.

3. **Install the required packages:**
   - Install the required packages using the command: `pip install -r requirements.txt`

## Usage
Run the application:
- Use the command: `streamlit run app.py`
- Access the application by opening your web browser and going to `http://localhost:8501`.

### Input Parameters:
- Enter the company name (ticker symbol).
- Select the start and end dates for the data.
- Adjust model parameters such as time step, number of epochs, and learning rate.

### Actions:
- Click "Get Data" to fetch stock data.
- Click "Clean Data" to preprocess the data.
- Click "Save Cleaned Data" to save the cleaned dataset.
- Select data for analysis and click "Analyze" to train the model and visualize results.

## Model Parameters
- **Time Step**: The number of previous time steps to consider for predicting the next value.
- **Number of Epochs**: The number of times the model will iterate over the training dataset.
- **Learning Rate**: The step size at each iteration while moving toward a minimum of the loss function.

## Data Cleaning
The application includes a robust data cleaning process that:
- Drops missing values.
- Removes outliers using the Interquartile Range (IQR) method.

## Contributing
Contributions are welcome! If you would like to contribute to the Stock Analysis Tool, please follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or feedback, please contact:
- **Lunaris**: lunaris4452@gmail.com
- **GitHub**: Lunaris

Thank you for using the Stock Analysis Tool! We hope it helps you gain valuable insights into stock market trends.
