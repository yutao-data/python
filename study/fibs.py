def fibs(num):
    results = [0, 1]
    for i in range(num - 2):
        results.append(results[-2] + results[-1])
    print(results)


print(fibs(10))
