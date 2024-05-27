import os, time
import stanza
from dotenv import load_dotenv

load_dotenv()
STANZA_RESOURCES_DIR=os.getenv("STANZA_RESOURCES_DIR")

nlp = stanza.Pipeline(lang='en', processors='tokenize,ner', download_method=None)

en_doc = nlp("The IRS is in Kansas for Nadia to file her personal taxes on Monday. Walk-ins at 235 Garrison Street, Upland, CA 98232") # run annotation over a sentence

print("Mention text\tType\tStart-End")
for ent in en_doc.ents:
    print("{}\t{}\t{}-{}".format(ent.text, ent.type, ent.start_char, ent.end_char))


# print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in en_doc.sentences for ent in sent.ents], sep='\n')

     