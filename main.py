import tkinter as tk
import sqlite3
import csv
from course import Course
from curriculum import CurriculumManager
from courses import *

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()


my_dict = {}

#titles_file = 'titles.txt'
#authors_file = 'authors.txt'

#crea el diccionario
def get_dict(input_file):
    print("Creating dict...")
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        #id = 1
        for row in reader:
            row['Unlocks'] = []
            id = row['Codigo']
            del row['Codigo']
            #id = "'" + row['Codigo'] + "'"
            my_dict[id] = row
            #id += 1
    print("Created your dictionary as: my_dict")

#convierte las materias en ints    

def cuatri_to_int():
    print("Converting Nivel to int...")
    for id in my_dict:
        my_dict[id]['Nivel'] = int(my_dict[id]['Nivel'][0])
        
    #for key, value in my_dict.items():
    #    print(f"{key} {value}")


#Convierte los requisitos en listas
def split_req():
    print("Creating requirements as lists...")
    for id in my_dict:
        text = my_dict[id]['Requisitos']
        my_dict[id]['Requisitos'] = [item.strip() for item in text.split(",")]
        for index in range(len(my_dict[id]['Requisitos'])):
            #print(index)
            if my_dict[id]['Requisitos'][index] == 'AN-100':
                print(f"Found AN-100 at: {id}")
                print(f"Modifying AN-100 to IC-100...")
                my_dict[id]['Requisitos'][index] = 'IC-100'
            #if item == 'AN-100':
            #    item = 'IC-100'
            #print(f"id: {id}")                
        
def fill_unblocks():
    print("\nFilling Unlocks list...")
    for id in my_dict:
        if not 'Ninguno' in my_dict[id]['Requisitos']:
            #print(f"\nPara el curso: {id} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
            for requirement in my_dict[id]['Requisitos']:                
                #ERROR PORQUE HAY UN REQ QUE DICE [CO] al final
                #TODO add a try catch exception in case requirement does not exist
                try:
                    my_dict[requirement]['Unlocks'].append(id)
                except:
                    print(f"Error {requirement} does not exist")
                    print("Retrying...")
                    requirement = requirement[:6]
                    my_dict[requirement]['Unlocks'].append(id)
                    print(f"Success as {requirement}")
       
def get_total():
    print(f"\nLa cantidad de cursos totales es {len(my_dict)}\n")
        
def prepare_data(input_file):
    print("\nPreparing data...\n")    
    get_dict(input_file)
    print("Success!\n")    
    cuatri_to_int()
    print("Success!\n")    
    split_req()
    print("Success!\n")
    fill_unblocks()
    print("Success!\n")
    print("Your data is ready\n")
        
def dict_to_file():
    prepare_data()
    
    headers = ['id', 'Nivel', 'Codigo', 'Curso', 'Requisitos', 'Estado']  # Define headers

    with open('plan_estudios_clean.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for key, value in my_dict.items():
            row = {'id': key}
            row.update(value)
            writer.writerow(row)

def dict_to_class():
    with open('courses.py', 'w') as file:
        file.write("from course import Course\n")
        file.write("course_catalog = {}\n")
        
    for item in my_dict:
        print(item)
        item_name = item
        item_name = Course(item, my_dict[item]['Nivel'], my_dict[item]['Curso'], my_dict[item]['Requisitos'], my_dict[item]['Estado'], my_dict[item]['Unlocks'])
        with open('courses.py', 'a') as f:
            f.write(f"course_catalog['{item}'] = {item_name}\n")

#lista los requisitos        
def get_all_reqs():
    print("\nGetting all requirements\n")
    for id in my_dict:
        print(f"Para el curso: {id} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
        
def get_reqs():
    print("\nGetting requirements for pending courses")
    unblocks = []
    for id in my_dict:
        if not 'Ninguno' in my_dict[id]['Requisitos'] and my_dict[id]['Estado'] != 'Aprobado' and my_dict[id]['Estado'] != 'Matriculado':
            print(f"\nPara el curso: {id} {my_dict[id]['Curso']} Necesitas: {my_dict[id]['Requisitos']}")
            for requirement in my_dict[id]['Requisitos']:
                #ERROR PORQUE HAY UN REQ QUE DICE [CO] al final
                #TODO add a try catch exception in case requirement does not exist
               
                try: 
                    if my_dict[requirement]['Estado'] == 'Aprobado':
                        print(f"Tienes el requisito: {requirement} Aprobado!")
                        
                    if my_dict[requirement]['Estado'] == 'Matriculado':
                        print(f"Tienes el requisito: {requirement} Matriculado!")
                        unblocks.append(id)
                        
                    if my_dict[requirement]['Estado'] == 'Por matricular':
                        print(f"Falta el requisito: {requirement}")
                        
                except: 
                    print(f"{requirement} not found... Fixing...")
                    requirement = requirement[:6]
                    print(f"{requirement} se encuentra {my_dict[requirement]['Estado']}")                    

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
            print(f"{id}: {my_dict[id]['Curso']}")  
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
    print(f"Solo faltan {count} cursos por completar\n")  
    
def get_pending_count():
    count = 0      
    for id in my_dict:
        if my_dict[id]['Estado'] == 'Por matricular':
            count +=1
    print(f"Solo faltan {count} cursos por completar\n")      
                   
def get_all():
    print(f"\n*PRINTING ALL*\n")
    for key, value in my_dict.items():
        #print(value['Curso'])
        print(f"{key}: {value}")
        
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
    prepare_data('plan_estudios.csv')
    print("Opening menu...")
    get_pending()
    get_all()
    #get_all_reqs()
    get_reqs()
    get_all()
    dict_to_class()
    print("\n============\nEL CATALOGO\n============\n")
    for id in course_catalog:
        print(f"{id}: {course_catalog[id]}")
    #print(course_catalog)
    print(course_catalog['II-115'].name)
    res = cursor.execute("SELECT name FROM users")
    res.fetchone()
    print(res.fetchone())
    conn.close()
    #main_menu()
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
