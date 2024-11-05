# import numpy as np
# import pandas as pd

# # Task 1
# arry = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9],
#                  [10, 11, 12]])

# # Task 2
# rand_array = np.random.random((3, 4))

# # Task 3
# arry_shape = arry.shape
# rand_array_shape = rand_array.shape

# # Task 4
# matrix_product = np.dot(arry, rand_array)

# # Displaying the results
# print("arry - Shape:", arry_shape)
# print(" rand_array - Shape:", rand_array_shape)
# print("Matrix Product using NumPy:\n", matrix_product)





import pandas as pd

# Sample data (replace this with your actual data)
data = pd.DataFrame({
    'gender': ['male', 'female', 'male', 'female', 'male'],
    'age': [30, 25, 40, 22, 35],
    'salary': [60000, 45000, 75000, 55000, 80000],
    'iphone_purchase': [True, False, True, False, True]
})


data.rename(columns={'salary': 'income'}, inplace=True)


gender_counts = data['gender'].value_counts()


females_data = data[data['gender'] == 'female']
males_data = data[data['gender'] == 'male']


min_age = data['age'].min()
max_age = data['age'].max()


income_purchase_data = data[['income', 'iphone_purchase']]

# Displaying the results
print( data)
print(gender_counts)
print(females_data)
print( males_data)
print( min_age,  max_age)
print( income_purchase_data)




