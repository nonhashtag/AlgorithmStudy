import random
import pandas as pd
from typing import TypeVar, List, Tuple
from scratch.statistics import median, standard_deviation, correlation, mean, de_mean
from scratch.linear_algebra import dot, Vector
import random
import tqdm
from scratch.linear_algebra import vector_mean
from scratch.gradient_descent import gradient_step
from scratch.simple_linear_regression import total_sum_of_squares

X = TypeVar('X')  # generic type to represent a data point
Y = TypeVar('Y')  # generic type to represent output variables

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:] #(실습) Make a shallow copy
    cut = int(len(data) * prob) #(실습) Use prob to find a cutoff
    return data[:cut], data[cut:] #(실습) and split the shuffled list there.
'''
data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

# The proportions should be correct
assert len(train) == 750
assert len(test) == 250

# And the original data should be preserved (in some order)
assert sorted(train + test) == data
'''
#
#
#
#

def train_test_split(xs: List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    # Generate the indices and split them.
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)

    return ([xs[i] for i in train_idxs],  # x_train
            [xs[i] for i in test_idxs],   # x_test
            [ys[i] for i in train_idxs],  # y_train
            [ys[i] for i in test_idxs])   # y_test

xs = [x for x in range(20)]  # xs are 1 ... 1000
ys = [2 * x for x in xs]       # each y_i is twice x_i
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)

#print(xs, ys)
#print(x_train, x_test)
#print(y_train, y_test)

'''
def predict(x: Vector, beta: Vector) -> float:
    """assumes that the first element of x is 1"""
    return dot(x, beta)

def error(x: Vector, y: float, beta: Vector) -> float:
    return predict(x, beta) - y

def squared_error(x: Vector, y: float, beta: Vector) -> float:
    return error(x, y, beta) ** 2

def sqerror_gradient(x: Vector, y: float, beta: Vector) -> Vector:
    err = error(x, y, beta)
    return [2 * err * x_i for x_i in x]

def least_squares_fit(xs: List[Vector],
                      ys: List[float],
                      learning_rate: float = 0.001,
                      num_steps: int = 1000,
                      batch_size: int = 1) -> Vector:
    """
    Find the beta that minimizes the sum of squared errors
    assuming the model y = dot(x, beta).
    """
    # Start with a random guess
    guess = [random.random() for _ in xs[0]]

    for _ in tqdm.trange(num_steps, desc="least squares fit"):
        for start in range(0, len(xs), batch_size):
            batch_xs = xs[start:start+batch_size]
            batch_ys = ys[start:start+batch_size]

            gradient = vector_mean([sqerror_gradient(x, y, guess)
                                    for x, y in zip(batch_xs, batch_ys)])
            guess = gradient_step(guess, gradient, -learning_rate)

    return guess


def multiple_r_squared(xs: List[Vector], ys: Vector, beta: Vector) -> float:
    sum_of_squared_errors = sum(error(x, y, beta) ** 2
                                for x, y in zip(xs, ys))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(ys)
'''
def predict(alpha, beta, x_i):  	#선형모델
    return beta * x_i + alpha
def error(alpha, beta, x_i, y_i):	# 모델과 실제의 에러 계산 음수문제
    return predict(alpha, beta, x_i) - y_i
# 최소자승법: 모델과 실제의 에러제곱의 합을 최소로하는 알파, 베타 찾는 방법
def sum_of_sqerrors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

# 최소자승법 계수 구하기: 복잡한 algebra 를 거치면 다음 결과를 얻음
def least_squares_fit(x,y):
    """given training values for x and y,  find the least-squares values of alpha and beta"""
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def total_sum_of_squares(y):
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
    """the fraction of variation in y captured by the model, which equals
    1 - the fraction of variation in y not captured by the model"""
    if(1.0 - (sum_of_sqerrors(alpha, beta, x, y) / total_sum_of_squares(y)))>=0.75:
        print("1등급 R^2")
    elif(1.0 - (sum_of_sqerrors(alpha, beta, x, y) /total_sum_of_squares(y)))>=0.5:
        print("2등급 R^2")
    elif(1.0 - (sum_of_sqerrors(alpha, beta, x, y) /total_sum_of_squares(y)))>=0.25:
        print("3등급 R^2")
    else:
        print("4등급 R^2")
    return 1.0 - (sum_of_sqerrors(alpha, beta, x, y) /
                  total_sum_of_squares(y))

