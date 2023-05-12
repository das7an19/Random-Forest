import csv

headers = ["Sales", "Competitor Price", "Income", "Advertising", "Population", "Price",
           "Shelf Location at stores", "Age", "Education", "Urban", "US"]

data = [
    [10, 5, 50, 10, 100, 20, "Good", 30, "High", "Yes", "Yes"],
    [15, 6, 60, 8, 120, 22, "Medium", 35, "Low", "No", "Yes"],
    
]


file_path = "your_dataset.csv"  

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print("Файл данных успешно создан:", file_path)
