# 1) c) Identify the people who are owning both the two wheelers and Mid-range cars using appropriate Python function

# Define the sets for two wheelers and mid-range cars
two_wheelers = set(
    [
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
)
mid_range_cars = set(
    [
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
)
# Find the intersection of the two sets to get the common owners
common_owners = two_wheelers.intersection(mid_range_cars)

# Convert the set to a sorted list for easy viewing
common_owners_list = sorted(list(common_owners))

# Print the list of people who own both two wheelers and mid-range cars
for owner in common_owners_list:
    print(owner)
