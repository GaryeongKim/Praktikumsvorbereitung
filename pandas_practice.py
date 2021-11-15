import numpy as np
import pandas as pd
# Create and populate a 5x2 NumPy array.
my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

# Create a Python list that holds the names of the two columns.
my_column_names = ['temperature', 'activity']

# Create a DataFrame.
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

# Print the entire DataFrame
print(my_dataframe)

"""
the Python Circular Import problem occurs 
when you accidentally name your working file the same 
as the module name and those modules depend on each other. 
This way the python opens the same file which causes a circular loop and eventually throws an error.

So be carefull do not name python file as same as the existed moduls etc you want to use!
"""