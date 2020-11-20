def make_mean(a,b,c):
    mean = (round((a+b+c)/3,2))
    if mean >= 90 :
        grade = 'A'
    elif mean >= 80 :
        grade = 'B'
    elif mean >=70:
        grade = 'C'
    elif mean >= 60 :
        grade = 'D'
    else:
        grade = 'F'
    mean_list = (mean,grade)
    return mean_list


a,b,c = map(int,input().split())
list = make_mean(a,b,c)
print ('%.2f'%list[0],list[1])