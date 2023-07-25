from admin import Admin

ad = Admin('zhang', 'shufang')
ad.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"]

ad.privileges.show_privileges()