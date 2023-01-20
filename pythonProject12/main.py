#Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope

#Modifying Global scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies outside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

print("Hello"[:-1])