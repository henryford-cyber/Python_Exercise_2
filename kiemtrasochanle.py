def xu_ly_chuoi(s0):
    ds_so_le = []
    for value in s0:
        if value % 2 != 0:
            ds_so_le.append(value)
    return ds_so_le


with open('input.txt') as f:
    contents = f.read()
s = contents.split()

try:
    if s == []:
        print("danh sach rong")
    else:
        s0 = list(map(int, s))
        print("Danh sach ca so le")
        print(xu_ly_chuoi(s0))
except:
    print("khong hop le")
