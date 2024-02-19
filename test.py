import time

 
name = input("What's your name? ")
 
print("Hi", name + "!")

 
print("Welcome to Schatz:")

# Get current time
current_time = time.strftime("%H:%M:%S")

# Example data (you can replace this with your own data)
data = {
  "current_time": current_time
}

# Print the data
for key, value in data.items():
    print(key + ":", value)
