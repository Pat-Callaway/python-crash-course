guests = ['Christopher', 'Susan', 'Bill', 'Satya']
print(f"Hello, {guests[0]}! I am inviting you to dinner.")
print(f"Hello, {guests[1]}! I am inviting you to dinner.")
print(f"Hello, {guests[2]}! I am inviting you to dinner.")
print(f"Hello, {guests[3]}! I am inviting you to dinner.")
# Output:
# Hello, Christopher! I am inviting you to dinner.
# Hello, Susan! I am inviting you to dinner.
# Hello, Bill! I am inviting you to dinner.
# Hello, Satya! I am inviting you to dinner.

# Path: 3_5_Changing_Guest_List.py
print(f"{guests[0]} can't make it to dinner.")
guests[0] = 'Steve'
print(f"Hello, {guests[0]}! I am inviting you to dinner.")
print(f"Hello, {guests[1]}! I am inviting you to dinner.")  
print(f"Hello, {guests[2]}! I am inviting you to dinner.")
print(f"Hello, {guests[3]}! I am inviting you to dinner.")

#3_6_More_Guests.py

print("I found a bigger table!")
guests.insert(0, 'Alice')
guests.insert(2, 'Bob')
guests.append('Charlie')    
print(f"Hello, {guests[0]}! I am inviting you to dinner.")
print(f"Hello, {guests[1]}! I am inviting you to dinner.")
print(f"Hello, {guests[2]}! I am inviting you to dinner.")
print(f"Hello, {guests[3]}! I am inviting you to dinner.")
print(f"Hello, {guests[4]}! I am inviting you to dinner.")
print(f"Hello, {guests[5]}! I am inviting you to dinner.")
print(f"Hello, {guests[6]}! I am inviting you to dinner.")

#3_7_Shrinking_Guest_List.py
 # pop() removes the last item in the list
 # append() adds an item to the end of the list

print("I can only invite two people to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest}. I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest}. I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest}. I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest}. I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest}. I can't invite you to dinner.")
print(f"Hello, {guests[0]}. You're still invited.")
print(f"Hello, {guests[1]}. You're still invited.")
del guests[0]
del guests[0]
print(guests)


# 3_8_Seeing_the_World.py

locations = ['Paris', 'Tokyo', 'New York', 'London', 'Sydney']
print(locations)
# Output: This will print the list in alphabetical order
print(sorted(locations))
# Output: Showing the list in the orginal state after the sorted() function
print(locations)
# Output: Showing the list in reverse alphabetical order
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3_9_Dinner_Guests.py
print(f"I am inviting {len(guests)} guests to dinner.")

# 3_10_Every_Function.py
mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']
rivers = ['Nile', 'Amazon', 'Yangtze', 'Mississippi', 'Yenisei']
countries = ['USA', 'China', 'Russia', 'Canada', 'Brazil']  
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City']
languages = ['English', 'Mandarin', 'Hindi', 'Spanish', 'French']

print(sorted(mountains))
mountains.sort()
# print(mountains.sort(reverse=True)) this prints None
languages.sort(reverse=True)
print(languages)

