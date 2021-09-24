import random

def train_test_split(x, test_size = 0.1):
    
    xt = {}
    
    x_temp = {}
    
    len_x = len(x)
    
    test_len = int(test_size * len_x)
    
    test = random.sample(list(range(len_x)), test_len)
    
    j,k = 0,0
    
    for i in range(len_x):
        
        if i in test:
            
            xt[str(j)] = x[str(i)]
            
            j += 1
            
        else:
            
            x_temp[str(k)] = x[str(i)]
            
            k += 1
            
    x = x_temp
    
    return x, xt

#%%
''' 
Sample Code:
    
x = {'0':[0,0,0],'1':[0,0,1],'2':[0,1,0],'3':[0,1,1],'4':[1,0,0],'5':[1,0,1],'6':[1,1,0],'7':[1,1,1]}

x, xt = train_test_split(x,0.4)

print(x)
print(xt)

Expected Output:
{'0': [0, 1, 0], '1': [0, 1, 1], '2': [1, 0, 0], '3': [1, 0, 1], '4': [1, 1, 1]}
{'0': [0, 0, 0], '1': [0, 0, 1], '2': [1, 1, 0]}
'''