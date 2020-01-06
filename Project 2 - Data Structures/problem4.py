class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):

    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if not isinstance(group, Group):
        print("Please enter a real group")
        return

    if user in group.get_users():
        return True

    else:
        for x in group.get_groups():
            return is_user_in_group(user, x)

    return False

# test setup

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child_user2 = "sub_child_user2"
child.add_user(sub_child_user2)

child.add_group(sub_child)
parent.add_group(child)

# test case 1

print(is_user_in_group("sub_child_user", parent))

# test case 2

print(is_user_in_group("sub_child_user2", parent))

# test case 3

print(is_user_in_group("sub_child_user_bad", parent))

# test case 4

print(is_user_in_group("sub_child_user_bad", "bad group"))
