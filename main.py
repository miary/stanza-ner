import os, time
import stanza
from dotenv import load_dotenv

load_dotenv()
STANZA_RESOURCES_DIR=os.getenv("STANZA_RESOURCES_DIR")

if(os.path.isdir(STANZA_RESOURCES_DIR)):
    print(f"Stanza Resource Directory Found: {STANZA_RESOURCES_DIR}")
else:
    print(f"Failed to load Stanza Resources: {STANZA_RESOURCES_DIR}")

nlp = stanza.Pipeline(lang='en', processors='tokenize,ner', download_method=None, model_dir=STANZA_RESOURCES_DIR)

en_doc = nlp("The IRS is in Kansas for Nadia to file her personal taxes on Monday. Walk-ins at 235 Garrison Street, Upland, CA 98232") # run annotation over a sentence
en_doc = nlp("592 Cherry Blod, Upland, California 91784")
en_doc = nlp("document with 370-09-4318")
print("Mention text\tType\tStart-End")
for ent in en_doc.ents:
    print("{}\t{}\t{}-{}".format(ent.text, ent.type, ent.start_char, ent.end_char))


# print(*[f'entity: {ent.text}\ttype: {ent.type}' for sent in en_doc.sentences for ent in sent.ents], sep='\n')

     