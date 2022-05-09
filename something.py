def median_of_rolling_averages(values, rolling_average_length):
    rolling_averages = []
    for i in range(len(values) - rolling_average_length + 1):
        average = 0
        for j in range(rolling_average_length):
            average += values[i + j]
        average /= rolling_average_length
        rolling_averages.append(average)
    
    rolling_averages.sort()
    print(rolling_averages)
    median_index = len(rolling_averages) // 2
    if len(rolling_averages) % 2 != 0:
        return rolling_averages[median_index]
    else:
        return rolling_averages[median_index]

rolling_average_length = 3
print(median_of_rolling_averages([5, 1, 9, 8, 9999], rolling_average_length))