#
#
#
#
#
df = pd.read_csv("data2.csv", encoding='utf-8-sig', parse_dates=True, index_col=0)
df = df.reset_index()


xs = df[["fdust","ozone(ug/m^3)","nd(ug/m^3)","cm(ug/m^3)","sagas(ug/m^3)"]]
xs_list = xs.values.tolist()
fs = df["fdust"]
os = df["ozone(ug/m^3)"]
ns = df["nd(ug/m^3)"]
cs = df["cm(ug/m^3)"]
ss = df["sagas(ug/m^3)"]
ys= df["ufdust"]
ys = ys.values.tolist()
#print(xs_list)
#print(ys_list)
train_ys, test_ys = split_data(ys, 0.7)
train_fs, test_fs = split_data(fs, 0.7)
train_os, test_os = split_data(os, 0.7)
train_ns, test_ns = split_data(ns, 0.7)
train_cs, test_cs = split_data(cs, 0.7)
train_ss, test_ss = split_data(ss, 0.7)

alpha1, beta1 = least_squares_fit(train_fs, train_ys)
alpha2, beta2 = least_squares_fit(train_os, train_ys)
alpha3, beta3 = least_squares_fit(train_ns, train_ys)
alpha4, beta4 = least_squares_fit(train_cs, train_ys)
alpha5, beta5 = least_squares_fit(train_ss, train_ys)
alpha6, beta6 = least_squares_fit(test_fs, test_ys)
alpha7, beta7 = least_squares_fit(test_os, test_ys)
alpha8, beta8 = least_squares_fit(test_ns, test_ys)
alpha9, beta9 = least_squares_fit(test_cs, test_ys)
alpha10, beta10 = least_squares_fit(test_ss, test_ys)

print("########################################")
print("#################Traing#################")
print("########################################")
print("when xi is fdust : beta =", beta1)
print("R^2 =", r_squared(alpha1,beta1,train_fs,train_ys),"\n")
print("when xi is ozone : beta =", beta2,"")
print("R^2 =", r_squared(alpha2,beta2,train_os,train_ys),"\n")
print("when xi is nd : beta =", beta3)
print("R^2 =", r_squared(alpha3,beta3,train_ns,train_ys),"\n")
print("when xi is cm : beta =", beta4)
print("R^2 =", r_squared(alpha4,beta4,train_cs,train_ys),"\n")
print("when xi is sagas : beta =", beta5)
print("R^2 =", r_squared(alpha5,beta5,train_ss,train_ys),"\n")

print("########################################")
print("##################Test##################")
print("########################################")
print("when xi is fdust : beta =", beta6)
print("R^2 =", r_squared(alpha6,beta6,test_fs,test_ys),"\n")
print("when xi is ozone : beta =", beta7,"")
print("R^2 =", r_squared(alpha7,beta7,test_os,test_ys),"\n")
print("when xi is nd : beta =", beta8)
print("R^2 =", r_squared(alpha8,beta8,test_ns,test_ys),"\n")
print("when xi is cm : beta =", beta9)
print("R^2 =", r_squared(alpha9,beta9,test_cs,test_ys),"\n")
print("when xi is sagas : beta =", beta10)
print("R^2 =", r_squared(alpha10,beta10,test_ss,test_ys),"\n")


#ufdust = predict(alpha1, beta1, fs)
#print(ufdust)

#print(r_squared(alpha1,beta1,fs,ys))

#r_square = multiple_r_squared(xs_list, ys_list, beta)