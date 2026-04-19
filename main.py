import tkinter as tk
import csv



input_file = 'plan_estudios.csv'

my_dict = {}

#titles_file = 'titles.txt'
#authors_file = 'authors.txt'

#crea el diccionario
def get_dict():
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        id = 1
        for row in reader:
            my_dict[id] = row
            id += 1
    print("Your dictionary is ready as: my_dict")

#convierte las materias en ints    
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
        
    #for key, value in my_dict.items():
    #    print(f"{key} {value}")


#Convierte los requisitos en listas
def split_req():
    for id in my_dict:
        text = my_dict[id]['Requisitos']
        my_dict[id]['Requisitos'] = text.split(", ")
        
def get_total():
    print(f"\nLa cantidad de cursos totales es {len(my_dict)}\n")
        
def prepare_data():
    get_dict()
    cuatri_to_int()
    split_req()
        
def dict_to_file():
    prepare_data()
    
    headers = ['id', 'Nivel', 'Codigo', 'Curso', 'Requisitos', 'Estado']  # Define headers

    with open('example.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for key, value in my_dict.items():
            row = {'id': key}
            row.update(value)
            writer.writerow(row)


#lista los requisitos        
def get_all_reqs():
    print("\nGetting requirements\n")
    for id in my_dict:
        print(f"Para el curso: {my_dict[id]['Codigo']} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
        
def get_reqs():
    print("\nGetting requirements for pending courses")
    unblocks = []
    for id in my_dict:
        if not 'Ninguno' in my_dict[id]['Requisitos'] and my_dict[id]['Estado'] != 'Aprobado' and my_dict[id]['Estado'] != 'Matriculado':
            print(f"\nPara el curso: {my_dict[id]['Codigo']} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
            for requirement in my_dict[id]['Requisitos']:
                for items in my_dict:
                    if requirement in my_dict[items]['Codigo'] and my_dict[items]['Estado'] == 'Aprobado':
                        print(f"Tienes el requisito: {requirement} aprobado")
                    if requirement in my_dict[items]['Codigo'] and my_dict[items]['Estado'] == 'Matriculado':
                        print(f"Tienes el requisito: {requirement}: {my_dict[items]['Curso']} Matriculado!")
                        unblocks.append(my_dict[id])
                    if requirement in my_dict[items]['Codigo'] and my_dict[items]['Estado'] == 'Por matricular':
                        print(f"Falta el requisito: {requirement} : {my_dict[items]['Curso']}")

    print("\nTus cursos matriculados te desbloquean 1 en las siguientes materias:\n")
    for thing in unblocks:
        print(f"{thing}")
    
        
#lista las materias aprobadas        
def get_approved():
    print("\nAPPROVED COURSES ARE\n")
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Aprobado':
            print(my_dict[id])
            count += 1
    get_approved_count()     

#lista las materias matriculadas
def get_enrolled():
    print("\nENROLLED COURSES ARE\n")
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Matriculado':
            print(my_dict[id])
    get_enrolled_count()  

#lista las materias pendientes            
def get_pending():
    print("\nPENDING COURSES ARE\n")   
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Por matricular':
            print(f"{my_dict[id]['Codigo']}: {my_dict[id]['Curso']}")  
    get_pending_count()             

def get_approved_count():
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Aprobado':
            count +=1
    print(f"Has completado {count} cursos")  
    
def get_enrolled_count():
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Matriculado':
            count +=1
    print(f"Solo faltan {count} cursos por completar")  
    
def get_pending_count():
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Por matricular':
            count +=1
    print(f"Solo faltan {count} cursos por completar")      
                   
def get_all():
    for item, value in my_dict.items():
        #print(value['Curso'])
        print(f"{item}: {value}")
        
def get_by_level(cuatri):
    print(f"Las materias del cuatri {cuatri} son:")
    for id in my_dict:
        if my_dict[id]['Nivel'] == cuatri:
            print(f"{my_dict[id]['Curso']} {my_dict[id]['Estado']}")
            
def get_by_id(value):
    print(f"{my_dict[value]}")

def main_menu():
    while True:
        print("\n--- APP MAIN MENU ---")
        print("1. Print all")
        print("2. Get by cuatri")
        print("3. Help")
        print("0. Exit")

        choice = input("\nSelect an option (1-4): ")       
        if choice == '1':
            print("Displaying all assignatures...")
            get_all()
        elif choice == '2':
            print("Opening settings...")
            level_menu()
        elif choice == '3':
            print("Loading help documentation...")
            get_enrolled()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break  # This stops the while loop
        else:
            print("Invalid choice. Please try again.")

def level_menu():
    while True:
        print("\n--- APP SECONDARY MENU ---")
        print("1. Print all")
        print("2. Settings")
        print("3. Help")
        print("0. Exit")

        choice = input("\nSelect an option (1-4): ")       
        if choice == '1':
            print("Displaying profile information...")
            get_by_level(1)
            break;
        elif choice == '2':
            print("Opening settings...")
            get_by_level(2)
            break;
        elif choice == '3':
            print("Loading help documentation...")
            get_by_level(3)
            break;
        elif choice == '0':
            print("Exiting... Goodbye!")
            break  # This stops the while loop
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Hello from project-one!")
    print("Assignature tracker")
    prepare_data()
    print("Opening menu...")
    #main_menu()
    get_pending()
    #get_by_id(38)
    #get_by_level(8)
    #dict_to_file()


#    root = tk.Tk()
#    root.title("WSL Tkinter Test")
#    string = ',\n'.join(str(x) for x in my_array)
#    label = tk.Label(root, text=string, anchor="w", justify="left")
#    label.pack(padx=20, pady=20)
#    root.mainloop()


if __name__ == "__main__":
    main()
