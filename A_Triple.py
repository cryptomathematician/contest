import sys

def find_triple_occurrence(t, test_cases):
    for n, arr in test_cases:
        freq = {}
        candidates = []
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 3:
                candidates.append(num)
        
        print(max(candidates) if candidates else -1)

def main():
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    test_cases = []
    
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index + n]))
        index += n
        test_cases.append((n, arr))
    
    find_triple_occurrence(t, test_cases)

if __name__ == "__main__":
    main()

