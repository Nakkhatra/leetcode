def maxAreaNaive(height):
    Max = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            if height[i] < height[j]:
                area = height[i] * (j - i)
            else:
                area = height[j] * (j - i)
            # area = (height[i]  (height[i] < height[j]) + height[j]  (height[i] >= height[j])) * (j-i)

            if area > Max:
                Max = area

    return Max


def maxAreatry(height):
    sHeight = sorted(set(height))
    lengths = []

    Max = 0

    for h in sHeight:
        print(f"iter for {h} #############")
        idx = [i for i, x in enumerate(height) if x == h]
        print(f"indices of lowest number {h} = {idx}")
        for index in idx:
            lengths.append(len(height) - 1 - index)
            lengths.append(index)

        print(f"lengths for both ends: {lengths}")

        maxlen = max(lengths)
        lengths = []

        if (maxlen * h) > Max:
            Max = maxlen * h

        for index in idx:
            if index == 0 or index == len(height) - 1:
                height[index] = "*"
            else:
                height[index] = 0

        height = [x for x in height if x != "*"]

        print(f"result: {height}, {maxlen}, {h}, {Max}")

    return Max


def maxAreatry2(height):
    sHeight = sorted(set(height))[::-1]
    Max = 0
    area = 0

    for i, h in enumerate(sHeight):
        if (len(height) - 1) * h >= Max:
            candidates = [i for i, x in enumerate(height) if x == h]
            if i == 0:
                if len(candidates) > 1:
                    start, end = candidates[0], candidates[-1]
                    Range = [start, end]
                    area = (end - start) * h

                else:
                    Range = candidates

            else:
                for candidate in candidates:
                    if len(Range) > 1:
                        if candidate in range(start, end):
                            continue
                        else:
                            if candidate <= start:
                                start = candidate
                            else:
                                end = candidate
                    else:
                        if candidate >= Range[0]:
                            start = Range[0]
                            end = candidate
                        else:
                            end = Range[0]
                            start = candidate

                        Range = [start, end]

                    area = h * (end - start)
                    # if area > Max:
                    #     Max = area
        else:
            break

        if area > Max:
            Max = area

    return Max

# NOTE: Below is the most efficient method======================================================================

def maxArea(height):
    s = 0
    Max = 0
    start = 0
    end = len(height) - 1
    
    for _ in height:
        
        if height[start] >= height[end]:
            if height[end] <= s:
                end -= 1
                continue
            
            s = height[end]
            area = s * (end - start)
            end -= 1
            
        else:
            if height[start] <= s:
                start += 1
                continue
            
            s = height[start]
            area = s * (end - start)
            start += 1
            
        if area > Max:
            Max = area
        
    return Max
        
        
        
        
    

# print(maxArea([3, 6, 5, 8, 1]))
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(maxArea([4, 2, 1, 3, 1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(maxArea([1, 2, 1]))
print(maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4]))
