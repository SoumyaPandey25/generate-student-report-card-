roll=[]
name=[]
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]
total=[]

n=int(input("Enter number of student"))
for i in range(n):
    x=int(input("Enter roll no.:"))
    roll.append(x)
    x=input("Enter name of student")
    name.append(x)
    x=int(input("Enter marks1 of student:"))
    m1.append(x)
    x=int(input("Enter marks2 of student:"))
    m2.append(x)
    x=int(input("Enter marks3 of student:"))
    m3.append(x)
    x=int(input("Enter marks4 of student:"))
    m4.append(x)
    x=int(input("Enter marks5 of student:"))
    m5.append(x)
    total.append(m1[i]+m2[i]+m3[i]+m4[i]+m5[i])
ch='Y'
while ch=='Y' or ch=='y':
    print("1. PRINT TABULAR DATA")
    print("2. PRINT REPORT CARD")
    m=int(input("Enter option:"))
    if m==1:
        print("ROLL NO\t\tNAME\tMARKS1\tMARKS2\tMARKS3\tMARKS4\tMARKS5\tTOTAL")
        print("------------------------------------------------------------------------------")
        for i in range(n):
            print(roll[i],end='\t\t')
            print(name[i],end='\t')
            print(m1[i],end='\t')
            print(m2[i],end='\t')
            print(m3[i],end='\t')
            print(m4[i],end='\t')
            print(m5[i],end='\t')
            print(total[i])
    if m==2:
        max1=m1[0]
        max2=m2[0]
        max3=m3[0]
        max4=m4[0]
        max5=m5[0]
        for i in range(n):
            if m1[i]>max1:
                max1=m1[i]
            if m2[i]>max2:
                max2=m2[i]
            if m3[i]>max3:
                max3=m3[i]
            if m4[i]>max4:
                max4=m4[i]
            if m5[i]>max5:
                max5=m5[i]
        f=0
        x=int(input("Enter roll no. of student whoes Report card you want:"))
        print("\t\t\tREPORT CARD")
        for i in range(n):
            if roll[i]==x:
                f=1
                print("ROLL NO,:",roll[i])
                print("NAME OF STUDENT:",name[i])
                print("-------------------------------------------------------------------------------")
                print("SUBJECT\t\tMARKS OBTAINED\t\tHIGHEST MARKS")
                print("PHYSICS\t\t",m1[i],"\t\t\t",max1)
                print("MATHEMATICS\t",m2[i],"\t\t\t",max2)
                print("ENGLISH\t\t",m3[i],"\t\t\t",max3)
                print("CHEMISTRY\t",m4[i],"\t\t\t",max4)
                print("COMPUTER SCIENCE",m5[i],"\t\t\t",max5)
                print("-------------------------------------------------------------------------------")
                print("TOTAL MARKS",total[i])
        if(f==0):
            print("ROLL NO. DOESN'T EXIST")
    ch=input("DO YOU WANT TO CONTINUE(Y/N)?:")
