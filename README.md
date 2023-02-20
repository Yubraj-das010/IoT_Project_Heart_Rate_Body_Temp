# IoT_Project_Heart_Rate_Body_Temp

Health Monitoring system that would measure and monitor patients' health related data such as body temperature and heart beat using pulse  temperature sensors, & Arduino UNO.

1. IoT_Analysis folder contains all the necessary files for the implemented model hosting. /static/css folder contains the .css file. /templates folder contails index.html file that is used for Health Condition Prediction. Also /templates folder has index_regressor.html file that is used for Heart rate prediction purpose.
2. app.py file has OnevsOne Classifier implemented. OnevsOne Classifier along with Random Forest classifier had the best output to find the healt condition prediction. app_regressor.py file has the code for Linear Regression classifier which helps to predict the Heart Rate.
3. model.pkl & model_regressor.pkl files are the .pkl files which contains the training data of OnevsOne Classifier & Linear Regression Classifier respectively.
4. IoT model implementation.ipynb file has all the models implemented along with the comparison.
5. iot-exploratory-data-analysis.ipynb file contains detailed exploratory data analysis.
6. IoT Circuit Diagram Demo.mp4 is the demo video with explained circuit working principle.
7. IoT Circuit Diagram.jpg is the image file of the built circuit.
