# 1) b) List out the people who are owning anyone of the vehicle in the region using appropriate Python function

# Create sets to store unique owners of each type of vehicle
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
# Merge the sets to get a unique list of all owners
all_owners = two_wheelers.union(mid_range_cars, high_end_cars)

# Convert the set to a sorted list
all_owners_list = sorted(list(all_owners))

# Print the list of people who own any of the vehicles
for owner in all_owners_list:
    print(owner)
