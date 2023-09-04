from FASTA import ReadFASTA


def reverseComplement(seq):
    #This function returns a reverse complement
 
        # complement strand
        seq = seq.replace("A", "t").replace(
            "C", "g").replace("T", "a").replace("G", "c")
        seq = seq.upper()
         
        # reverse strand
        seq = seq[::-1]
        return seq
def hammingDistance(a,b):
    if len(a) != len(b):
        raise ValueError("Strand lengths are not equal!")
    else:
        return sum(1 for (i,j) in zip(a,b) if i!=j)

def correction(words):
    prefectWords=[]
    imprefectWords=[]
    #find the prefect words
    for word in words:
        # print(word+"-"+reverseComplement(word))
        # first each word is a candidate for imprefects
        if word  not in imprefectWords and reverseComplement(word) not in imprefectWords:
            imprefectWords.append(word)
        else:
            #if see it again it is prefect
            if word in imprefectWords: 
                imprefectWords.remove(word)
            else:
                imprefectWords.remove(reverseComplement(word))
            prefectWords.append(word)
    #find the correct match between prefect and imprefect words
    matches={}
    for imprefect in imprefectWords:
        for prefect in prefectWords:
            if hammingDistance(imprefect,prefect)==1:
                matches[imprefect]=prefect
            #check for reverse compliment
            if hammingDistance(imprefect,reverseComplement(prefect))==1:
                matches[imprefect]=reverseComplement(prefect)
    return matches
    # print(prefectWords)
    # print(imprefectWords)
    # print(matches)



# Parse the input data.
words = [fasta[1] for fasta in ReadFASTA('12_input.txt')]
matches=correction(words)
for key,value in matches.items():
    print(key+"->"+value)