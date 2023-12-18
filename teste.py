import random 
test_list = ["a", "b", "c", "d", "e"] 
print ("The original list is : " + str(test_list)) 
res = random.sample(test_list, len(test_list)) 
print ("The shuffled list is : " +  str(res)) 