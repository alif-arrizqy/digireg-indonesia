from app.config.connection import mongo_connection
from fastapi import HTTPException
collection = mongo_connection()

def create_task(data):
    datas = {
        "task_id": data.get("task_id"),
        "task_name": data.get("task_name"),
        "task_description": data.get("task_description"),
        "task_status": data.get("task_status"),
        "created_at": data.get("created_at")
    }
    collection.insert_one(datas)
    datas.pop("_id")
    return datas


def get_task():
    result = collection.find()
    datas = []
    for x in result:
        x.pop("_id")
        datas.append(x)
    return datas


def get_task_by_id(task_id):
    try:
        result = collection.find()
        for x in result:
            x.pop("_id")
            if task_id == x.get("task_id"):
                return x
    except:
        pass


def update_task(task_id, data):
    try:
        task_name = data.get("task_name")
        task_description = data.get("task_description")
        task_status = data.get("task_status")
        updated_at = data.get("updated_at")

        result = collection.find({"task_id": task_id})
        for x in result:
            if task_id == x.get("task_id"):
                update = {
                    "task_name": task_name,
                    "task_description": task_description,
                    "task_status": task_status,
                    "updated_at": updated_at
                }
                collection.update_one({"_id": x.get("_id")}, {"$set": update})
                datas = {
                    "task_id": task_id,
                    "task_name": task_name,
                    "task_description": task_description,
                    "task_status": task_status,
                    "updated_at": updated_at
                }
                return datas
    except:
        pass


def delete_task(task_id):
    try:
        result = collection.find({"task_id": task_id})
        for x in result:
            if task_id == x.get("task_id"):
                collection.delete_one({"_id": x.get("_id")})
                result = f"Task Id {task_id} deleted"
                return result
    except:
        pass