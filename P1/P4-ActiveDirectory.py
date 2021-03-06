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
    groups = group.get_groups()
    users = group.get_users()
    for val in users:
        if user == val:
            return True

    #else search on other subgroups of the group
    # TODO: is there a chance of infinite loop here ?
    for group in groups:
        if is_user_in_group(user,group):
            return True
    return False


sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child = Group("child")
child.add_group(sub_child)

parent = Group("parent")
parent.add_group(child)

# test1
print(is_user_in_group(sub_child_user,parent))
# True
print(is_user_in_group(sub_child_user,child))
# True


# test2 : group of groups 
print(is_user_in_group(sub_child_user,sub_child))
# True


#test3

g1 = Group("")
u1 = ""
g1.add_user(u1)
print(is_user_in_group(u1,g1))
#True
