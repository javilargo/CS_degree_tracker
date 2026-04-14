import tkinter as tk
import csv



input_file = 'plan_estudios.csv'

my_dict = {}
transformed_data = []
my_array = []
multi_req_rows = []
multi_req = 0
#titles_file = 'titles.txt'
#authors_file = 'authors.txt'

def read_csv():
    with open(input_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        total_courses = 0
        new_rows = []
        for row in spamreader:
            total_courses += 1
            if row[-1] != "Aprobado":
                print(row)
                new_rows.append(row)
        print("\nTHIS ARE THE NOT APPROVED COURSES\n")
        count = 0
        for row in new_rows:
            count+=1
            print(row)
            my_array.append(row)
        print(f"From the total of {total_courses-1} courses")
        print(f"There are {count-1} courses remaining")
        
        multi_req = 0
        multi_req_rows = []
        for row in new_rows:
            if row[0] == "2do Cuatrimestre":
                row[0] = 2
            if row[0] == "3er Cuatrimestre":
                row[0] = 3
            if row[0] == "4to Cuatrimestre":
                row[0] = 4
            if row[0] == "5to Cuatrimestre":
                row[0] = 5
            if row[0] == "6to Cuatrimestre":
                row[0] = 6
            if row[0] == "7mo Cuatrimestre":
                row[0] = 7
            if row[0] == "8vo Cuatrimestre":
                row[0] = 8                     
            print(row)
            if len(row) > 5:
                multi_req += 1
                multi_req_rows.append(row)
        print(f"From the total of {total_courses-1} courses")
        print(f"There are {count-1} courses remaining")
        print(f"There are {multi_req} courses with more than 1 requirement")
        print(f"These are the courses with more than 1 req {multi_req_rows}")
        
        print(f"\nLAS MATERIAS QUE FALTAN SON:") 
        for row in new_rows:
            if row[-1] == "Por matricular":
                print(f"Del cuatri {row[0]} falta {row[2]}")   

        print(f"\nPOR EL LADO BUENO LLEVO ESTAS:")
        for row in new_rows:
            if row[-1] == "Matriculado":
                print(row)
                print(f"Del cuatri {row[0]} llevas {row[2]}")
                
        print(f"\nLAS QUE TIENEN MAS DE UN REQUISITO SON:")
        for row in multi_req_rows:
            print(f"{row}")
            
        print(f"\nO BIEN, LAS QUE TIENEN MAS DE UN REQUISITO SON:")
        for row in multi_req_rows:
            if len(row) == 6:
                reqs_dict = {"requisitos": [row[3], row[4]]}
                row[3] = reqs_dict
                row.pop(4)
            if len(row) == 7:
                reqs_dict = {"requisitos": [row[3], row[4], row[5]]}
                row[3] = reqs_dict
                row.pop(4)
                row.pop(4)
                
        for row in multi_req_rows:
            print(f"{row}")        
#         Filter out empty lines to get a clean list of [Title, Author, Title, Author...]
#         lines = [line.strip() for line in f if line.strip()]

#    with open(titles_file, 'w', encoding='utf-8') as t_file, \
#         #open(authors_file, 'w', encoding='utf-8') as a_file:

#        for i in range(0, len(lines), 2):
#            t_file.write(lines[i] + '\n')
#            if (i + 1) < len(lines):
#                a_file.write(lines[i+1] + '\n')

    #print(f"Split complete: '{titles_file}' and '{authors_file}' created.")
def get_dict():
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        id = 1
        for row in reader:
            my_dict[id] = row
            id += 1
    print("Your dictionary is ready as: my_dict")
    
def cuatri_to_int():
    for id in my_dict:
        if my_dict[id]['Nivel'] == '1er Cuatrimestre':
            my_dict[id]['Nivel'] = 1
        if my_dict[id]['Nivel'] == '2do Cuatrimestre':
            my_dict[id]['Nivel'] = 2
        if my_dict[id]['Nivel'] == '3er Cuatrimestre':
            my_dict[id]['Nivel'] = 3
        if my_dict[id]['Nivel'] == '4to Cuatrimestre':
            my_dict[id]['Nivel'] = 4
        if my_dict[id]['Nivel'] == '5to Cuatrimestre':
            my_dict[id]['Nivel'] = 5
        if my_dict[id]['Nivel'] == '6to Cuatrimestre':
            my_dict[id]['Nivel'] = 6
        if my_dict[id]['Nivel'] == '7mo Cuatrimestre':
            my_dict[id]['Nivel'] = 7
        if my_dict[id]['Nivel'] == '8vo Cuatrimestre':
            my_dict[id]['Nivel'] = 8
        
    for key, value in my_dict.items():
        print(f"{key} {value}")
        
def get_req():
    print("\nGetting requirements\n")
    for id in my_dict:
        print(f"Para el curso: {my_dict[id]['Codigo']} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
        
        
def get_approved():
    print("\nAPPROVED COURSES ARE\n")      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Aprobado':
            print(my_dict[id])   

def get_enrolled():
    print("\nENROLLED COURSES ARE\n")      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Matriculado':
            print(my_dict[id])   
            
def get_pending():
    print("\nPENDING COURSES ARE\n")      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Por matricular':
            print(my_dict[id])               

def transform_data():
    global total_courses
    global multi_req
    global multi_req_rows 
    with open(input_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        #total_courses = len(spamreader) - 1
        for row in spamreader:
            if row[0] == "1er Cuatrimestre":
                row[0] = 1
            if row[0] == "2do Cuatrimestre":
                row[0] = 2
            if row[0] == "3er Cuatrimestre":
                row[0] = 3
            if row[0] == "4to Cuatrimestre":
                row[0] = 4
            if row[0] == "5to Cuatrimestre":
                row[0] = 5
            if row[0] == "6to Cuatrimestre":
                row[0] = 6
            if row[0] == "7mo Cuatrimestre":
                row[0] = 7
            if row[0] == "8vo Cuatrimestre":
                row[0] = 8                     
            transformed_data.append(row)
            
    print("Success! Data has been transformed")
    print("This is the new data")
    for row in transformed_data:
        print(row)

def get_aprobados():
    global total_courses
    with open(input_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')       
        new_rows = []
        for row in spamreader:
            total_courses += 1
            if row[-1] == "Aprobado":
                print(row)
                new_rows.append(row)
        print("\nTHIS ARE THE APPROVED COURSES (W)\n")
        count = 0
        for row in new_rows:
            count+=1
            print(row)
            my_array.append(row)
        print(f"From the total of {total_courses-1} courses")
        print(f"There are {count} courses completed")
        
def split_req():
    for id in my_dict:
        text = my_dict[id]['Requisitos']
        my_dict[id]['Requisitos'] = text.split(", ")
        
def get_total():
    print(f"\nLa cantidad de cursos totales es {len(my_dict)}\n")

def main():
    print("Hello from project-one!")
    get_dict()
    get_req()
    cuatri_to_int()
    get_approved()
    get_enrolled()
    get_pending()
    get_total()
    split_req()
    #transform_data()
    #get_total()
    #read_csv()
    #get_aprobados()
#    root = tk.Tk()
#    root.title("WSL Tkinter Test")
#    string = ',\n'.join(str(x) for x in my_array)
#    label = tk.Label(root, text=string, anchor="w", justify="left")
#    label.pack(padx=20, pady=20)
#    root.mainloop()


if __name__ == "__main__":
    main()
