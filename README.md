# detecting-unsourced-sentences
The task was to :

- Extract sentences without citations from the Wikipedia data dumps : This was the most important and difficult task. I dealt with wiki dumps once and used apertium WikiExtractor, but since this python script extracts bare text only from the xml file, it wasn't a great help. I looked at and tried 4 out of the 6 suggested parser (2 perl, 1 java and 1 python) scripts, but after some hours of try and error, I found nothing except for errors and not expected formats from me. After that I went again to the WikiExtractor, and tried to read and trace the code, and surprisingly I found what I was looking for, the script was ignoring almost all the tags and elements, and by doing some tweakings here and there, I was finally able to mark citations and sections by a very naive way (by just adding (section) and (citation)) after a section or a citation :).

- Use citation-needed model to detect whether these sentences need citations or not : After I generated the marked wiki dump, I wrote a script to identify an uncited statement and its section and formatting them as required for the classification model, identifying the statements and sections was easy because of the added marks, but I think the problem would be in my segmenting to the text, as I just split the text by a full stop followed by a space '. ' , which I think is not mature enough to segment a paragraph, but I think it will be enough for a demonstration. Now, we have the dataset ready to be fed to the model, but the model gave some errors regarding empty labels which should be the true boolean value for the segment. That was strange because it was stated in the github repo that if we don't need an evaluation, we could just put a zero in the citation column. So, I just commented out the lines causing the error, and it run peacifully after that.

- Generate a dump containing the list of sentences that are detected as needing citations from the model : I wrote a script to extract the statements predicted as 'need citation', which should have prediction score >= 0.5 as true.
 

I worked with this wiki-dump at https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p10p30302.bz2.

And the final 'need a citation' statements could be found here https://drive.google.com/open?id=1XNqsYCZCMMgiZCzw2vufTW4aLylK-w_Y.
