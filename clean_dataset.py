##################################################cleaning it (removing unwanted columns)

# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('Crop_recommendation.csv')

# # Drop the column(s) you want to remove, e.g., 'column_to_remove'
# #specify the column name
# df = df.drop(columns=['humidity', 'rainfall'])

# # Save the DataFrame back to a CSV file
# df.to_csv('your_file_modified.csv', index=False)



####################################################limiting the value to certain decimal point

# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('your_file_modified.csv')

# # Round values in a specific column to a certain number of decimal points
# # For example, rounding the values in the 'column_to_round' column to 2 decimal places
# df['ph'] = df['ph'].round(3)

# # Save the modified DataFrame back to a CSV file
# df.to_csv('edited2.csv', index=False)


###################################################similarly limiting temperature to a limit decimal point

# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('edited2.csv')

# # Round values in a specific column to a certain number of decimal points
# # For example, rounding the values in the 'column_to_round' column to 2 decimal places
# df['temperature'] = df['temperature'].round(3)

# # Save the modified DataFrame back to a CSV file
# df.to_csv('edited3.csv', index=False)


#########   clearing redundant values

# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('edited3.csv')

# # Display the first few rows of the DataFrame to understand the structure
# print("DataFrame Head:")
# print(df.head())

# # Group by the specified columns and count the occurrences
# repeated_counts = df.groupby(['N', 'P', 'K', 'temperature', 'ph']).size().reset_index(name='counts')

# # Filter to show only combinations that are repeated
# repeated_combinations = repeated_counts[repeated_counts['counts'] > 1]

# # Display the repeated combinations and their counts
# print("Repeated Combinations:")
# print(repeated_combinations)



# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('Fertilizer Prediction.csv')

# # Drop the column(s) you want to remove, e.g., 'column_to_remove'
# #specify the column name
# df = df.drop(columns=['Humidity ', 'Soil Type'])

# # Save the DataFrame back to a CSV file
# df.to_csv('Fertilizer_Prediction.csv', index=False)


###############      Rearrangement of columns

# import pandas as pd

# # Load the CSV file
# input_file = 'inorganic_fertilizers_npk_value.csv'
# output_file = 'inorganic_fertilizers_npk_value.csv'

# # Read the CSV file
# df = pd.read_csv(input_file)

# # Print the original column order
# print("Original columns:", df.columns)

# # Define the new column order
# new_column_order = ['N', 'P', 'K','Fertilizer']  # replace with your desired order

# # Reorder the columns
# df = df[new_column_order]

# # Print the new column order
# print("New columns:", df.columns)

# # Save the reordered DataFrame to a new CSV file
# df.to_csv(output_file, index=False)
