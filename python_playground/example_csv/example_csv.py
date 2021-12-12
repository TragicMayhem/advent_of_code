import csv
from datetime import datetime

path = "./google_stock_market .csv"
file = open(path)

print("\n**** Not using the csv module ****\n")

# Prints out the lines of the file
# for line in file:
#     print(line)

# Using list comprehension
lines = [line for line in open(path)]
print(lines[0])
print(lines[1])

# Strip the spaces and new lines
print("<< --- lines[0] * has a \\n at end  >>")
clean_line = lines[0].strip()
clean_split = lines[0].strip().split(',')
print(lines[0])
print("<< --- clean_line * no new line >>")
print(clean_line)
print("<< End >>")
print(clean_split)

print("\n\nReading into list split directly")
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])

print("\n**** CSV module ****\n")
print(dir(csv))
print("\n")

file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # Reads the first line which is a header

# data is still processed as strings
data = [row for row in reader]  # Read the remaining data
print(header)
print(data[0])

file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # Reads the first line which is a header

print("\nCorrecting datatypes")
data_correct_types = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj Close]
    date = datetime.strptime(row[0], "%m/%d/%Y")
    open_price = float(row[1])
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data_correct_types.append([date, open_price, high_price, low_price,
                               close_price, volume, adj_close])

print(data_correct_types[0])

print("\nWriting out a daily returns file")
# compute the daily returns
returns_path = "./google_returns.csv"
file = open(returns_path, 'w', newline='')  # Use newline='' to not add new line
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

# stop at the send to last row, because of the daily comparison
for i in range(len(data_correct_types) - 1):
    todays_row = data_correct_types[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data_correct_types[i + 1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price

    formatted_date = todays_date.strftime('%m/%d/%Y')
    formatted_change = "{0:.5f}".format(daily_return)
    writer.writerow([formatted_date, formatted_change])
