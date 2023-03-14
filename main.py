# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0 for _ in range(n)]
    
    for job in range(m):
        next_thread = 0
        
        for cur_thread in range(n):
            if threads[cur_thread] < threads[next_thread]:
                next_thread = cur_thread
        
        output.append([next_thread, threads[next_thread]])
        threads[next_thread] += data[job]

    return output

def main():
    try:
        input_param = list(map(int, input().split()))
        data = list(map(int, input().split()))

        n = input_param[0]
        m = input_param[1]
    except:
        print("Wrong input")
        return

    
    if len(input_param) != 2 or m != len(data):
        print("Wrong input")
        return

    result = parallel_processing(n, m, data)

    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()
