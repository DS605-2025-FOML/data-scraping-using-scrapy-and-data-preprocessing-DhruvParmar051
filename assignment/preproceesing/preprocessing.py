# Preprocessing

import pandas as pd


class Preprocessor:
    def __init__(self, path):
        self.book_df = pd.read_csv(path)
        
    def convert_ratings(self):

        rating_map = {
            'One':1,
            'Two':2,
            'Three':3,
            'Four':4,
            'Five':5
        }
        
        self.book_df['book_rating'] = self.book_df['book_rating'].map(rating_map)
        
    
    def clean_prices(self):
        self.book_df['book_price'] = self.book_df['book_price'].astype(str).str.replace('£', '', regex=False).astype(float)


    def clean_stock(self):
        self.book_df['book_instock'] = self.book_df['book_instock'].apply(
        lambda x: 'In stock' in str(x)
        )

        
    def save_to_csv(self,out_path='books.csv'):
        self.book_df.to_csv(out_path, index=False)
        

if __name__ == '__main__':
    path = r'D:\DAU\SEM 1\DS605 - Fundamentals of Machine Learning\Lab\Lab02DhruvParmar051\assignment\assignment\spiders\books.csv'

    books_df = Preprocessor(path)
    print('book df successfully loaded')
    books_df.clean_prices()
    print('book_df price attribute cleaned')
    books_df.clean_stock()
    print('book_df in stock attribute cleaned')
    books_df.convert_ratings()
    print('book_df string ratings converted to numeric')
    books_df.save_to_csv(path)
    print('book_df is now saved as CSV named books.csv')
