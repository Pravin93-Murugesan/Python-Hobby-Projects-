#!/usr/bin/env python
# coding: utf-8

# In[8]:


# frequency distribution of the letters in any large text data
letter_frequency = {'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32, 'E': 12.0, 
                    'F': 2.3,  'G': 2.03, 'H': 5.92, 'I': 7.31, 'J': 0.1, 
                    'K': 0.69, 'L': 3.98, 'M': 2.61, 'N': 6.95, 'O': 7.68, 
                    'P': 1.82, 'Q': 0.11, 'R': 6.02, 'S': 6.28, 'T': 9.1, 
                    'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17, 'Y': 2.11, 'Z': 0.07}


# In[9]:


file = open("Encrypted_data.txt","r")
test_str = file.read().upper()

res = {} 
for keys in test_str: 
    res[keys] = res.get(keys, 0) + 1

# Display characters
print ("Count of all characters in the encrypted file is :\n" + str(res)) 

from string import ascii_uppercase
results = {x:res[x] for x in ascii_uppercase}
print ("\nCount of only characters is :\n" + str(results))


# In[10]:


sum = 0
for i in results.keys():
    sum = sum + results[i]

for i in results.keys():
    results[i] = (results[i]/sum)*100
    results[i] = round(results[i], 2)

print(results)


# In[11]:


import matplotlib.pylab as plt

ELF_sorted = sorted(letter_frequency.items()) # sorted by key
X, Y = zip(*ELF_sorted) # unpacks a list of pairs into two tuples

maxValue = max(letter_frequency, key=letter_frequency.get)
letter_frequency = list(letter_frequency)

plt.figure(figsize=(10,6))
bar_plot = plt.bar(X, Y, width=0.6)
bar_plot[letter_frequency.index(maxValue)].set_color('g')
plt.show()


results_sorted = sorted(results.items()) # sorted by key
x, y = zip(*results_sorted) # unpacks a list of pairs into two tuples

maxValue2 = max(results, key=results.get)
results = list(results)

plt.figure(figsize=(10,6))
bar_plot = plt.bar(x, y, width=0.6)
bar_plot[results.index(maxValue2)].set_color('r')
plt.show()


# In[12]:


from string import ascii_lowercase as strs                  # strs = 'abcdefghijklmnopqrstuvwxyz' 
file = open("Encrypted_data.txt","r")

def decipher(shift):
    inp = file.read().lower()
    out = []
    for i in inp:                                           # iterate over the text 
        if i in strs and i.strip():                         # if the char is not a space " "  
            out.append(strs[(strs.index(i) - shift) % 26])  
        #elif '\n' in i:
            #out = '\n'.join(out)
            #out.append('NL')                               # if it's a space, then simply append to data
        else:
            out.append(i)                                   # if it's a space, then simply append to data
    output = ''.join(out)
    return output

shift_val = results.index(maxValue2) - letter_frequency.index(maxValue)
decipher(shift_val)


# In[ ]:




