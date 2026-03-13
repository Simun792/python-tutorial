
DETAILS = {
    'simanchal': {
        'first_name': 'Simanchala',
        'surname': 'Gouda',
        'address': 'Golanda',
        'mobile_no': '987568687'
    },
    'rakesh': {
        'first_name': 'Rakesh',
        'surname': 'Panigrahy',
        'address': 'Digapahandi',
        'mobile_no': '9768807119'
    }
}

def address(user_name):
    user_details = DETAILS[user_name]
    return user_details["address"]
    
def fullname(user_name):
    user_details = DETAILS[user_name]
    return f"{user_details["first_name"]} {user_details["surname"]}"

def mobile_no(user_name):
    user_details = DETAILS[user_name]
    return user_details["mobile_no"]



