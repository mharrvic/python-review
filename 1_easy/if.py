is_old = True
is_licenced = False

if is_old and is_licenced:
    print('you are old enough to drive! yo')
elif is_licenced:
    print('you are licenced')
else:
    print('check check')


is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)