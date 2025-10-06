from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)
tasks = []

task_id_control = 1
@app.route("/tasks", methods=['POST'])
def create_task():
    
    global task_id_control
    data= request.get_json()
    new_task = Task(id = task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)


    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    
    #for task in tasks:
      #  task_list.append(task.to_dict())  
        
    output = {
            "tasks": task_list,
            "total_tasks": len(task_list)
            }
        
    print(task_list)
    return output

@app.route("/tasks/<int:id_task>", methods=['GET'])
def get_task(id_task):
    for t in tasks:
        if t.id == id_task:
            return jsonify(t.to_dict())
    
    return({"message": "Não foi possível encontrar a atividade"}),  404

#@app.route("/user/<int:username_id>")
#def show_user(username_id):
 #   print(username_id)
 #   print(type(username_id))
 #   return 

@app.route("/tasks/<int:id>", methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t #task recebe a task atual
            
        if task == None: #Caso não encontre
            return jsonify({"message": "Não foi possível encontrar a atividade"}),  404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    
    return jsonify({"message": "task atualizada com sucesso"}), 200

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):
    task = None
    
    for t in tasks:
        print(t)
        if t.id == id:
            task = t
            break
            
    if task == None:
        return({"message": "Não foi possível encontrar a atividade"}),  404
    
    tasks.remove(task)
    return({"message": "Tarefa deletada com sucesso"}), 200
    
    
    
if __name__ == "__main__":
    app.run(debug=True)