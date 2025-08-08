# Preprocessing

import pandas as pd


class preprocessor:
    def __init__(self, path):
        self.book_df = pd.read_csv(path)
        
    def convert_ratings(self):
        """convert string star rating to numbers """

        rating_map = {
            'One':1,
            'Two':2,
            'Three':3,
            'Four':4,
            'Five':5
        }
        
        self.book_df['book_rating'] = self.book_df['book_rating'].map(rating_map)
        
    
    def clean_prices(self):
        """Remove currency symbol (£) and convert price to float."""
        self.book_df['book_price'] = self.book_df['book_price'].replace(
            to_replace='£', value='', regex=True
        ).astype(float)  
        
    def clean_stock(self):
        self.book_df['book_instock'] = self.book_df['book_instock'].apply(
            lambda x: 'In stock' in x if isinstance(x, str) else False
        )
        
    def save_to_csv(self,out_path='books.csv'):
        self.book_df.to_csv(out_path, index=False)
        
        
path = r'D:\DAU\SEM 1\DS605 - Fundamentals of Machine Learning\Lab\Lab02DhruvParmar051\assignment\assignment\books.csv'

books_df = preprocessor(path)
print('book df successful loaded')
books_df.clean_prices()
print('book_df price attribute cleaned')
books_df.clean_stock()
print('book_df in stock attribute cleaned')
books_df.convert_ratings()
print('book_df string ratings converted to numeric')
books_df.save_to_csv(path)
print('book_df is now saved as CSV named books.csv')
