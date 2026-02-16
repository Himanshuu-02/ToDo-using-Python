from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db= client.todo_db #database create kiya 
task_collection=db.tasks #collection bnaya

#insert function
def create_task(description,subject):
    task={
        'task':description,
        'subject': subject
    }
    result=task_collection.insert_one(task)
    print(f'task created with id: {result.inserted_id}')
#read task
def read_task():
    tasks=task_collection.find()
    for docs in tasks:
        subject = docs.get('subject', 'No subject')
        print(f"Task :{docs['task']} | Subject:{subject}") 
#delete task
def delete_task():
    del_subject=input("Enter your subject which you want to delete: ")
    del_task=task_collection.delete_one({'subject':del_subject})
    if (del_task.deleted_count > 0):
        print("you task is deleted")
    else:
        print("Your choosen task is not found")
while True:
    print("\n1. Create Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
        description= input("Enter your Task: ")
        subject=input("enter your fav subject: ")
        create_task(description,subject)
        
        
    elif choice=="2":
        read_task()
        
    elif choice=="3":
        delete_task()
    elif choice=="4":
        break
    else:
        print("Please enter a valid number")
