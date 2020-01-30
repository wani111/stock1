import pandas as pd 
  
# Create the dataframe 
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                    'Cost':[10000, 5000, 15000, 2000]}) 
  
# Print the dataframe 
print(df) 

Row_list =[] 
  
# Iterate over each row 
for index, rows in df.iterrows(): 
    # Create list for the current row 
    my_list =rows.Cost 
      
    # append the list to the final list 
    Row_list.append(my_list) 
  
# Print the list 
print(Row_list) 