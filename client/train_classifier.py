import pickle
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data_dict = pickle.load(open('../models/data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# split data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# predict
y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly !'.format(str(score * 100)))

# save model
f = open('../models/model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()