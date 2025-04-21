def create_user_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name']= last

    return user_info

joao_profile = create_user_profile('joao', 'lima', age=28, favorite_food='file a parmegiana')
print(joao_profile)
