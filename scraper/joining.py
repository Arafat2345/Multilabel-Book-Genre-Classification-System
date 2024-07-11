import pandas as pd

# List of CSV files
csv_files = [
    "best_book_2020's_details_scraper.csv",
    "best_book_2010's_details.csv",
    "best_book_2000's_details.csv",
    "best_book_1990's_details.csv",
    "best_book_1980's_details.csv",
    "best_book_1970's_details.csv",
    "best_book_1960's_details.csv",
    "best_book_1950's_details.csv",
    "best_book_1940's_details.csv",
    "best_book_1930's_details.csv"
]

# Read each CSV file into a DataFrame and store them in a list
data_frames = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv("best_books_details.csv", index=False)

