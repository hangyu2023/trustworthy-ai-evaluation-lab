import json

def accuracy(items):
    return sum(1 for x in items if x["pred"] == x["label"]) / len(items)

def confusion(items):
    labels = ["correct","partially_correct","incorrect"]
    M = {a:{b:0 for b in labels} for a in labels}
    for x in items:
        M[x["label"]][x["pred"]] += 1
    return M
