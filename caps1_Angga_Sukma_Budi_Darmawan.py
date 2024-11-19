##input : employee id, nama, status (pkwt, pkwtt, freelance), position, department, date joined, date left, monthly salary
from prettytable import PrettyTable
from datetime import datetime

def show_table():
    print('\n Daftar Karyawan')
    print(tabel)

def bubble_sort(tabel, key, reverse):
    list_data = [list(row) for row in tabel.rows] #ubah tabel ke list
    data = list_data.copy()
    column_map = {
        'ID': 0,
        'Nama': 1,
        'Status': 2,
        'Role': 3,
        'Divisi': 4,
        'Umur': 5,
        'Jenis Kelamin': 6,
        'Gaji (Rp)': 7
    }
    column_index = column_map[key] #indeks kolom
    tabel_sort = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji (Rp)'])
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            # Membandingkan dua data berdasarkan key (misalnya 'jumlah')
            if reverse=='desc':
                if data[j][column_index] < data[j+1][column_index]:  # Urutkan menurun
                    data[j], data[j+1] = data[j+1], data[j]
            else:
                if data[j][column_index] > data[j+1][column_index]:  # Urutkan menaik
                    data[j], data[j+1] = data[j+1], data[j]
    
    for i in data:
        tabel_sort.add_row(i)
    print(tabel_sort)

def confirm_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["y", "n"]:
            return choice
        print("Invalid input. Please enter 'y' or 'n'.")

def input_status(prompt):
    while True:
        value = input(prompt).strip()
        value_check = value
        if value_check.replace(" ", "").isalpha() and value_check.upper() in ['PKWT', 'PKWTT', 'FREELANCE', 'INTERN']:
            if value_check.upper() in ['PKWT', 'PKWTT']:
                value = value.upper()
                return value
            else: #freelance, intern
                value = value.capitalize()
                return value
        print("Invalid input.")

def input_id(prompt, duplicate,trigger_break):
    while True:
        id = input(prompt).strip().upper()
        if not id: #case kosong
            print('Input tidak boleh kosong!')
            continue #kembali ke loop
        if not tabel.rows and duplicate == 2: #case db empty, update/read/delete
            print('\nID karyawan tidak terdaftar di database')
            break #break the loop
        elif id[0].isalpha() == True and id[1:].isdigit() == True:
            #check duplicate
            data_id = [row[0] for row in tabel.rows]
            if duplicate == 1: #untuk case create, no duplicate
                if id in data_id:
                    print(f'ID karyawan sudah terdaftar di database!')
                    trigger_break = 'BREAK'
                    return trigger_break
                else:
                    return id
            if duplicate == 2: #untuk case update delete read
                if id in data_id:
                    return id
                else:
                    print('ID karyawan tidak terdaftar di database')
                    trigger_break = 'BREAK'
                    return trigger_break
        else:
            print('Invalid input!')

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        value_check = value
        if value_check.replace(" ", "").isalpha():  # Memastikan input hanya berisi huruf atau spasi
            return value
        print("Invalid input.")

def input_role(prompt):
    while True:
        value = input(prompt).strip()
        value_check = value
        if value_check.replace(" ", "").isalpha():  # Memastikan input hanya berisi huruf atau spasi
            if len(value)==2 or len(value)==3: #case satu kata, caps
                value = value.upper()
            elif value[0:2].lower() in['it', 'hr'] and value[2].lower() == ' ': #case >1 kata, huruf pertama 2 huruf
                value = capitalize_first_word(value)
            else:
                value = value.title()
            return value
        print("Invalid input.")

def capitalize_first_word(input_string):
    words = input_string.split()
    output_string = " ".join([words[0].upper(), words[1].capitalize()])
    return output_string

