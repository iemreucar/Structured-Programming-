def compare_sum (list,target):
    for i in range (len(list)):
        for j in range (i+1,len(list)):
            for k in range (j+1,len(list)):
                sum=list[i]+list[j]+list[k]
                if sum==target:
                    return True
    else:
        return False
        
print(compare_sum([1,2,3,4,5],2))


name = "Ayşe"
age = 30
print("Merhaba, ben %s. %d yaşındayım." % (name, age))
average=100

print("Average: {:.2f} centigrat degrees".format(average))


floatNumber = 1.9876
print("%.2f" % floatNumber)

name = "Ayşe"
age = 30
print("Merhaba, ben %s. %d yaşındayım." % (name, age))
# Çıktı: Merhaba, ben Ayşe. 30 yaşındayım.

num1 = 10
num2 = 5
print(f"{num1} ile {num2} toplamı: {num1 + num2}")
# Çıktı: 10 ile 5 toplamı: 15

name = "Ahmet"
age = 25
print("Merhaba, ben {}. {} yaşındayım.".format(name, age))
# Çıktı: Merhaba, ben Ahmet. 25 yaşındayım


size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)