def number_of_isosceles_triangles(number_of_points, points):
    result = 0
    for a in points:
        distances = {}
        for b in points:
            distance = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
            if distance not in distances:
                distances[distance] = 0
            distances[distance] += 1
        for distance in distances:
            result += distances[distance] * (distances[distance] - 1) // 2
    set_points = set(points)
    count = 0
    for i in range(number_of_points):
        for j in range(number_of_points):
            if i != j:
                if (points[i][0] * 2 - points[j][0], points[i][1] * 2 - points[j][1]) in set_points:
                    count += 1
    return result - count // 2
