import pandas as pd
from collections import Counter
#from scratch.linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt
import random
from typing import TypeVar, List, Tuple
X = TypeVar('X')  # generic type to represent a data point
Y = TypeVar('Y')  # generic type to represent output variables




def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""
    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
             key=lambda point_label: distance(point_label[0], new_point))
    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]
    # and let them vote
    return majority_vote(k_nearest_labels)

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:] #(실습) Make a shallow copy
    #random.shuffle(data) #(실습) because shuffle modifies the list.
    cut = int(len(data) * prob) #(실습) Use prob to find a cutoff
    return data[:cut], data[cut:] #(실습) and split the shuffled list there.

"""
data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

# The proportions should be correct
assert len(train) == 750
assert len(test) == 250

# And the original data should be preserved (in some order)
assert sorted(train + test) == data
"""


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
"""
xs = [x for x in range(20)]  # xs are 1 ... 1000
ys = [2 * x for x in xs]       # each y_i is twice x_i
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)

print(xs, ys)
print(x_train, x_test)
print(y_train, y_test)
"""

def tp_tn_fn_fp(real, k_pred):
    tp=0
    tn=0
    fn=0
    fp=0
    #tp = Counter((real==True) and (k_pred==True))
    for i in range(len(real)):
        if (real[i] == True) and (k_pred[i] ==True):
            tp+=1
    #tn=sum((real==0)&(k_pred==0))
        if (real[i] == False) and (k_pred[i] == False):
            tn += 1
    #fn=sum((real==1)&(k_pred==0))
        if (real[i] == True) and (k_pred[i] == False):
            fn += 1
    #fp=sum((real==0)&(k_pred==1))
        if (real[i] == False) and (k_pred[i] == True):
            fp += 1
    return tp, tn, fn, fp

def accuracy(tp,tn,fn,fp):
    return (tp+tn)*100 / (tp+tn+fn+fp)

def precision(tp, fp):
    if(tp+fp)==0:
        return 0
    else:
        return tp / (tp+fp)

def recall(tp, fn):
    if (tp + fn)==0:
        return 0
    else:
        return tp / (tp+fn)

def f1_score(pre, rec):
    if (pre + rec)==0:
        print("f1-score 4등급")
        return 0
    else:
        if (2 * pre * rec / (pre + rec))>=0.75:
            print("f1-score 1등급")
        elif (2 * pre * rec / (pre + rec))>=0.5:
            print("f1-score 2등급")
        elif (2 * pre * rec / (pre + rec))>=0.25:
            print("f1-score 3등급")
        else:
            print("f1-score 4등급")
        if (pre + rec) == 0:
            return 2*pre*rec/1
        else:
            return 2 * pre * rec / (pre + rec)




df = pd.read_csv("data2_2.csv", encoding='utf-8-sig', parse_dates=True, index_col=0)
df = df.reset_index()

#data = [n for n in range(1000)]
#train, test = split_data(data, 0.75)




df_list = df.values.tolist()
df_qual = df['airquality'].values.tolist()
#df_record = df.to_records(index=False)  #dataframe to tuple
#df_list = list(df_record)               #tuple to list
#print(df_list)

aver_point = [(7.5, 0.01, 0.01, 0.5, 0.005, "best"),
              (23, 0.025, 0.025, 1.5, 0.015, "better"),
              (35.5, 0.045, 0.045, 3.75, 0.03, "good"),
              (45.5, 0.075, 0.055, 7.25, 0.045, "normal"),
              (63, 0.105, 0.095, 10.5, 0.075, "bad"),
              (88, 0.135, 0.165, 13.5, 0.125, "worse"),
              (125.5, 0.265, 0.65, 23.5, 0.375, "serious"),
              (176.5, 0.495, 1.55, 40.5, 0.825, "worst")]   #각 구간별 중앙값을 좌표로 잡음(거리 비교를 위해서)

aver_point = [([f, o, n, c, s], pred)
              for f, o, n, c, s, pred in aver_point]


#print(df_list[1][5:10])
#print(len(df_list))


pred_quality = [knn_classify(1, aver_point ,df_list[i][5:10]) for i in range(len(df_list))]


