class SeeMee:
    def youcanseeme(self):
        return 'you can see me'

    def __youcannotseeme(self):
        return 'you cannot see me'


# Outside class
Check = SeeMee()
print(Check.youcanseeme())
#print(Check.__youcannotseeme())
print(Check._SeeMee__youcannotseeme())

# Changing the name causes it to access the function