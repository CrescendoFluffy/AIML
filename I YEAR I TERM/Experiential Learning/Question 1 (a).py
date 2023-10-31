# 1)Identifying the Replicated data and remove those data from the record using PYTHON
# a)Create a list for each case (i.e. Two wheelers, Mid-range cars, High end cars) and remove the replicated names in each list using appropriate Python function.

# Lists of persons owning different types of vehicles
two_wheelers = [
    "Raju",
    "Ravi",
    "Anusha",
    "Arun",
    "Arjun",
    "Kailash",
    "Kishore",
    "Raghu",
    "Ramu",
    "Abhilash",
    "Arun",
    "Kavitha",
    "Karan",
    "Kiran",
    "Kumar",
    "Arjun",
    "Ramu",
    "Aravind",
    "Randheer",
    "Shyam",
]
mid_range_cars = [
    "Rahul",
    "Ravi",
    "Anusha",
    "Ashok",
    "Ismail",
    "Prabhu",
    "Rajesh",
    "Randheer",
    "Shyam",
    "Nandan",
    "Arun",
    "Arjun",
    "Kailash",
    "Kiran",
    "Sandeep",
    "Dinesh",
    "Sravan",
    "Kumar",
    "Arjun",
    "Raju",
]
high_end_cars = [
    "Lokesh",
    "Teja",
    "Arundathi",
    "Sharma",
    "Devendra",
    "Prasad",
    "Kumari",
    "Prasanna",
    "Lalitha",
    "Kiran",
    "Kumar",
    "Arjun",
    "Ramu",
    "Arjun",
    "Kailash",
    "Kiran",
    "Randheer",
    "Shyam",
]

# Remove replicated names using sets
two_wheelers = list(set(two_wheelers))
mid_range_cars = list(set(mid_range_cars))
high_end_cars = list(set(high_end_cars))

# Print the updated lists without replicated names
print("Two Wheelers:", two_wheelers)
print("Mid-range Cars:", mid_range_cars)
print("High-end Cars:", high_end_cars)