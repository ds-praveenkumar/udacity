import sys
import pandas as pd

from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
        Read two csv files and merge into one dataframe
        ARGS:
            - path for messages csv file
            - path for categories csv file
        RETURNS:
            - A merge Dataframe 
    """
    # Read CSV files
    print('reading')
    messages_df = pd.read_csv(messages_filepath)
    categories_df = pd.read_csv(categories_filepath)
    
    # Merge CSV files
    merged_df = messages_df.merge(categories_df,on = 'id')
    
    return merged_df

def clean_data(df):
    """
        Cleans merged dataframe
        ARGS:
            - merged Dataframe
        RETURNS:
            - A cleaned Dataframe 
    """
    # Create column based on values in categories column
    categories = df['categories'].str.split(';', expand=True)

    # Rename the columns with the proper name
    row = categories.loc[0,:]
    category_colnames = row.apply(lambda x: x.split('-')[0]).tolist()
    categories.columns = category_colnames

    # Clean the value in categories
    for column in categories:

        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x.split('-')[1])
        
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    categories['related'] = categories['related'].replace(2, 1)

    # Replace the original categories column with the new one and drop duplicates
    df.drop(columns=['categories'], inplace=True)
    df = pd.concat([df, categories], axis=1)
    df.drop_duplicates(inplace=True)

    return df


def save_data(df, database_filename):
    """
        saves clean data from Dataframe to Database.
        ARGS:
            - dataframe and data file
    """   
    # Create sqlite engine and save the dataframe with the name messages
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('messages', engine, index=False)



def main():
    if len(sys.argv) == 4:
        

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        #df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        #save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()