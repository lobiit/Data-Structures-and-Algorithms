def find_biggest_number(samplearray):
    biggest_number = samplearray[0]
    for index in range(1, len(samplearray)):
        if samplearray[index]>biggest_number:
            biggest_number = samplearray[index]
    print(biggest_number)