"""
best= [df_list[i][10]=="best" for i in range(len(df_list))]
pbest = [pred_quality[i]=="best" for i in range(len(df_list))]

better = [df_list[i][10]=="better" for i in range(len(df_list))]
pbetter=[pred_quality[i]=="better" for i in range(len(df_list))]

good = [df_list[i][10]=="good" for i in range(len(df_list))]
pgood=[pred_quality[i]=="good" for i in range(len(df_list))]

normal = [df_list[i][10]=="normal" for i in range(len(df_list))]
pnormal= [pred_quality[i]=="normal" for i in range(len(df_list))]

bad = [df_list[i][10]=="bad" for i in range(len(df_list))]
pbad=[pred_quality[i]=="bad" for i in range(len(df_list))]

worse = [df_list[i][10]=="worse" for i in range(len(df_list))]
pworse= [pred_quality[i]=="worse" for i in range(len(df_list))]

serious = [df_list[i][10]=="serious" for i in range(len(df_list))]
pserious=[pred_quality[i]=="serious" for i in range(len(df_list))]

worst = [df_list[i][10]=="worst" for i in range(len(df_list))]
pworst= [pred_quality[i]=="worst" for i in range(len(df_list))]
"""


train, test = split_data(df_qual, 0.7)
ptrain, ptest = split_data(pred_quality, 0.7)

"""traing data"""
traing_best= [train[i]=="best" for i in range(len(train))]
traing_pbest = [ptrain[i]=="best" for i in range(len(ptrain))]

traing_better = [train[i]=="better" for i in range(len(train))]
traing_pbetter=[ptrain[i]=="better" for i in range(len(ptrain))]

traing_good = [train[i]=="good" for i in range(len(train))]
traing_pgood=[ptrain[i]=="good" for i in range(len(ptrain))]

traing_normal = [train[i]=="normal" for i in range(len(train))]
traing_pnormal= [ptrain[i]=="normal" for i in range(len(ptrain))]

traing_bad = [train[i]=="bad" for i in range(len(train))]
traing_pbad=[ptrain[i]=="bad" for i in range(len(train))]

traing_worse = [train[i]=="worse" for i in range(len(train))]
traing_pworse= [ptrain[i]=="worse" for i in range(len(train))]

traing_serious = [train[i]=="serious" for i in range(len(train))]
traing_pserious=[ptrain[i]=="serious" for i in range(len(train))]

traing_worst = [train[i]=="worst" for i in range(len(train))]
traing_pworst= [ptrain[i]=="worst" for i in range(len(train))]




"""test data"""
best= [test[i]=="best" for i in range(len(test))]
pbest = [ptest[i]=="best" for i in range(len(test))]

better = [test[i]=="better" for i in range(len(test))]
pbetter=[ptest[i]=="better" for i in range(len(test))]

good = [test[i]=="good" for i in range(len(test))]
pgood=[ptest[i]=="good" for i in range(len(test))]

normal = [test[i]=="normal" for i in range(len(test))]
pnormal= [ptest[i]=="normal" for i in range(len(test))]

bad = [test[i]=="bad" for i in range(len(test))]
pbad=[ptest[i]=="bad" for i in range(len(test))]

worse = [test[i]=="worse" for i in range(len(test))]
pworse= [ptest[i]=="worse" for i in range(len(test))]

serious = [test[i]=="serious" for i in range(len(test))]
pserious=[ptest[i]=="serious" for i in range(len(test))]

worst = [test[i]=="worst" for i in range(len(test))]
pworst= [ptest[i]=="worst" for i in range(len(test))]


traing_tp_best, traing_tn_best, traing_fn_best, traing_fp_best = tp_tn_fn_fp(traing_best, traing_pbest)
traing_tp_better, traing_tn_better, traing_fn_better, traing_fp_better = tp_tn_fn_fp(traing_better, traing_pbetter)
traing_tp_good, traing_tn_good, traing_fn_good, traing_fp_good = tp_tn_fn_fp(traing_good, traing_pgood)
traing_tp_normal, traing_tn_normal, traing_fn_normal, traing_fp_normal = tp_tn_fn_fp(traing_normal, traing_pnormal)
traing_tp_bad, traing_tn_bad, traing_fn_bad, traing_fp_bad = tp_tn_fn_fp(traing_bad, traing_pbad)
traing_tp_worse, traing_tn_worse, traing_fn_worse, traing_fp_worse = tp_tn_fn_fp(traing_worse, traing_pworse)
traing_tp_serious, traing_tn_serious, traing_fn_serious, traing_fp_serious = tp_tn_fn_fp(traing_serious, traing_pserious)
traing_tp_worst, traing_tn_worst, traing_fn_worst, traing_fp_worst = tp_tn_fn_fp(traing_worst, traing_pworst)

tp_best, tn_best, fn_best, fp_best = tp_tn_fn_fp(best, pbest)
tp_better, tn_better, fn_better, fp_better = tp_tn_fn_fp(better, pbetter)
tp_good, tn_good, fn_good, fp_good = tp_tn_fn_fp(good, pgood)
tp_normal, tn_normal, fn_normal, fp_normal = tp_tn_fn_fp(normal, pnormal)
tp_bad, tn_bad, fn_bad, fp_bad = tp_tn_fn_fp(bad, pbad)
tp_worse, tn_worse, fn_worse, fp_worse = tp_tn_fn_fp(worse, pworse)
tp_serious, tn_serious, fn_serious, fp_serious = tp_tn_fn_fp(serious, pserious)
tp_worst, tn_worst, fn_worst, fp_worst = tp_tn_fn_fp(worst, pworst)

