def scoreComp(document):
    #print(document)
    document = open(document,"r")
    document = document.read()
    stopWords = ["is", "a","in", "which",",","or","are","too","from","the","you","that","the","them","does","not","more","your","than"
    "not","having","puts","serious","also","control","if","to", "be", "of","and","use","can","all","such","he","she","it","an"]
    bagOfWords = []
    documentList = document.split()
    labels = {"computer science" : ['theory','engineer','science','algorithm', 'mathematics','academic'], "program" : ['web', 'calculating', 'machine learning', 'engine','game','programming'],
    			"computer"    : [ 'digital', 'ibm','computation','software','hardware'],   "parts" : ['hard drive','mother board','gpu','mechanical','cpu'],"function":['communication','storage', 'output','processing', 'networking','distributed',
                'database'] }

    for word in documentList :
    	if word not in stopWords :
    		bagOfWords.append(word)

    outputLabel = {}

    for word in bagOfWords :
        word=word.replace(',','')
        word=word.replace('.','')
        word=word.replace('?','')
        word=word.replace('(','')
        word=word.replace(')','')
        word=word.lower()

    count =0
    for word in bagOfWords :
        for labelKey in labels:
    		# Iterating over all the words associated with the label
            associatedToLabel = labels[labelKey]
            if word in associatedToLabel :
                if word in outputLabel.keys() :
                    outputLabel[word][0] += 1

                else :
    				# Update the dictionary
                    data = []
                    data.append(1)
                    data.append(labelKey)
                    entry = { word:data}
                    outputLabel.update(entry)
                    count = count +1
    return count


def scoreDiabetes(document):
    #print(document)
    document = open(document,"r")
    document = document.read()
    stopWords = ["is", "a","in", "which",",","or","are","too","from","the","you","that","the","them","does","not","more","your","than"
    "not","having","puts","serious","also","control","if","to", "be", "of","and","use","can","all","such","he","she","it","an"]
    bagOfWords = []
    documentList = document.split()
    labels = {"diabetes" : ['diabetic','prediabetes','insulin','type'], "blood sugar" : ['blood', 'glucose', 'sugar', 'glucose','diet','exercise'],
    			"doctor"    : [ 'medical', 'professional', 'blood','test','a1c'],   "body" : ['heart','stomach','nerves','kidney','eyes','blood','hormone'] }

    for word in documentList :
    	if word not in stopWords :
    		bagOfWords.append(word)

    outputLabel = {}

    for word in bagOfWords :
        word=word.replace(',','')
        word=word.replace('.','')
        word=word.replace('?','')
        word=word.replace('(','')
        word=word.replace(')','')
        word=word.lower()
    count =0
    for word in bagOfWords :

        for labelKey in labels:
    		# Iterating over all the words associated with the label
            associatedToLabel = labels[labelKey]

            if word in associatedToLabel :
                if word in outputLabel.keys() :
                    outputLabel[word][0] += 1

                else :
    				# Update the dictionary
                    data = []
                    data.append(1)
                    data.append(labelKey)
                    entry = { word:data}
                    outputLabel.update(entry)
                    count = count +1

    return count

def compuPos(document,diff):
    fp = 'FP'
    tp = 'TP'
    if document=='unlabeled-1.txt':
        return tp
    elif document=='unlabeled-2.txt':
        return tp
    elif document=='unlabeled-3.txt':
        return tp
    elif document=='unlabeled-4.txt':
        return tp
    elif document=='unlabeled-5.txt':
        return fp
    elif document=='unlabeled-6.txt':
        return fp

def diaPos(document,diff):
    fp = 'FP'
    tp = 'TP'
    if document=='unlabeled-1.txt':
        return fp
    elif document=='unlabeled-2.txt':
        return fp
    elif document=='unlabeled-3.txt':
        return fp
    elif document=='unlabeled-4.txt':
        return fp
    elif document=='unlabeled-5.txt':
        return tp
    elif document=='unlabeled-6.txt':
        return fp
def main():
    documents=['unlabeled-1.txt','unlabeled-2.txt','unlabeled-3.txt','unlabeled-4.txt','unlabeled-5.txt','unlabeled-6.txt']
    for document in documents:
        compCount = scoreComp(document)
        diabetesCount = scoreDiabetes(document)
        diff = compCount - diabetesCount
        if diff > 0:
            value = compuPos(document, diff)
            if diff <= 3:
                print('Result below confidence')
            print(document, "Computer Science article score: ",diff, "Positivity",value)
        elif diff < 0:
            diff = abs(diff)
            value = diaPos(document,diff)
            if diff <= 3:
                print('results are not conclusive')
            print(document, "Diabetes Article score: ",diff, "Positvity", value)
        else:
            print("unsure")
        print('------------------------')
print('------------------------')
main()
