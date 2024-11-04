def maxWidth(points):
    points.sort(key=lambda point: point[0])

    max_width = 0
    for i in range(1, len(points)):
        width = points[i][0] - points[i-1][0]
        max_width = max(max_width, width)
    
    return points

points = [[8, 7], [9, 9], [7, 4], [9, 7]]
result = maxWidth(points)
print(result)