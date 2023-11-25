NO_OF_CHARS = 256

def getNextState(pat, M, state, x):
    if state < M and x == ord(pat[state]):
        return state + 1
    i = 0
    for ns in range(state, 0, -1):
        if ord(pat[ns - 1]) == x:
            while i < ns - 1:
                if pat[i] != pat[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0

def computeTF(pat, M):
    global NO_OF_CHARS
    TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(M + 1)]
    for state in range(M + 1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
    return TF

def finite_automaton(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)
    state = 0
    operations = 0  # Initialize the operation count
    for i in range(N):
        operations += 1  # Increment the operation count for state transition
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".format(i - M + 1))
    return operations

def get_user_input():
    txt = input("Enter the text: ")
    pat = input("Enter the pattern: ")
    return txt, pat

if __name__ == '__main__':
    txt, pat = get_user_input()
    print('Finite Automaton:')
    start_time = time.time()
    operations = finite_automaton(pat, txt)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Number of operations (state transitions):", operations)
    print("Execution time:", execution_time, "seconds")