def input_umur(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() == True:
            return value
        print("Invalid input.")

def input_gender(prompt):
    while True:
        choice = input(prompt).strip().upper()
        if choice in ["L", "P"]:
            return choice
        print("Invalid input. Please enter 'L' or 'P'.")

def input_gaji(prompt):
    while True:        
        try:
            salary = int(input('Masukkan gaji pokok bulanan: '))
            return salary
        except ValueError:
            print('Format Input Salah!')

def menampilkan_daftar_karyawan():
    while True:
        pilihanread = input('''\nOpsi tampilan daftar karyawan: 
1. Tampilkan semua data karyawan
2. Tampilkan salah satu data karyawan
3. Tampilkan data dengan kolum disortir
4. Kembali ke menu awal
Masukkan angka pilihan: ''')
        if pilihanread == '1':
            while True:
                #check database empty/not
                if not tabel.rows:
                    print('\nDatabase empty')
                    break
                else:
                    show_table()
                    break
        elif pilihanread == '2':
            while True:
                #check database empty/not
                if not tabel.rows:
                    print('\nDatabase empty')
                    break
                else:
                    breakk=0
                    read_id = input_id('\nID karyawan yang ingin ditampilkan (contoh:E001): ', 2, breakk)# 2 untuk read/delete/update
                    if read_id == 'BREAK':
                        break
                    data_id = [row[0] for row in tabel.rows] #buat list data dari tabel
                    index_read = data_id.index(read_id) #cari index id pada list
                    print(f'\nBerikut data karyawan dengan id {read_id}: ')
                    print(tabel[index_read])
                    break
        elif pilihanread == '3':
            #check database empty/not
            if not tabel.rows:
                print('\nDatabase empty')
            else:
                while True:
                    sort_kolom = input('Input pilihan kolom yang ingin disortir: ')
                    if sort_kolom.lower() not in ['id', 'nama', 'status', 'role', 'divisi', 'umur', 'jenis kelamin', 'gaji']:
                        print('Input salah!')
                    else: #case penamaan kolom
                        if sort_kolom.lower() == 'id':
                            sort_kolom = sort_kolom.upper()
                        elif sort_kolom.lower() == 'jenis kelamin':
                            sort_kolom = sort_kolom.title()
                        elif sort_kolom.lower() == 'gaji':
                            sort_kolom = 'Gaji (Rp)'
                        else:
                            sort_kolom = sort_kolom.capitalize()
                        break
                while True:
                    pilihan_sort = input('Input pilihan sort (asc/desc): ').lower()
                    if pilihan_sort not in['asc', 'desc']:
                        print('Inputan salah!')
                    else:
                        bubble_sort(tabel, sort_kolom, pilihan_sort)
                        break
        elif pilihanread == '4':
            break
        else :
            print('Input salah!')

def menambah_karyawan():
    while True:
        pilihancreate = input('''\nOpsi input data karyawan: 
1. Memasukkan data karyawan berdasarkan ID
2. Kembali ke menu awal
Masukkan angka pilihan: ''')
        if pilihancreate == '1':
            while True:
                breakk = 0
                #input data karyawan per kolom
                id_karyawan = input_id('Masukkan ID karyawan (contoh: E001): ', 1, breakk)
                if id_karyawan == 'BREAK':
                    break
                nama_karyawan = input_string('Masukkan nama: ')
                nama_karyawan = nama_karyawan.title()
                status_karyawan = input_status('Masukkan status pegawai (PKWT,PKWTT,Freelance,Intern): ')
                posisi_karyawan = input_role('Masukkan posisi: ')
                divisi_karyawan = input_role('Masukkan divisi: ')
                umur = input_umur('Masukkan umur karyawan: ')
                jenis_kelamin = input_gender('Masukkan jenis kelamin (L/P): ')
                gaji_karyawan = input_gaji('Masukkan gaji pokok bulanan (Rp.): ')
                #show data create
                list_create = [id_karyawan, nama_karyawan, status_karyawan, posisi_karyawan, divisi_karyawan, umur, jenis_kelamin, gaji_karyawan]
                tabel_create = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji Pokok (Rp.)'])
                tabel_create.add_row(list_create)
                print('\nBerikut adalah data yang ingin dimasukan: ')
                print(tabel_create)
                #konfirmasi
                choice = confirm_yes_no('Save Data? (y/n) :')
                if choice == 'y':
                    tabel.add_row([id_karyawan, nama_karyawan, status_karyawan, posisi_karyawan, divisi_karyawan, umur, jenis_kelamin, gaji_karyawan])
                    print('\nData telah diinput')
                    break
                else:
                    print('Data batal dimasukkan')
                    break
        elif pilihancreate == '2':
            break
        else:
            print('INPUT SALAH!')

def menghapus_karyawan():
    while True: 
        pilihandelete = input('''\nOpsi menghapus data karyawan: 
1. Delete data karyawan berdasarkan ID
2. Delete lebih dari satu data karyawan
3. Delete seluruh data
4. Kembali ke menu awal
Masukkan angka pilihan: ''')
        if pilihandelete == '1':
            while True:
                breakk=0
                id_delete_input = input_id('Masukkan id karyawan yang ingin dihapus (contoh: E001):', 2, breakk)#2 untuk delete/update
                if not tabel.rows: #case db empty
                    break #break the loop
                elif id_delete_input == 'BREAK':
                    break
                data_id = [row[0] for row in tabel.rows]
                index_delete = data_id.index(id_delete_input) #cari index id
                #show data yang akan didelete
                print(f'\nBerikut data karyawan dengan id {id_delete_input}: ')
                print(tabel[index_delete])
                deletekah = confirm_yes_no('Delete data? (y/n): ')
                if deletekah.lower() == 'y':
                    del tabel._rows[index_delete]
                    print('\nData telah dihapus')
                    break
                elif deletekah.lower() == 'n':
                    print('Data batal dihapus')
                    break
        elif pilihandelete == '2':
            j=0
            while True:
                # Input ID karyawan yang akan dihapus, dipisahkan dengan koma
                ids_to_delete = input("Masukkan ID karyawan yang ingin dihapus (pisahkan dengan koma, contoh: E001, E002, E003): ").split(',')
                if not tabel.rows:
                    break #break the loop
                ids_to_delete = [id.strip().upper() for id in ids_to_delete]
                data_id = [row[0] for row in tabel.rows]
                index_delete = []
                list_del = []
                tabel_del = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji (Rp)'])
                for i in ids_to_delete: #check id terlebih dahulu
                    if i in data_id:
                        print(f'{i} ada dalam data.')
                        index_delete.append(data_id.index(i))
                        j=0 #case id ada dalam data
                    elif i[0].isalpha() == True and i[1:].isdigit() == True:
                        print(f'{i} tidak ada dalam data.')
                        j=2 #case id tidak ada dalam ada
                        break
                    else:
                        print(f'{i} tidak sesuai format.')
                        j=1
                        break
                if j==0 or j==2: #stop input jika semua id inputan sesuai format
                    break
            
            if j==0: #case id ada dalam data
                #buat tabel delete untuk di show    
                tabel_del = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji (Rp)'])
                for i in index_delete:
                    list_del.append(tabel._rows[i])
                for j in list_del:
                    tabel_del.add_row(j)
                print('\nBerikut data yang ingin dihapus: ')
                print(tabel_del)
                #konfirmasi
                while True:
                    delete_multiple = confirm_yes_no('Delete data? (y/n): ')
                    if delete_multiple.lower() == 'y':
                        for k in index_delete:
                            del tabel._rows[k]
                    elif delete_multiple.lower() == 'n':
                        print('Data batal dihapus')
                        break
                    else:
                        print('Input Salah!')
                    break
                break
            if j==2 : #langsung kembali ke sub-menu
                continue
        elif pilihandelete == '3':
            print('\nBerikut data tabel sebelum dihapus: ')
            show_table()
            input_delete = confirm_yes_no('Apakah yakin ingin menghapus semua data di database(y/n)?: ')
            if input_delete == 'y':
                tabel.clear_rows()
                print('\nData telah dihapus')
            elif input_delete == 'n':
                print('Data batal dihapus')
        elif pilihandelete == '4':
            break
        else:
            print('Input Salah!')

def update_karyawan():
    while True:
        pilihanupdate = input('''\nOpsi update data karyawan berdasarkan ID: 
1. Update data karyawan berdasarkan pilihan kolom
2. Update data karyawan seluruh kolom
3. Kembali ke menu awal
Masukkan angka pilihan: ''')
        if pilihanupdate == '1':
            while True:
                breakk = 0
                id_update_input = input_id(f'Masukan ID Karyawan Yang Ingin di Update: ', 2, breakk)
                if not tabel.rows:
                    break #break the loop
                elif id_update_input == 'BREAK':
                    break
                data_id = [row[0] for row in tabel.rows]
                index_update = data_id.index(id_update_input)
                print(f'\nBerikut data karyawan dengan id {id_update_input}: ')
                print(tabel[index_update])
                updatekah = confirm_yes_no('Continue Update? (y/n): ')
                if updatekah.lower() == 'y':
                    input_column = input('Kolom yang ingin diupdate: ')
                    if input_column.lower() == 'nama':
                        nama_karyawan = input_string('Masukkan nama: ')
                        data_update = nama_karyawan.title()
                        index_column = 1
                    elif input_column.lower() == 'status':
                        status_karyawan = input_status('Masukkan status pegawai (PKWT,PKWTT,Freelance,Intern): ')
                        data_update = status_karyawan
                        index_column = 2
                    elif input_column.lower() == 'role':
                        posisi_karyawan = input_role('Masukkan posisi: ')
                        data_update = posisi_karyawan
                        index_column = 3
                    elif input_column.lower() == 'divisi':
                        divisi_karyawan = input_role('Masukkan divisi: ')
                        data_update = divisi_karyawan
                        index_column = 4
                    elif input_column.lower() == 'umur':
                        umur = input_umur('Masukkan umur: ')
                        data_update = umur
                        index_column = 5
                    elif input_column.lower() == 'jenis kelamin':
                        jenis_kelamin = input_gender('Masukkan jenis kelamin(L/P): ')
                        data_update = jenis_kelamin
                        index_column = 6
                    elif input_column.lower() == 'gaji':
                        gaji_karyawan = input_gaji('Masukkan gaji pokok bulanan (Rp.): ')
                        data_update = gaji_karyawan
                        index_column = 7
                    else:
                        print(f'Kolom {input_column.capitalize()} tidak ada dalam data.')
                    print('\nBerikut adalah data yang ingin dimasukan: ')
                    print(f'{id_update_input}, {input_column.capitalize()} : {data_update}')
                    #konfirmasi 
                    update_id = confirm_yes_no('Update Data? (y/n) :')
                    if update_id.lower() == 'y': #UPDATE
                        tabel._rows[index_update][index_column] = data_update
                        print('\nData telah diupdate')
                        break
                    elif update_id.lower() == 'n':
                        print('Data batal diupdate')
                        break
        elif pilihanupdate == '2':
            while True:
                breakk = 0
                id_update_input = input_id(f'Masukan ID Karyawan Yang Ingin di Update: ', 2, breakk)
                if not tabel.rows:
                    break #break the loop
                elif id_update_input == 'BREAK':
                    break
                data_id = [row[0] for row in tabel.rows]
                index_update = data_id.index(id_update_input)
                print(f'\nBerikut data karyawan dengan id {id_update_input}: ')
                print(tabel[index_update])
                updatekah = confirm_yes_no('Continue Update? (y/n): ')
                if updatekah.lower() == 'y':
                    nama_karyawan = input_string('Masukkan nama: ')
                    nama_karyawan = nama_karyawan.title()
                    status_karyawan = input_status('Masukkan status pegawai(PKWT,PKWTT,Freelance,Intern): ')
                    posisi_karyawan = input_role('Masukkan posisi: ')
                    divisi_karyawan = input_role('Masukkan divisi: ')
                    umur = input_umur('Masukkan umur: ')
                    jenis_kelamin = input_gender('Masukkan jenis kelamin(L/P): ')
                    gaji_karyawan = input_gaji('Masukkan gaji pokok bulanan (Rp.): ')
                    print('\nBerikut adalah data yang ingin dimasukan: ')
                    list_update = [id_update_input, nama_karyawan, status_karyawan, posisi_karyawan, divisi_karyawan, umur, jenis_kelamin, gaji_karyawan]
                    tabel_update = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji Pokok (Rp.)'])
                    tabel_update.add_row(list_update)
                    print(tabel_update)
                    #konfirmasi 
                    update_id = confirm_yes_no('Update Data? (y/n) :')
                    if update_id.lower() == 'y': #UPDATE
                        tabel._rows[index_update] = list_update
                        print('Data telah diupdate')
                        break
                    elif update_id.lower() == 'n':
                        print('Data batal diupdate')
                        break
                    else :
                        print('INPUT SALAH!')
        elif pilihanupdate == '3':
            break
        else:
            print('INPUT SALAH!')

def main_menu():
    while True:
        pilihanMenu=input('''
Selamat Datang di database karyawan
List Menu:
1. Menampilkan Daftar Karyawan
2. Menambah Data Karyawan
3. Menghapus Data Karyawan
4. Update Data Karyawan
5. Exit Program
Masukkan angka Menu yang ingin dijalankan : ''')
        if pilihanMenu=='1': #Read
            menampilkan_daftar_karyawan()
        elif pilihanMenu=='2': #Create
            menambah_karyawan()
        elif pilihanMenu =='3': #Delete
            menghapus_karyawan()        
        elif pilihanMenu =='4': #Update
            update_karyawan()
        elif pilihanMenu =='5': #Exit
            print('Keluar dari Program !!!')
            break
        else:
            print('Invalid Input !!!')

#data dummy
list_data = [['E001', 'Alice Johnson', 'PKWT', 'Software Engineer', 'IT', '29', 'P',20000000], ['E002', 'Bob Smith', 'PKWTT', 'Project Manager', 'Operations', '35', 'L', 12000000], ['E003', 'Charlie Davis', 'Intern', 'Graphic Designer', 'Marketing', '27', 'L', 3500000], ['E004', 'Dana Lee', 'PKWT', 'HR Specialist', 'HR', '32', 'P',10000000], ['E005', 'Edward Brown', 'PKWTT', 'Data Analyst', 'IT', '30', 'L', 6000000], ['E006', 'Fiona Green', 'PKWT', 'Accountant', 'Finance', '40', 'P',9000000], ['E007', 'George White', 'Freelance', 'Copywriter', 'Marketing', '24', 'L', 3000000], ['E008', 'Hannah King', 'PKWTT', 'Sales Executive', 'Sales', '28', 'L',20000000], ['E009', 'Ian Black', 'PKWT', 'IT Support', 'IT', '33', 'L', 7500000], ['E010', 'Julia Scott', 'PKWTT', 'Product Manager', 'R&D', '38', 'P', 9500000]]
tabel = PrettyTable(['ID', 'Nama', 'Status', 'Role', 'Divisi', 'Umur', 'Jenis Kelamin', 'Gaji (Rp)'])

#input data dummy ke tabel
for i in list_data:
    tabel.add_row(i)

main_menu()