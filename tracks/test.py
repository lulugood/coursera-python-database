
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.text == key :
            found = True
    return None
f = 'happy','cry','sad'
lookup(f,'sad')
