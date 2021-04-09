import os
java_path = "C:\\Program Files\\Java\\jre1.8.0_281\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path


#import data kalimat
import pandas as pd
df = pd.read_csv('G:\Agus Folder\Data Science\parser\Data\Data test\kalimat (id_gsd-ud-dev).csv',encoding='iso-8859-1')

##Tagger
from nltk.tag.stanford import StanfordPOSTagger
path_to_model = "D:\Constituency parsing\Parser\stanford-parser-full-2020-11-17\ind_pos_tag"
path_to_jar = "D:\Constituency parsing\Parser\stanford-parser-full-2020-11-17\stanford-postagger-4.2.0.jar"
tagger=StanfordPOSTagger(path_to_model, path_to_jar)
# tagger.java_options='-mx4096m'          ### Setting higher memory limit for long sentences

sentences = []
for x in range(len(df['sentences'])):
    sentence = df.at[x,'sentences']
    tagged = tagger.tag(sentence.split())
    sentences.append(tagged)
df['tagged'] = sentences 

##Constituent Parser
from nltk.parse.stanford import StanfordParser
path_to_model_1 = "D:\Constituency parsing\Parser\stanford-parser-full-2020-11-17\model.ser.gz"
path_to_jar_1 = "D:\Constituency parsing\Parser\stanford-parser-full-2020-11-17\stanford-parser.jar"
parser= StanfordParser(path_to_model_1, path_to_jar_1)
# parser.java_options='-mx4096m'          ### Setting higher memory limit for long sentences
parse_string = []
for y in range(len(df['tagged'])):
    tagged = df.at[y,'tagged']
    cons = next(parser.tagged_parse(tagged))
    cons = ' '.join(str(cons).split())
    parse_string.append(cons)
df['Parse_String'] = parse_string

# parse_string = ' '.join(str(cons).split())
# print(parse_string)

#Move into excel csv
import pandas as pd
df_new = df
df_new.to_csv('coba.csv')

# print(cons.pretty_print())