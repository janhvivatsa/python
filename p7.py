arr = [1, 2, 3, 4, 5]
k = 3

window_sum = 0

for i in range(len(arr)):
    window_sum += arr[i]

    if i >= k - 1:
        print(window_sum) 
        window_sum -= arr[i - k + 1]
