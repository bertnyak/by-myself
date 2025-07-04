a = input()
total_kop = len(a) * 60  # всего копеек
rub = total_kop // 100   # целые рубли
kop = total_kop % 100    # остаток копеек
print(f"{rub} р. {kop:0d} коп.")