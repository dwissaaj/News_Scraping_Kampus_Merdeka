import main
import pandas as pd
import sys


main.new_df['dates'] = main.new_df['dates'].apply(lambda a: pd.to_datetime(a).date())
clean_data = main.new_df.to_excel('liputan6.xlsx')