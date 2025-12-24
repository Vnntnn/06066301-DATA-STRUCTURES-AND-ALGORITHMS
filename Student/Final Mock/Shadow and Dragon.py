n = int(input())  # จำนวนทหารเงา
attack = list(map(int, input().split()))  # พลังโจมตีของทหารเงา
defense = list(map(int, input().split()))  # พลังป้องกันของทหารเงา

m = int(input())  # จำนวนมังกร
dragon_attack = list(map(int, input().split()))  # พลังโจมตีของมังกร
dragon_defense = list(map(int, input().split()))  # พลังป้องกันของมังกร

# สำหรับแต่ละมังกร
for i in range(m):
    da = dragon_attack[i]  # พลังโจมตีของมังกรตัวที่ i
    dd = dragon_defense[i]  # พลังป้องกันของมังกรตัวที่ i

    min_mana = float('inf')  # เริ่มต้นค่ามานาน้อยที่สุดเป็นอนันต์

    # ทหารเงาที่โจมตีได้จะต้องมี attack[j] >= dd (พลังโจมตี >= พลังป้องกันของมังกร)
    possible_attackers = []
    for j in range(n):
        if attack[j] >= dd:
            possible_attackers.append(j)

    if not possible_attackers:
        # ถ้าไม่มีทหารเงาคนไหนโจมตีมังกรได้
        print(-1)
    else:
        # ถ้ามีทหารที่สามารถโจมตีมังกรได้
        for j in possible_attackers:
            # คำนวณมานาที่ต้องใช้เพิ่มพลังโจมตี
            mana_needed_for_attack = max(0, dd - attack[j])

            # คำนวณพลังป้องกันรวมของทหารที่เหลือ
            remaining_defense = sum(defense[k] for k in range(n) if k != j)
            # คำนวณมานาที่ต้องใช้เพิ่มพลังป้องกัน
            mana_needed_for_defense = max(0, da - remaining_defense)

            # รวมมานาที่ต้องใช้
            total_mana = mana_needed_for_attack + mana_needed_for_defense

            # หาค่ามานาน้อยที่สุด
            min_mana = min(min_mana, total_mana)

        print(min_mana)
