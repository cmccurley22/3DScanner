import csv
import matplotlib.pyplot as plt

# calibration function into inches
def convert_to_inches(data):
  return 7.49078357932937710**-5 * data**2 + (-0.0972 * data) + 38.6755

with open("letterM.csv") as f:
  r = csv.reader(f)

  points = [[], []]
  for row in r:
    if int(convert_to_inches(int(row[2]))) > 18:
      points[0].append(int(row[0]) - 90) # subtract start point in degrees
      points[1].append(int(row[1]) - 50) # substract start point in degrees

# re-center data (due to scanner movement in opposite directions)
for i in range(len(points[0]) - 1):
    if int(points[1][i]) > int(points[1][i + 1]):
      points[1][i] += 2 
    else:
      points[1][i] -= 2


plt.scatter(points[1], points[0], color = "green")

plt.xlim([0, 45])
plt.ylim([0, 30])
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("Generated Scan of the Letter A")

plt.show()