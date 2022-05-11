import pandas as pd
import logging
import os
import glob

logging.basicConfig(filename="csv_concat.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

combined_csv = r'C:\Users\Pooja Rani TS\Downloads\Engineering Test Risk Analytics\Engineering Test Risk Analytics\Engineering Test Files\Combined.csv'
if os.path.exists(combined_csv):
    logger.info(f'reading input file {combined_csv}')
    df = pd.read_csv(combined_csv)
else:
    logger.info(f'{combined_csv}  file not available, creating a new file') 
    df = pd.DataFrame()

print(df.shape)

# Copying the combined input
df_output = df.copy()

for file in glob.glob(r'C:\Users\Pooja Rani TS\Downloads\Engineering Test Risk Analytics\Engineering Test Risk Analytics\Engineering Test Files\*'):
    if os.path.basename(file) != "Combined.csv":
        logger.info(f'Reading CSV {file} to append')
        df_file = pd.read_csv(file)

        df_file['Environment'] = (os.path.basename(file).split('.'))[0]

        df_output = pd.concat([df_output,df_file[['Source IP','Environment']]],ignore_index = True)
        print(os.path.basename(file))

df_output['Environment'] = df_output['Environment'].str.replace('\s\d+', '')

# Removing integers from enviroment values
df_output.drop_duplicates(inplace=True)
print(df_output)

# Sorting the dataframe based on source IP column
df_output.sort_values('Source IP',inplace= True)
df_output.to_csv('Combined.csv')
logger.info(f'output file created {combined_csv}')
