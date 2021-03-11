###solution to exercise 50 from ben stephenson's "the python workbook".

print("Enter the coefficients of the quadratic equation:")
coefficients = input().split(',')
coefficients = [float(i) for i in coefficients]
a,b,c = coefficients[0],coefficients[1],coefficients[2]

disc = b ** 2 - 4 * a * c

if disc < 0:
  print('The equation has no real roots.')
elif disc == 0:
  print(f'The equation has one real root: {(0 - b) / (2 * a):.4f}.')
else:
  print(f'The equation has two real roots: {((0 - b )+ ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a):.4f} and {((0 - b )- ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a):.4f}.')
