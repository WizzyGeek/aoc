import re;(lambda d:sum((((s>=i)&(j>=t))|((i>=s)&(t>=j)))+1j*((i<=t)&(s<=j))for i,j,s,t in map(lambda u:list(map(int,re.split("[-,]",u))),d)))(open("input.txt","r").read().split())