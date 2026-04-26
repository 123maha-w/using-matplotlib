import matplotlib.pyplot as plt
import numpy as np

products=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]
total_units=[2100,2100,3550,3700,8300,14400]

perc=[]
for x in total_units:
    res = (x/50)*10
    perc.append(res)

    print(perc)

    y1 = np.array([1200, 3000, 1234, 1300])

def marks_line_chart():
    plt.plot(products,total_units,y1,linestyle='dashed',color='r')
    plt.title("products graph")
    plt.xlabel("products")
    plt.ylabel("amount")
    plt.plot(y1)
    plt.show()

marks_line_chart()

def percentage_bar_chart():
    plt.bar(products,perc,color='black')
    plt.title("products percentage graph")
    plt.xlabel("products")
    plt.ylabel("amount percentage")
    plt.show()

percentage_bar_chart()



