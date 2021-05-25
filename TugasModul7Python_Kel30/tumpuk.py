from collections import deque
queue = deque()
stack = []
count = 0
while count == 0:
    print("---Menu---")
    print("1. Masukkan data bilangan bulat")
    print("2. Tampilkan data queue")
    print("3. Tampilkan data stack")
    print("4. pop item(stack)")
    print("5. dequeue item(queue)")
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
        data = int(input("Data yang ditambahkan : "))
        if data%2==0:
            queue.append(data)
            print("berhasil memasukkan data ke queue")
        elif data%2==1:
            stack.append(data)
            print("berhasil memasukkan data ke stack")
    elif pilihan == 2:
        print(queue)
    elif pilihan == 3:
        print(stack)
    elif pilihan == 4:
        jumlahprint= int(input("pop item sebanyak(jumlah tumpukan saat ini : "))
        for i in range(jumlahprint):
            stack.pop()
    elif pilihan == 5:
        jumlahprint= int(input("pop item sebanyak (jumlah tumpukan saat ini : "))
        for i in range(jumlahprint):
            queue.popleft()