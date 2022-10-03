import serial
import csv

arduino_com_port = "COM6"
baud_rate = 9600

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout = 1)


reading_data = True
data = [[], [], []]

while reading_data:
  line_of_data = serial_port.readline().decode()
  if len(line_of_data) > 0:
    # print values for debugging
    # print("sensor value: " + line_of_data)

    # check if our scan is complete
    if "end" in line_of_data:
      reading_data = False
    else:
      # if not complete, add to data matrix
      data[0].append(int(line_of_data.split(", ")[0]))
      data[1].append(int(line_of_data.split(", ")[1]))
      data[2].append(int(line_of_data.split(", ")[2]))

# write data to CSV
with open("letterA.csv", "w", newline = "") as f:
  w = csv.writer(f)
  for i in range(len(data[0])):
    w.writerow([data[0][i], data[1][i]], data[2][i])
