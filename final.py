def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    results={}
    frequencies = file_contents.split()
    for words in frequencies:
        words = words.lower()
        if words in uninteresting_words:
            pass
        else:
            for x in punctuations:
                for letter in words:
                    if x in letter:
                        letter.replace(x,"")
                    if words not in results.keys():
                        results[words] = 0
                    else:
                        results[words] = 1
    return results
                       
           
print(calculate_frequencies(file_contents))
