import tkinter as tk
import csv



input_file = 'plan_estudios.csv'
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
        for row in new_rows:
            print(f"Del cuatri {row[0]} falta {row[2]}")   
        
#         Filter out empty lines to get a clean list of [Title, Author, Title, Author...]
#         lines = [line.strip() for line in f if line.strip()]

#    with open(titles_file, 'w', encoding='utf-8') as t_file, \
#         #open(authors_file, 'w', encoding='utf-8') as a_file:

#        for i in range(0, len(lines), 2):
#            t_file.write(lines[i] + '\n')
#            if (i + 1) < len(lines):
#                a_file.write(lines[i+1] + '\n')

    #print(f"Split complete: '{titles_file}' and '{authors_file}' created.")

def main():
    print("Hello from project-one!")
    read_csv()
#    root = tk.Tk()
#    root.title("WSL Tkinter Test")
#    label = tk.Label(root, text="If you see this, WSLg is working!")
#    label.pack(padx=20, pady=20)
#    root.mainloop()


if __name__ == "__main__":
    main()
