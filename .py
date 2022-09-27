import matplotlib.pyplot as plt

def main():
    x_axis = [1,2,3,4,5]
    y_axis = [2,5,2,1,3]

    plt.plot(x_axis,y_axis,color='red')
    plt.title('Sale of year')
    plt.xlabel('Year')
    plt.ylabel('Sale')

    plt.yticks([1,2,3,4,5],['$1M','$2M','$3M','$4M','$5M'])
    plt.xticks(x_axis,['2020','2021','2022','2023','2024'])

    plt.grid(True)
    plt.show()

main()