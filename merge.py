import pandas as pd

# Function to standardize 'word' column values
def standardize_word_column(value):
    # Convert to lowercase and strip leading/trailing whitespace
    return str(value).lower().strip()

# Load the data from your CSVs
df1 = pd.read_csv('flashcards_fulldefs_copy.csv')
df2 = pd.read_csv('setences_final_copy.csv')

# Standardize 'word' column in both DataFrames
df1['word'] = df1['word'].apply(standardize_word_column)
df2['word'] = df2['word'].apply(standardize_word_column)

# Merge the dataframes on the standardized 'word' column
merged_df = pd.merge(df1, df2, on='word', how='left')

# Write the merged dataframe to a new CSV file
merged_df.to_csv('combined.csv', index=False)

print("Merged data written to 'combined.csv'")
