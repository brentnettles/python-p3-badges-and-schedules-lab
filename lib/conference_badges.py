# def badge_maker(name):
#     print(f'Hello, name is {name}.')
#     return f'Hello, name is {name}.'

# def batch_badge_creator(names):
#     badges = []
#     for name in names:
#         badges.append(badge_maker(name))
#     return badges

# def assign_rooms(names):
#     room = 1
#     for name in names:
#         print(f"Hello, {name}! You'll be assigned to room {room}.")
#         room += 1

# def printer(names):
#     badges = batch_badge_creator(names)
#     for badge in badges:
#         print(badge)
#     assign_rooms(names)

 
def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return [f"Hello, {speaker}! You'll be assigned to room {room}!" for room, speaker in enumerate(speakers, start=1)]

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)


speakers = ["Arel", "Carol"]
printer(speakers)

#____________________________________


# badge_maker('Sammy')

# print(batch_badge_creator)

# names = ['Mike', 'Seth', 'Shan']
# # batch_badge_creator(names)
# printer(names)
# assign_rooms(names)

# countries = ['US', 'GB', 'CA', 'DE']
# for index, item in enumerate(countries):
#     print(item, index)