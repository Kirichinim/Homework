print('Введите, пожалуйста, число и степень счисления в котором вы хотите его наблюдать.')
a,b=input().split()
def Perevod(a,b):
    s=0
    st=''
    x=['A', 'B', 'C', 'D', 'E', 'F']
    try:
        a=int(a)
        b=int(b)
    except:
            print('Вы ввели что-то не то, сорян')
    else:
        while a>0:
            s=a%b
            if s>=10:
                s=x[s-10]
            else:
                s=str(s)
            st+=s
            a=a//b
    st[::-1]
    return st
n=Perevod(a,b)
n_list=list(n)
n_list.reverse()
nk= "".join(n_list)
print(nk)

