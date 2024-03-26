from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "[X]" if task.completed else "[ ]"
            print(f"{i}.{status}{task.name}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name},{task.completed}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, completed = line.strip().split(',')
                    task = Task(name)
                    task.completed = bool(completed)
                    self.tasks.append(task)
        except FileNotFoundError:
            print("ERROR!!!, File not found in the database.")
            pass
        
todo_list = ToDoList()

@app.route('/')
def index():
    return render_template('index.html', tasks = todo_list.tasks)

@app.route('/reference', methods=['POST'])
def reference():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    return render_template("reference.html")

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))
        
    return render_template("contact.html")

@app.route('/add_task')
def add_task():
    task_name = request.form.get('task_name')
    todo_list.add_task(Task(task_name))
    
    return redirect(url_for('index'))

@app.route('/mark_completed/<int:task_index>')
def mark_completed(task_index):
    todo_list.mark_completed(task_index)
    
    return redirect(url_for('index))

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    todo_list.remove_task(task_index)
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
