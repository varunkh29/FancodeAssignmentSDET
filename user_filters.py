def filter_users_by_location(users):
    fan_code_city_users = []
    for user in users:
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        if -40 <= lat <= 5 and 5 <= lng <= 100:
            fan_code_city_users.append(user)
    return fan_code_city_users