#recall(traing_tp_best, traing_fn_best)
#print(tp_best)
#print(fn_best)

print("Training Best\n recall:", recall(traing_tp_best, traing_fn_best), "precision:",
      precision(traing_tp_best, traing_fp_best), "f1-score:",
      f1_score(precision(traing_tp_best, traing_fp_best), recall(traing_tp_best,traing_fn_best)), "\n")
print("Training Better\n recall:", recall(traing_tp_better, traing_fn_better), "precision:",
      precision(traing_tp_better, traing_fp_better), "f1-score:",
      f1_score(precision(traing_tp_better, traing_fp_better), recall(traing_tp_better, traing_fn_better)), "\n")
print("Training Good\n recall:", recall(traing_tp_good, traing_fn_good), "precision:",
      precision(traing_tp_good, traing_fp_good), "f1-score:",
      f1_score(precision(traing_tp_good, traing_fp_good),recall(traing_tp_good, traing_fn_good)), "\n")
print("Training Normal\n recall:", recall(traing_tp_normal, traing_fn_normal), "precision:",
      precision(traing_tp_normal, traing_fp_normal), "f1-score:",
      f1_score(precision(traing_tp_normal, traing_fp_normal),recall(traing_tp_normal, traing_fn_normal)), "\n")
print("Training Bad\n recall:", recall(traing_tp_bad, traing_fn_bad), "precision:",
      precision(traing_tp_bad, traing_fp_bad), "f1-score:",
      f1_score(precision(traing_tp_bad, traing_fp_bad),recall(traing_tp_bad, traing_fn_bad)), "\n")
print("Training Worse\n recall:", recall(traing_tp_worse, traing_fn_worse), "precision:",
      precision(traing_tp_worse, traing_fp_worse), "f1-score:",
      f1_score(precision(traing_tp_worse, traing_fp_worse), recall(traing_tp_worse, traing_fn_worse)), "\n")
print("Training Serious\n recall:", recall(traing_tp_serious, traing_fn_serious), "precision:",
      precision(traing_tp_serious, traing_fp_serious), "f1-score:",
      f1_score(precision(traing_tp_serious, traing_fp_serious), recall(traing_tp_serious, traing_fn_serious)), "\n")
print("Training Worst\n recall:", recall(traing_tp_worst, traing_fn_worst), "precision:",
      precision(traing_tp_worst, traing_fp_worst), "f1-score:",
      f1_score(precision(traing_tp_worst, traing_fp_worst), recall(traing_tp_worst, traing_fn_worst)), "\n")




print("Test Best\n recall:", recall(tp_best, fn_best), "precision:",
      precision(tp_best, fp_best), "f1-score:",
      f1_score(precision(tp_best, fp_best), recall(tp_best, fn_best)), "\n")
print("Test Better\n recall:", recall(tp_better, fn_better), "precision:",
      precision(tp_better, fp_better), "f1-score:",
      f1_score(precision(tp_better, fp_better), recall(tp_better, fn_better)), "\n")
print("Test Good\n recall:", recall(tp_good, fn_good), "precision:",
      precision(tp_good, fp_good), "f1-score:",
      f1_score(precision(tp_good, fp_good),recall(tp_good, fn_good)), "\n")
print("Test Normal\n recall:", recall(tp_normal, fn_normal), "precision:",
      precision(tp_normal, fp_normal), "f1-score:",
      f1_score(precision(tp_normal, fp_normal),recall(tp_normal, fn_normal)), "\n")
print("Test Bad\n recall:", recall(tp_bad, fn_bad), "precision:",
      precision(tp_bad, fp_bad), "f1-score:",
      f1_score(precision(tp_bad, fp_bad),recall(tp_bad, fn_bad)), "\n")
print("Test Worse\n recall:", recall(tp_worse, fn_worse), "precision:",
      precision(tp_worse, fp_worse), "f1-score:",
      f1_score(precision(tp_worse, fp_worse), recall(tp_worse, fn_worse)), "\n")
print("Test Serious\n recall:", recall(tp_serious, fn_serious), "precision:",
      precision(tp_serious, fp_serious),
      "f1-score:", f1_score(precision(tp_serious, fp_serious), recall(tp_serious, fn_serious)), "\n")
print("Test Worst\n recall:", recall(tp_worst, fn_worst), "precision:",
      precision(tp_worst, fp_worst), "f1-score:",
      f1_score(precision(tp_worst, fp_worst), recall(tp_worst, fn_worst)), "\n")
