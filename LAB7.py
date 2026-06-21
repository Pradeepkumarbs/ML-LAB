import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

glass_df = pd.read_csv('glass.csv')
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

distance_metrics = [
  ('Euclidean', 'minkowski'),
  ('Manhattan', 'manhattan')
]

# ----------- 70-30 Split -----------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

for name, metric in distance_metrics:
  knn = KNeighborsClassifier(n_neighbors=3, metric=metric)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)
  print(f"\n--- Split 70-30 | K=3 | {name} ---")
  print("Accuracy:", accuracy_score(y_test, y_pred))



# ----------- 90-10 Split -----------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

for name, metric in distance_metrics:
  knn = KNeighborsClassifier(n_neighbors=3, metric=metric)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)
  print(f"\n--- Split 90-10 | K=3 | {name} ---")
  print("Accuracy:", accuracy_score(y_test, y_pred))


#b Fruit Dataset
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("fruits.csv")

X = df[['mass', 'color_score']]
y = df['fruit_subtype']

distance_metrics = [
  ('Euclidean', 'minkowski'),
  ('Manhattan', 'manhattan')
]

# ----------- 70-30 Split -----------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)

for name, metric in distance_metrics:
  knn = KNeighborsClassifier(n_neighbors=3, metric=metric)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)
  print(f"\n--- Split 70-30 | K=3 | {name} ---")
  print("Accuracy:", accuracy_score(y_test, y_pred))



# ----------- 90-10 Split (safe stratified size) -----------

desired_test_size = 0.1
min_test_size = y.nunique() / len(y)
safe_test_size = max(desired_test_size, min_test_size)

X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=safe_test_size, random_state=1, stratify=y
)

for name, metric in distance_metrics:
  knn = KNeighborsClassifier(n_neighbors=3, metric=metric)
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)
  print(f"\n--- Split 90-10 | K=3 | {name} ---")
  print("Accuracy:", accuracy_score(y_test, y_pred))
