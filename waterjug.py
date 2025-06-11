def water_jug():
    jug1_capacity = int(input("Enter capacity of Jug 1: "))
    jug2_capacity = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount: "))

    jug1 = 0
    jug2 = 0

    steps = 0  

    while True:
        print(f"Step {steps}: Jug1 = {jug1}L, Jug2 = {jug2}L")
        steps += 1

        if jug1 == target or jug2 == target:
            print(f"\n🎯 Target reached: {target}L")
            break

     
        if jug2 == jug2_capacity:
            print("➡️ Empty Jug2")
            jug2 = 0
        elif jug1 == 0:
            print("➡️ Fill Jug1")
            jug1 = jug1_capacity
        else:
            transfer = min(jug1, jug2_capacity - jug2)
            print(f"➡️ Pour {transfer}L from Jug1 to Jug2")
            jug1 -= transfer
            jug2 += transfer


water_jug()
