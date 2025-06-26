import csv
# 1) Να βαλετε το περιεχομενο το csv σε μια λιστα απο λεξικα
csvPath = './sales.csv'
def read_data(data_file):
    data=[]
    with open(data_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append({
                'Ημερομηνία':row['Ημερομηνία'],
                'Προϊόν':row['Προϊόν'],
                'Ποσότητα':int(row['Ποσότητα']),
                'Τιμή_Μονάδας':float(row['Τιμή_Μονάδας'])
            })
    return data

x=read_data(csvPath)
# print(x)

# 2) Να βρειτε την πιο κερδοφορα μερα(ημερομηνία)
def profitable_day(data):
    days_max=[]
    maxSale=0
    examinedDate=data[0]['Ημερομηνία']
    for i in range(len(data)):
        if examinedDate == data[i]['Ημερομηνία']:
            maxSale=maxSale+(data[i]['Ποσότητα']*data[i]['Τιμή_Μονάδας'])
        else:
            days_max.append({'examinedDate':examinedDate,"salesTotal":maxSale})
            examinedDate=data[i]['Ημερομηνία']
            maxSale=0
    
    print(days_max)
    localMax=0
    for i in range(len(days_max)):
        if days_max[i]["salesTotal"] >localMax:
            localMax =days_max[i]["salesTotal"]
            new_best = {'bestDate':days_max[i]['examinedDate'],'bestSale':localMax}
    print(new_best)

profitable_day(x)     

# 3) Να βρειτε τον μεσωνια την τιμη των προϊν
def average_prices(data):
    products_avgs=[]
    uniqueProducts= set()
    uniqueProductsArray=[]
    for i in range(len(data)):
        uniqueProducts.add(data[i]['Προϊόν'])
    uniqueProductsArray.extend(uniqueProducts)

    product_revenue =0
    product_counter=0
    for i in range(len(uniqueProductsArray)):
        for j in range(len(data)):
            if uniqueProductsArray[i]==data[j]['Προϊόν']:
                product_revenue=product_revenue+(data[j]['Ποσότητα']*data[j]['Τιμή_Μονάδας'])
                product_counter=product_counter+1
        product_avg=product_revenue/product_counter
        products_avgs.append({"product_name":uniqueProductsArray[i],"average_price":product_avg})
    print(f"The average prices are:\n{products_avgs}")

average_prices(x)

# 4) Να βρειτε το πιο κερδοφορο και τον πιο χαμηλο προϊον σε πωλησεις.
def min_max_sales(data):
    products_total_sales=[]
    uniqueProducts= set()
    uniqueProductsArray=[]
    for i in range(len(data)):
        uniqueProducts.add(data[i]['Προϊόν'])
    uniqueProductsArray.extend(uniqueProducts)

    product_sales_counter=0
    for i in range(len(uniqueProductsArray)):
        for j in range(len(data)):
            if uniqueProductsArray[i]==data[j]['Προϊόν']:
                product_sales_counter = product_sales_counter + data[j]['Ποσότητα']
    products_total_sales.append({"product_name":uniqueProductsArray[i],"total_sales":product_sales_counter})
    product_sales_counter=0

    minSales=100000
    maxSales=0
    min_product={}
    max_product={}
    for i in range(len(products_total_sales)):
        if products_total_sales[i]["total_sales"]>maxSales:
            maxSales=products_total_sales[i]["total_sales"]
            max_product={"product_name":products_total_sales[i]["product_name"],"total_sales":maxSales}
        if products_total_sales[i]["total_sales"]<minSales:
            minSales=products_total_sales[i]["total_sales"]
            min_product={"product_name":products_total_sales[i]["product_name"],"total_sales":minSales}
    
    print(f"Best Performing product:\n{max_product}")
    print(f"Least Performing product:\n{min_product}")

min_max_sales(x)