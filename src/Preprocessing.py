import pandas as pd

def load_and_clean_data(path="data/Dataset.csv"):
    df = pd.read_csv(path, encoding='latin1')

    # Rename columns (Zomato dataset)
    df = df.rename(columns={
        'name': 'Restaurant Name',
        'cuisines': 'Cuisines',
        'rate': 'Aggregate rating',
        'approx_cost(for two people)': 'Average Cost for two'
    })

    # Keep only required columns
    df = df[['Restaurant Name', 'Cuisines', 'Aggregate rating', 'Average Cost for two']]

    # Remove duplicates
    df = df.drop_duplicates(subset=['Restaurant Name', 'Cuisines'])

    # Fill missing
    df['Cuisines'] = df['Cuisines'].fillna('')
    df['Aggregate rating'] = df['Aggregate rating'].fillna('0')
    df['Average Cost for two'] = df['Average Cost for two'].fillna('0')

    # Clean rating
    df['Aggregate rating'] = df['Aggregate rating'].astype(str).str.replace('/5', '')
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

    # Clean cost
    df['Average Cost for two'] = df['Average Cost for two'].astype(str)
    df['Average Cost for two'] = df['Average Cost for two'].str.replace('₹', '')
    df['Average Cost for two'] = df['Average Cost for two'].str.replace(',', '')
    df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')

    # Remove bad data
    df = df[df['Aggregate rating'] >= 3.5]
    df = df[df['Average Cost for two'] > 100]

    # Fill remaining NaN
    df['Aggregate rating'] = df['Aggregate rating'].fillna(0)
    df['Average Cost for two'] = df['Average Cost for two'].fillna(df['Average Cost for two'].mean())

    # 🔥 IMPORTANT: reset index (fixes your crash)
    df = df.reset_index(drop=True)

    return df