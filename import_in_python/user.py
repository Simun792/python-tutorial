from user_details import fullname, mobile_no, address

def user_bio(user_name):
    user_fullname = fullname(user_name=user_name)
    user_mobile_no = mobile_no(user_name=user_name)
    user_address = address(user_name=user_name)

    return f"User name: {user_fullname}\nUser mobile no: {user_mobile_no}\nUser address: {user_address}"


if __name__ == "__main__":
    print(user_bio("rakesh"))
    