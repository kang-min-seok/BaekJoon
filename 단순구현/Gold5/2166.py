def calculate_polygon_area(num_sides, coordinates):
    area = 0.0

    for i in range(num_sides):
        j = (i + 1) % num_sides
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    area = abs(area) / 2.0
    
    print(round(area,1))
    return area

N = int(input()) 
coordinates = []

for i in range(N):
    X, Y = map(int, input().split()) 
    coordinates.append((X, Y)) 

calculate_polygon_area(N, coordinates)