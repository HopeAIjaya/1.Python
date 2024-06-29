class multiplefunction():
     def Subfields():
        list=['Machine learning','Neural Networks','Vision','Rootics','Speech processing','Natural language processing']
        print("sub-filds in AI are:")
        for i in list:
            print(i)  
            
     def oddEven():
        num=int(input("Enter a number:"))
        if num%2==0:
            print(num,"is Even number")
        else:
            print(num,"is odd number")
            
     def ElegiblityForMarriage():
        gender = input("your Gender: ")
        age    = int(input("your age:"))
        if(gender=='Male' and age>=21) or (gender=='Female' and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")
            
     def percentage():
        mark1=int(input("Subject1="))
        mark2=int(input("Subject2="))
        mark3=int(input("Subject3="))
        mark4=int(input("Subject4="))
        mark5=int(input("Subject5="))
        total_ob=mark1+mark2+mark3+mark4+mark5
        per=(total_ob/500)*100
        print("Total:468")
        print("percentage:",per)
         
     def triangle():
        length=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(length*breadth)/2
        print("area of triangle:",area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeter=Height1+Height2+Breadth
        print("perimeter of Triangle:",perimeter)