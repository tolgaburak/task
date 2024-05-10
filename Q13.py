import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



# Veri seti
data = pd.read_csv("dataset.csv")
print("Veri setinin ilk birkaç satırı:\n", data.head())
print("\nVeri setinin temel istatistikleri:\n", data.describe())
print("\nEksik değerlerin sayısı:\n", data.isnull().sum())
data.fillna(data.mean(), inplace=True)


plt.figure(figsize=(8, 6))
data['isVirus'].value_counts().plot(kind='bar', color=['skyblue', 'orange'])
plt.title('Sınıf Dağılımı')
plt.xlabel('Etiket')
plt.ylabel('Sayı')
plt.xticks(rotation=0)
plt.show()


data.hist(figsize=(10, 8))
plt.suptitle('Özelliklerin Dağılımı')
plt.show()


X = data.iloc[:, :-1]
y = data.iloc[:, -1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nDoğruluk: {:.2f}%".format(accuracy * 100))

conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred))

# Tahmin edilen değerlerin dağılımı
y_pred = y_pred.astype(int)
plt.figure(figsize=(8, 6))
plt.hist(y_pred, bins=2, color='skyblue', alpha=0.7)
plt.title('Tahmin Edilen Değerlerin Dağılımı')
plt.xlabel('Etiket')
plt.ylabel('Sayı')
plt.xticks([0.25, 0.75], ['Not a Virus', 'Virus'])
plt.show()

# Confusion matrix
plt.figure(figsize=(6, 4))
plt.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.7)
plt.title('Confusion Matrix')
plt.xlabel('Tahmin Edilen Etiket')
plt.ylabel('Gerçek Etiket')
plt.colorbar()
plt.show()

