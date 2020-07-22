import json

with open('job_texts.json', 'r') as f:
    texts = json.load(f)

lines = []
for t in texts:
    _lines = t.split('\n')
    _lines = ["<BOS>" + l + "<EOS>" for l in _lines if len(l) > 20]
    lines.extend(_lines)

with open('jobs_lines.json', 'w') as f:
    json.dump(lines, f)

print(f"Number of lines {len(lines)}")

# split to train/val/test
split_train = int(len(lines) * 0.7)
split_val = int(len(lines) * 0.15)
split_test = len(lines) - split_train - split_val

train = lines[0:split_train]
val = lines[split_train:split_train+split_val]
test = lines[split_train+split_val:split_train+split_val+split_test]

with open("train.txt", "w") as f:
    f.writelines(list( "%s\n" % item for item in train ))

with open("val.txt", "w") as f:
    f.writelines(list("%s\n" % item for item in val ))

with open("test.txt", "w") as f:
    f.writelines(list( "%s\n" % item for item in test ))

