# O(len(arr)) time complexity - 0(1) space complexity
def elementsAboveAndBelowN(arr, n):
    above = 0
    below = 0

    for num in arr:
        if num > n:
            above += 1

        elif num < n:
            below += 1

    print(f"above: {above}, below: {below}")

# O(len(string)) time complexity and space complexity
def rotateByN(string, n):
    
    rotation = n % len(string)

    if rotation < 0:
        rotation += len(string)

    overFlowPoint = len(string) - rotation

    print(string[overFlowPoint:] + string[0:overFlowPoint])

