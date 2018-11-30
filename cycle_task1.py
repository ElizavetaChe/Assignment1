school_scores=[{'school_class':'1a','scores':[4,5,5,3,4]},
                 {'school_class':'1b','scores':[3,3,5,5,4]},
                 {'school_class':'1c','scores':[2,5,5,3,4]},
                 {'school_class':'2a','scores':[5,5,5,3,4]},
                 {'school_class':'2b','scores':[4,4,3,5,4]}]

results={}
total_sum=0
total_num=0
for element in school_scores:
    sum_scores=0 
    num_scores=0
    avg_scores=0  
    for key, val in element.items():
        if key=='school_class':
            key1=val
            results.update({val:avg_scores})
        elif key=='scores':
            for num in val:
                total_sum+=num
                sum_scores+=num
                total_num+=1
                num_scores+=1
                avg_scores=sum_scores/num_scores
                val1=str(avg_scores)
                results.update({key1:val1})
results.update({'total_avg': str(total_sum/total_num)})
print(results)


   

