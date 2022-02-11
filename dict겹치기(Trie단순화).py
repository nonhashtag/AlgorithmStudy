info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def onTheHash(dictionary : dict, words : list):
    node = dictionary
    for w in words:
        if not w.isalpha():
            break
        if w not in node:
            node[w] = {}
            node = node[w]

table = [i.split() for i in info]
queries = [q.replace(" and", "").split() for q in query]

hashing = {}

onTheHash(hashing, table[0])
