import jsonlines


#used this method for dataset of bills
dataset = jsonlines.open('')

data = []


data[0]['summary']
for i in range(len(data)//2):
    train.append(data[i]['text'])
    label.append(data[i]['summary'])


output = ''

tldr = """

TLDR:

"""

separator = """

--separate

"""

for i in range(len(train)):
    output += train[i]+tldr+label[i]+separator


with open(, 'w') as f:
    f.write(output)
