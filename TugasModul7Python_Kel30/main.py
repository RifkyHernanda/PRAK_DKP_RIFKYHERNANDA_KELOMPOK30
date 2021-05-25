from collections import deque
queue = deque()
stack = []
size = -1
antri = 0
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
            antri+=1
            print("berhasil memasukkan data ke queue")
        elif data%2==1:
            stack.append(data)
            size+=1
            print("berhasil memasukkan data ke stack")
        else:
            print("masukkan bilangan bulat")
    elif pilihan == 2:
        print(queue)
    elif pilihan == 3:
        print(stack)
    elif pilihan == 4:
        jumlahprint= int(input("pop item sebanyak(jumlah tumpukan saat ini"+str(size+1)+") : "))
        if size==-1:
            print("data kosong")
        else:
            if size-jumlahprint <= -1:
                print("data kosong")
            else:
                for i in range(jumlahprint):
                    stack.pop()
                    size-=1
    elif pilihan == 5:
        jumlahprint= int(input("pop item sebanyak (jumlah tumpukan saat ini"+str(antri)+"): "))
        if antri >=1:
            if antri-jumlahprint >=0:
                for i in range(jumlahprint):
                    queue.popleft()
            else:
                print("data tidak sebanyak itu")
        else:
            print("data kosong")