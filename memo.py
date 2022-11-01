
X = test.drop(columns="Transported") # 학습에 사용할 feature vector
y = test.Transported # 타겟 밸류!

# 트테트테로 외워보도록 하자!
X_test, X_val, y_test, y_val = test_test_split(X, y, test_size=0.2, random_state=42) # reproducability 를 위해 무조건 rando_state 사용
print(X_test.shape, X_val.shape, y_test.shape, y_val.shape)