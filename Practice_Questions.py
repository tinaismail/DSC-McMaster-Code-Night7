def problem1(balance, transactions, credit_score):
    X = 10
    Y = 2
    if credit_score < 300:
        X = 20
        Y = 5
    if balance < 2500:
        balance -= X
    if transactions < 2 or transactions >10:
        balance -= Y*transactions
    if balance < 0:
        return "Your balance is Negative"
    else: return balance

print(problem1(2389.53, 13, 300))
print(problem1(20.21, 1, 140))
print(problem1(7815.83,0,200))
        
def problem2(nums):
    largest = []
    if sum(nums)==0:
        return 0
    sorted_nums = sorted(nums)
    i=0
    while len(largest) < len(sorted_nums):
        i -= 1
        largest.append(sorted_nums[i])
    largest = str(largest)
    largest = largest.replace(", ","")
    largest = largest[1:-1]
    return (largest)

print(problem2([5,2,7,9,3]))
print(problem2([5]))
print(problem2([6,1,6,1]))
print(problem2([0,0,0]))

def problem3(nums, quotient):
    fax = False
    for i in nums:
        for j in nums:
            try:
                if i/j==quotient or j/i==quotient:
                    fax=True
            except:
                if j!=0:
                    if i/j==quotient:
                        fax=True
                elif i!=0:
                    if j/i == quotient:
                        fax=True
    return fax

print(problem3([264,94,92,35,24,421],11))
print(problem3([-126, -21, 63, -57, 52],6))
print(problem3([-126, 21, 63, -57, 52],6))
print(problem3([0, -21, 63, -126, 52],6))
        
def problem4(matrix):
    diag_sum = 0
    x=0
    try:
        for i in range(len(matrix)):
            diag_sum+=matrix[x][x]
            x+=1
    except:
        pass
    return diag_sum

print(problem4([[21,53,68],[83,64,69],[27,12,32]]))
print(problem4([[0,1,1],[2,0,2],[3,3,0]]))
print(problem4([[1,1,1],[-1,-1,-1],[1,1,1]]))
print(problem4([[]]))

        
