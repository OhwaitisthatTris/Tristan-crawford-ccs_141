def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = { 'first_name':first, 'last_name':last }
   
    return user_info


    
user_profile = build_profile('Tristan', 'Crawford jr',
                                location='Earth',           
                                field='cyber crimnology',
                                skill_level='expert')
print(user_profile)