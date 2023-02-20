import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import train_test_split
import pickle
df = pd.read_csv('Maternal Health Risk Data Set.csv')
print(df.head())
X = df.drop('RiskLevel', axis=1)

y = df['RiskLevel']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
classifier = RandomForestClassifier()
ovo = OneVsOneClassifier(classifier)
ovo.fit(X_train, y_train)
pickle.dump(ovo, open("model.pkl", "wb"))

ovo_predictions = ovo.predict(X_test)

# accuracy on X_test
#accuracy = ovo.score(X_test, y_test)
#print(accuracy)

# creating a confusion matrix
#cm = confusion_matrix(y_test, gnb_predictions)