import pandas


dictionary = {
    'Name': ["John", "Cindy", "Mark", "Abraham", "Kevin"],
    'ID': ["1", "2", "3", "4", "5"],
    'Favroite Food': ["Pizza", "Pasta", "Fries", "burger", "donut"]

}




print(pandas.DataFrame(dictionary).set_index('ID'))

