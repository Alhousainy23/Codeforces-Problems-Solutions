# Solider and Bananes Problem 
cost , num_of_times,banana = map(int,input().split())
# Equaion to calculate the cost 
total_cost = cost *(banana *(banana+1)//2)
#Equation to calculate the borrow_cost we are neded 
borrow_cost = total_cost -num_of_times
#Make condition for borrow_cost = negative or 0 ==> don't rent money 
if borrow_cost<0 : borrow_cost =0
print(borrow_cost)

'''
# قراءة الإدخال k, n, w
k, n, w = map(int, input().split())

# حساب التكلفة الإجمالية
total_cost = k * (w * (w + 1) // 2)

# حساب المبلغ المطلوب للاستعارته
borrow = total_cost - n

# إذا كانت النتيجة سالبة أو صفر، الجندي لا يحتاج لاستعارة المال
if borrow < 0:
    borrow = 0

# طباعة النتيجة
print(borrow)
'''