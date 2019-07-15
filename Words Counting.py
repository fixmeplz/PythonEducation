# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального 
# слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
s = input().lower().split()
s2=[]
q=''
q2=''
n=1
for i in range(0, len(s)):
  for j in range(0, len(s)):
    if s[i]==s[j] and i!=j:
      n+=1
      q=s[i]+' '+str(n)
    else:
      q2=s[i]+' '+str(1)
  if q not in s2 and n>1:
    s2+=[q]
  elif q2 not in s2 and n==1:
    s2+=[q2]
  n=1

for i in range(0, len(s2)):
  print(s2[i])
