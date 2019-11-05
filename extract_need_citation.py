import sys
import pandas as pd

if (len(sys.argv) != 3) :
	print('\nUsage: python extract_need_citation.py predicted-result statements-file');
	sys.exit()

# read the csv file with tab as delimiter
pred = pd.read_csv(sys.argv[1], delimiter='\t')

# tab delimiter caused some shifts in Prediction column
# so we convert it to numeric again
pred['Prediction']=pd.to_numeric(pred['Prediction'], errors='coerce')

# choose statements with values >= 0.5 (need citation) 
pred=pred[pred['Prediction']>=0.5]

# write statements into a csv file
pred['Text'].to_csv(sys.argv[2], index=False, header=False)
