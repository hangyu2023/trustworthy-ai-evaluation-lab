import json, random, argparse
from metrics import accuracy, confusion

parser = argparse.ArgumentParser()
parser.add_argument("--data", required=True)
args = parser.parse_args()

with open(args.data) as f:
    data = [json.loads(line) for line in f]

labels = ["correct","partially_correct","incorrect"]
for x in data:
    x["pred"] = random.choice(labels)

print("Accuracy:", round(accuracy(data),4))
print("Confusion:", json.dumps(confusion(data), indent=2))

