from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics


from sklearn.svm import SVC

iris = load_iris()

X = iris.data
Y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                            test_size=0.80, random_state=0)

for Model in [GaussianNB, LinearSVC,SVC]:
    clf = Model().fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    print('%s: %s' %
          (Model.__name__, metrics.f1_score(Y_test, y_pred, average="macro")))