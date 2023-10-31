# 1) d) Identify the people who are owning both the Mid-range cars and High end cars using appropriate Python function

# Define the sets for mid-range cars and high-end cars
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
# Find the intersection of the two sets to get the common owners
common_owners = mid_range_cars.intersection(high_end_cars)

# Convert the set to a sorted list for easy viewing
common_owners_list = sorted(list(common_owners))

# Print the list of people who own both mid-range cars and high-end cars
for owner in common_owners_list:
    print(owner)
