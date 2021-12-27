import spacy

from spacy.matcher import Matcher
import re


class NER:
    def ner(self, data):
        data = re.sub('[\.,]', " ", data)
        nlp = spacy.load("en_ner_bc5cdr_md")
        doc = nlp(data)
        print(doc)

        medcine_list = []
        for ent in doc.ents:
            if ent.label_ == "CHEMICAL":
                medcine_list.append(ent.text)
        pattern = [{'ENT_TYPE': 'CHEMICAL'}, {'LIKE_NUM': True}, {'IS_ASCII': True}]
        matcher = Matcher(nlp.vocab)
        matcher.add("DRUG_DOSE", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # get string representation
            span = doc[start:end]  # the matched span
            if span.text not in medcine_list:
                medcine_list.append((span.text))
        return medcine_list


NER = NER()
