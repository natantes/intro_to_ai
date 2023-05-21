import common

def part_one_classifier(training_data, test_data):
    weights, bias = [0.0 for _ in range(common.constants.DATA_DIM)], 0.0
    
    for _ in range(1000):  
        for x in training_data:
            y = x[common.constants.DATA_DIM]
            pred = sum(weights[i] * x[i] for i in range(common.constants.DATA_DIM)) + bias > 0 
            if pred != y:
                for i in range(common.constants.DATA_DIM):
                    weights[i] += (y - pred) * x[i]
                bias += y - pred
    
    for x in test_data:
        x[common.constants.DATA_DIM] = sum(weights[i] * x[i] for i in range(common.constants.DATA_DIM)) + bias > 0

def part_two_classifier(training_data, test_data):
    weights = [[0.0 for _ in range(common.constants.DATA_DIM)] for _ in range(common.constants.NUM_CLASSES)]

    for _ in range(1000): 
        for x in training_data:
            y = int(x[common.constants.DATA_DIM])
            dp = [sum(weights[i][j] * x[j] for j in range(common.constants.DATA_DIM)) for i in range(common.constants.NUM_CLASSES)]
            prediction = dp.index(max(dp))
            if prediction != y:
                for i in range(common.constants.DATA_DIM):
                    weights[y][i] += x[i]
                    weights[prediction][i] -= x[i]
    
    for x in test_data:
        dp = [sum(weights[i][j] * x[j] for j in range(common.constants.DATA_DIM)) for i in range(common.constants.NUM_CLASSES)]
        x[common.constants.DATA_DIM] = dp.index(max(dp))