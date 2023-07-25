from admin import Admin

tom = Admin('tom', 'zhang')

tom.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]

tom.privileges.show_privileges()
            
            
            