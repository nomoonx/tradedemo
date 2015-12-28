#!/usr/bin/env python
#Name: Tingting Xu, andrew id: tingtinx, date: 03.08.2015
import sys
import math
import random

def parse(data_raw):
	data = []
	for i, x in enumerate(data_raw):
		if i == 0:
			pass
		else:
			temp = x.strip().split(",")
			for j, y in enumerate(temp):
				temp[j] = float(y)/100
			temp.insert(0, 1.0)
			data.append(temp)
	return data

def sigmoid(net):
	return (1+math.exp(-net))**(-1)

def initialization(nodes):
	weights = []
	# weights.append([0.1, 0.2, 0.3, 0.4])
	weights.append([random.random(), random.random(), random.random(), random.random(), random.random()])
	for i in range(1,5):
		# weights.append([0.1, 0.2, 0.3, 0.4, 0.5])
		weights.append([random.random(), random.random(), random.random(), random.random(), random.random(), random.random()])
	return weights

def input(xvalue, weight):
	net = sum([x * y for x, y in zip(weight, xvalue)])
	return net

def learn(data, weights):
	eta = 0.5
	attr = data[:len(data)-1]
	y = data[-1]
	hidden = [1.0]
	for i in range(1,5):
		net = input(attr, weights[i])
		o = sigmoid(net)
		hidden.append(o)
	net = input(hidden, weights[0])
	out = [0]
	out[0] = sigmoid(net)
	out.extend(hidden[1:])
	delta = []
	delta.append(out[0]*(1-out[0])*(y-out[0]))
	for i in range(1,5):
		delta.append(out[i]*(1-out[i])*weights[0][i]*delta[0])
	for i in range(5):
		if i == 0:
			weights[i] = [y+eta*delta[i]*x for x, y in zip(hidden, weights[i])]
		else:
			weights[i] = [y+eta*delta[i]*x for x, y in zip(data[:len(data)-1], weights[i])]
	error = 0.5*(data[-1]-out[0])*(data[-1]-out[0])
	return weights, error

def result(data, weights):
	hidden = [1.0]
	for i in range(1, 5):
		net = input(data, weights[i])
		o = sigmoid(net)
		hidden.append(o)
	net = input(hidden, weights[0])
	out = sigmoid(net)
	return out

if __name__ == "__main__":
	trainfile = sys.argv[1]
	testfile = sys.argv[2]
	train = open(trainfile, "r")
	train_raw = train.readlines()
	train.close()
	train_data = parse(train_raw)
	test = open(testfile, "r")
	test_raw = test.readlines()
	test.close()
	test_data = parse(test_raw)
	nodes = 4
	weights = initialization(nodes)
	iteration = 0
	error_total = 10
	while iteration < 5000 and error_total > 0.003:
		error_total = 0
		for x in train_data:
			weights, error = learn(x, weights)
			error_total += error
		print(error_total)
		iteration += 1
	print('TRAINING COMPLETED! NOW PREDICTING.')
	num = 0
	for x in test_data:
		out = 100*result(x, weights)
		print(out)