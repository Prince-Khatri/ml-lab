# Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis based on a set of training data samples. 
# Create your own dataset with minimum 4 attributes.

def find_s(data):
    hypo=[None]*(data[0].size()-1)
    for d in data:
        if d[-1] == "Yes":
            for i in range(0,len(data[0])-1):
                if hypo[i]==None:
                    hypo[i] = d[i]
                    continue
                elif hypo[i]!=d[i]:
                    hypo[i]='?'
    
    return hypo



training_data = [
    ['Sunny','Warm','Normal', 'Strong', 'Yes'],
    ['Sunny','Warm','High', 'Strong', 'Yes'],
    ['Rainy','Cold','High', 'Strong', 'No'],
    ['Sunny','Warm','Normal', 'Weak', 'Yes'],
]

print(find_s(training_data))
