inventory = {}

def add_product():
    name = input("商品名を入力してください: ")

    if name in inventory:
        print("その商品はすでに登録されています。")
        return

    quantity = int(input("在庫数を入力してください: "))

    if quantity < 0:
        print("在庫数に負の値は指定できません。")
        return

    inventory[name] = quantity
    print(f"{name} を在庫に追加しました。")

def update_stock():
    name = input("在庫数を更新する商品名を入力してください: ")
    if name not in inventory:
        print("その商品は登録されていません。")
        return

    change = int(input("増減数を入力してください（減らす場合はマイナス）: "))
    if inventory[name] + change < 0:
        print("在庫数が負になるため更新できません。")
        return

    inventory[name] += change
    print(f"{name} の在庫数を {inventory[name]} に更新しました。")

def show_inventory():
    if not inventory:
        print("在庫がありません。")
        return    
    print("【在庫一覧】")

    for name, quantity in inventory.items():
        print(f"{name}: {quantity}")

def show_out_of_stock():
    out_items = []
    for name, quantity in inventory.items():
        if quantity <= 0:
            out_items.append(name)
        if not out_items:
            print("在庫切れの商品はありません。")
            return

    print("【在庫切れ商品】")
    for name in out_items:
        print(name)

def main():
    while True:
        print("--- 在庫管理システム ---")
        print("1. 商品の追加")
        print("2. 商品の在庫数の更新")
        print("3. 在庫一覧の表示")
        print("4. 在庫切れ商品の表示")
        print("5. プログラムの終了")
        choice = input("番号を選択してください: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            show_out_of_stock()
        elif choice == "5":
            print("プログラムを終了します。")
            break
        else:
            print("正しい番号を入力してください。")
main()