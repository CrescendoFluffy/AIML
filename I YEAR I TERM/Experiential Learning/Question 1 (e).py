# 1) e) List out the people who are owning all the three vehicles in the region using appropriate Python function

# Define sets for each type of vehicle owner
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
high_end_cars = set(
    [
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
)
# Find the intersection of the three sets to get the common owners
common_owners = two_wheelers.intersection(mid_range_cars, high_end_cars)

# Convert the set to a sorted list for easy viewing
common_owners_list = sorted(list(common_owners))

# Print the list of people who own all three types of vehicles
for owner in common_owners_list:
    print(owner)
