from queue import PriorityQueue

import pandas
data=pandas.read_csv("squirrel_data.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])
data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]

}
squirrel_data=pandas.DataFrame(data_dict)
squirrel_data.to_csv("Squirrel_count.csv")