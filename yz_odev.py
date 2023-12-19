import math

# kosinus_benzerliğ:
def kosinus_benzerligi(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a**2 for a in vector1))
    magnitude2 = math.sqrt(sum(b**2 for b in vector2))
    return dot_product / (magnitude1 * magnitude2)
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result = kosinus_benzerligi(vector1, vector2)
print(f"kosinus_benzerliğ: {result}")


# kare_kök:
def kare_kok(number):
    return math.sqrt(number)
number = 16
result = kare_kok(number)
print(f"kare_kök: {result}")
 


# oklit:
def oklit_mesafesi(point1, point2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(point1, point2)))
point1 = (1, 2)
point2 = (4, 6)
result = oklit_mesafesi(point1, point2)
print(f"oklit mesafesi: {result}")



# manhattan :
def manhattan_mesafesi(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))
point1 = (1, 2)
point2 = (4, 6)
result = manhattan_mesafesi(point1, point2)
print(f"Manhattan mesafesi: {result}")



# minkowski :
def minkowski_mesafesi(point1, point2, p):
    return sum(abs(a - b)**p for a, b in zip(point1, point2))**(1/p)
point1 = (1, 2)
point2 = (4, 6)
p = 3  
result = minkowski_distance(point1, point2, p)
print(f"Minkowski mesafesi (p={p}): {result}")
