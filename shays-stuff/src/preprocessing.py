from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def split_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=123)
    return train, test


def encode_data(df):
    cols_to_encode = ["company_name", "location", "rocket_type"]
    for col in cols_to_encode:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

    return df
