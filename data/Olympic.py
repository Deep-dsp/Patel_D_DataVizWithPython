import matplotlib.pyplot as plt
import csv

golds = []
silvers = []
bronzes = []

categories = [] #first row -> not data 

with open('data/MenMedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0


	for row in reader:
		if line_count is 0:
			print("this is the first roe in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("Won a gold medal")
				golds.append(row[7])

			elif row[7] == "Silver":
				print("Won a silver medal")
				silvers.append(row[7])

			else:
				print("Won a Bronze medal")
				bronzes.append(row[7])


			print(line_count)
			line_count += 1

print("************************************")
print("total gold medals :", len(golds))
print("************************************")
print("************************************")
print("total silver medals :", len(silvers))
print("************************************")
print("************************************")
print("total bronze medals :", len(bronzes))
print("************************************")


labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
color = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=color, autopct='%1.f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Hockey Medal Wins -Historic Medal Counts")
plt.xlabel("Medal counts since 1924")
plt.show()

		

