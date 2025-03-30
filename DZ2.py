with open("DZ2.txt", "w") as cats_info:
    cats_info.write('''60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5''')


def get_cats_info(path):
    with open(path, "r") as information:
        content = information.readlines()
    cats_details = [{"id": item[0], "name": item[1], "age": item[2]} \
                    for item in (line.strip().split(",") for line in content) if len(item) == 3]
    return cats_details

cats_info = get_cats_info("DZ2.txt")
print(cats_info)

    