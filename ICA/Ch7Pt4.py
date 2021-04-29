# Week 12, ICA 2
import matplotlib.pyplot as plt

def main():
    premier = ('Liverpool','Chelsea','Arsenal','Southampton')
    mls = ('LAFC','LA Galaxy','DC United','Sporting KC')
    for epl in premier:
        print(epl)
    print()
    for x in range(4):
        print(mls[x])
    #unpack MLS tuple
    mls1, mls2, mls3, mls4 = mls
    print()
    print(mls1,'and',mls2,'and',mls3,'and',mls4)
    soccer_teams = list(premier)
    soccer_teams.append(mls1)
    soccer_teams.append(mls2)
    soccer_teams.append(mls3)
    soccer_teams.append(mls4)
    print(soccer_teams)
    soccer_teams2 = tuple(soccer_teams)
    print(soccer_teams2)

    # Part 2
    plt.figure()
    # Create lists with x, y coordinates
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords, y_coords, marker='o') # Build the line graph
    plt.title('Sales by Year') # Add a Title
    # Add labels to the axis
    plt.xlabel('Year')
    plt.ylabel('Sales')
    # Customize the tick markers
    plt.xticks([0,1,2,3,4], ['2016','2017','2018','2019','2020'])
    plt.yticks([0,1,2,3,4,5], ['$0M','$1M','$2M','$3M','$4M','$5M'])    
    plt.grid(True) # Add a Grid
    plt.show() # Display the line graph

    plt.figure()
    # Bar Graph - left edges
    left_edges = [0,10,20,30,40]

    # Bar Height
    heights = [100,200,300,400,500]

    bar_width = 10

    # Build Bar Chart
    plt.bar(left_edges, heights, bar_width, color=('r','g','b','m','y'))

    # Add a title 
    plt.title('Sales by Year')

    # Add labels to axis
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick markers
    plt.xticks([0,15,25,35,45], ['2016','2017','2018','2019','2020'])
    plt.yticks([0,100,200,300,400,500], ['$0M','$1M','$2M','$3M','$4M','$5M'])

    # Show the bar graph
    # plt.show()

    # Pie chart - sales amounts
    plt.figure()
    sales = [100,400,300,600]

    # labels for pie slices
    slice_labels = ['1st Qtr','2nd Qtr','3rd Qrt', '4th Qtr']

    # create pie chart
    plt.pie(sales,labels=slice_labels,colors=('r','g','m','b'))

    # create title
    plt.title('Sales by Quarter')

    # show pie chart
    plt.show()


main()