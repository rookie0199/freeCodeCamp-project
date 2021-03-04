import numpy as np
def calculate(list):
    if len(list) == 9:
        arr = np.array(list)
        arr = arr.reshape(3, 3)
        mean_axis0 = np.mean(arr, axis=0).tolist()
        mean_axis1 = np.mean(arr, axis=1).tolist()
        mean_flattened = np.mean(arr)
        variance_axis0 = np.var(arr, axis=0).tolist()
        variance_axis1 = np.var(arr, axis=1).tolist()
        variance_flattened = np.var(arr)
        std_axis0 = np.std(arr, axis=0).tolist()
        std_axis1 = np.std(arr, axis=1).tolist()
        std_flattened = np.std(arr)
        max_axis0 = np.max(arr, axis=0).tolist()
        max_axis1 = np.max(arr,axis=1).tolist()
        max_flattened = np.max(arr)
        min_axis0 = np.min(arr, axis=0).tolist()
        min_axis1 = np.min(arr, axis=1).tolist()
        min_flattened = np.min(arr)
        sum_axis0 = np.sum(arr, axis=0).tolist()
        sum_axis1 = np.sum(arr, axis=1).tolist()
        sum_flattened = np.sum(arr)
        calculations = {
            'mean' : [mean_axis0, mean_axis1, mean_flattened],
            'variance' : [variance_axis0, variance_axis1, variance_flattened],
            'standard deviation' : [std_axis0, std_axis1, std_flattened],
            'max' : [max_axis0, max_axis1, max_flattened],
            'min' : [min_axis0, min_axis1, min_flattened],
            'sum' : [sum_axis0, sum_axis1, sum_flattened]
        }
        return calculations
    else:
        print('List must contain nine numbers.')