"""
zip(*iterable): aggregate from two or more iterable (list, dic, tuples, etc) lists
                create a zip object with paired elements stored in tuples for each elements.
"""

username = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "Ghana123")
login_date = ["2/4/22", "3/6/22", "15/5/22"]

users = zip(username, passwords)
for i in users:
    print(i)

# ----------------------------------------------------------------
users = dict(zip(username, passwords))
for key,value in users.items():
    print(key + " : " + value)
# ----------------------------------------------------------------
users = zip(username, passwords, login_date)

for i in users:
    print(i)