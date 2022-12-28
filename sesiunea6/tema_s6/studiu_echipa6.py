"""
1.Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l.
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')


class TodoList:
    todo = {}

    def __str__(self):
        return f'{self.todo}'

    def __repr__(self):
        return str(self)

    def adauga_task(self, nume, descriere):
        self.todo.setdefault(nume, descriere)

    def finalizeaza_task(self, nume):
        if nume in self.todo.keys():
            self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print('My todo list:')
        for key in self.todo.keys():
            print(key)

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            to_continue = True
            while to_continue:
                question = input('Am detectat un task nou. Doresti sa il adaugi in lista (Y/N)? ').upper()

                if question == 'Y':
                    descriere_task = input('Scrie detalii legate de task-ul nou. ')
                    self.todo.setdefault(nume_task, descriere_task)
                    print(self.todo.get(nume_task))
                    break
                elif question == 'N':
                    to_continue = False
                    pass
                else:
                    print('Nu inteleg ce doresti. Introdu valoarea (Y/N)')
        else:
            print(self.todo.get(nume_task))


task_list1 = TodoList()

task_list1.adauga_task('Preda tema', 'Trebuie sa finalizezi tema astazi!')
task_list1.adauga_task('Studiu echipa', 'Nu uita de studiul in echipa, astazi la ora 19 PM')
task_list1.adauga_task('Studiu individual', 'Mai recapituleaza din lectii')
task_list1.finalizeaza_task('Preda tema')
task_list1.afiseaza_todo_list()
print()

print('Detalii suplimentare task:')
task_list1.afiseaza_detalii_suplimentare('Studiu echipa')
task_list1.afiseaza_detalii_suplimentare('Studiu individual')
task_list1.afiseaza_detalii_suplimentare('Tutorial Git')


