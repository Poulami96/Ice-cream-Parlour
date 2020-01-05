import csv
import datetime
file = 'sales-data.csv'

#Total sales of the store.

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    sum1=0
    for row in rd:
        sum1=sum1+int(row['Total Price'])
    print("Total sales of the store: ")
    print(sum1)

#Month wise sales totals in month1,2,3 simultaneously

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    sum2=0
    for row in rd:
        i=1
        date_time_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        if(i==date_time_obj.month):
            sum2=sum2+int(row['Total Price'])
    print("Total sale in month 1:")
    print(sum2)

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    sum2=0
    for row in rd:
        i=2
        date_time_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        if(i==date_time_obj.month):
            sum2=sum2+int(row['Total Price'])
    print("Total sale in month 2:")
    print(sum2)

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    sum2=0
    for row in rd:
        i=3
        date_time_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        if(i==date_time_obj.month):
            sum2=sum2+int(row['Total Price'])
    print("Total sale in month 3:")
    print(sum2)

#--------------------------------------------------------------------------

with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    SK1=[]
    SK2=[]
    SK3=[]

    for row in rd:
        date_time_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        if(date_time_obj.month==1):
            SK1.append(row)
        elif(date_time_obj.month==2):
            SK2.append(row)
        else:
            SK3.append(row)

    # Most popular item (most quantity sold) and Items generating most revenue in month 1,2,3 simultaneously.

    my_list = ['Rocky Road Double Scoop', 'Pista Single Scoop', 'Fig and Honey Single Scoop', 'Almond Fudge', 'Cafe Caramel', 'Chocolate Europa Single Scoop', 'Dew Drop Sundae', 'Caramel Crunch Single Scoop', 'Caramel Crunch Double Scoop', 'Hot Chocolate Fudge', 'Fig and Honey Double Scoop', 'Vanilla Single Scoop', 'Dry Fruit Double Scoop', 'Butterscotch Single Scoop', 'Vanilla Double Scoop', 'Butterscotch Double Scoop', 'Mint Fudge', 'Cake Fudge', 'Death by Chocolate', 'Rocky Road Single Scoop', 'Dry Fruit Single Scoop', 'Banana Split', 'Pista Double Scoop', 'Chocolate Europa Double Scoop', 'Trilogy']

    dict1={}
    rev1={}
    for i in range(0,len(my_list)):
        q=0
        r=0
        for j in range(0,len(SK1)):
            if(SK1[j]['SKU']==my_list[i]):
                q+=int(SK1[j]['Quantity'])
                r+=int(SK1[j]['Total Price'])
        dict1.update({my_list[i]:q})
        rev1.update({my_list[i]:r})
    quantity1 = max(dict1, key=dict1.get) 
    revenue1 = max(dict1, key=rev1.get) 
    print("Most popular item of month 1:" + quantity1) 
    print("Items generating most revenue in month 1:" + revenue1)

    dict2={}
    rev2={}
    for i in range(0,len(my_list)):
        q=0
        r=0
        for j in range(0,len(SK2)):
            if(SK2[j]['SKU']==my_list[i]):
                q+=int(SK2[j]['Quantity'])
                r+=int(SK2[j]['Total Price'])
        dict2.update({my_list[i]:q})
        rev2.update({my_list[i]:r})
    quantity2 = max(dict2, key=dict2.get) 
    revenue2 = max(dict2, key=rev2.get) 
    print("Most popular item of month 2:" + quantity2) 
    print("Items generating most revenue in month 2:" + revenue2)

    dict3={}
    rev3={}
    for i in range(0,len(my_list)):
        q=0
        r=0
        for j in range(0,len(SK3)):
            if(SK3[j]['SKU']==my_list[i]):
                q+=int(SK3[j]['Quantity'])
                r+=int(SK3[j]['Total Price'])
        dict3.update({my_list[i]:q})
        rev3.update({my_list[i]:r})
    quantity3 = max(dict3, key=dict3.get) 
    revenue3 = max(dict3, key=rev3.get) 
    print("Most popular item of month 3:" + quantity3) 
    print("Items generating most revenue in month 3:" + revenue3)
    
  
    #For the most popular item, find the min, max and average number of orders for month 1,2,3 simultaneously

    data1=[]
    summ1=0
    for i in range(0,len(SK1)):
        if(SK1[i]['SKU']==quantity1):
            data1.append(SK1[i]['Quantity'])
            print(min(data1))
            print(max(data1))
            summ1+=int(SK1[i]['Quantity'])
            avg=summ1/len(SK1[i])
            print(avg)


    data2=[]
    summ2=0 
    for i in range(0,len(SK2)):
        if(SK2[i]['SKU']==quantity2): 
            data2.append(SK2[i]['Quantity'])
            print(min(data2))
            print(max(data2))
            summ2+=int(SK2[i]['Quantity'])
            avg=summ2/len(SK2[i])
            print(avg)


    data3=[]
    summ3=0 
    for i in range(0,len(SK3)):
        if(SK3[i]['SKU']==quantity3): 
            data3.append(SK3[i]['Quantity'])
            print(min(data3))
            print(max(data3))
            summ3+=int(SK3[i]['Quantity'])
            avg=summ3/len(SK3[i])
            print(avg)
        
        
        


        
       
        