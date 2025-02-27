"""
Example file to show a SonarQube bug
"""


def unlock_the_locks():
    """
    Example showing a Sonar Bug
    :return: Locked or unlocked
    """
    word1 = input("Input the first key: ")
    word2 = input("Input the second key: ")
    if word2 == "key2":
            return "Unlocked!"
    elif word1 == "key1":
        return "Key 1 Unlocked"
    return "Locked!"


if __name__ == '__main__':
    print(unlock_the_locks())
