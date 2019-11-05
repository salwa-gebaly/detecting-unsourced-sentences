import sys
import re

if (len(sys.argv) != 3) :
	print('\nUsage: python extract_uncited_stats.py wiki-dump statements-file');
	sys.exit()

# each title or sub-title ends with '(section)'
# '(citation)' indicates a citation


wiki = open(sys.argv[1], 'r')
stats = open(sys.argv[2], 'w+')

# add file header
stats.write('section\tstatement\tcitations\n')

section = ''
for line in wiki :
  # update section  
  if '(section)' in line :
    section = line.replace('(section)', '').replace('\n','')
  
  # split paragraph into sentences, but remove cited ones  
  else :
    # remove <ref> tag
    line = re.sub('<\s*/?ref\s*>','',line)
    
    # put newlines after each sentence ends with a dot
    line = line.replace('. ','.\n').replace('.(citation) ', '.(citation)\n')
    
    sents = line.split('\n')
    # write not cited sentences
    for sent in sents :
      if sent and '(citation)' not in sent :
        stats.write(section+'\t'+sent+'\t'+'0'+'\n')

wiki.close()
stats.close()
