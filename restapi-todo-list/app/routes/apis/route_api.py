from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.controllers import *
from app.response_helper import *
from app.models import *

router = APIRouter()

@router.post("/api/create_task")
def create_new_task(new_task: CreateTaskSchema = Body(...)):
    check_datas = create_task(jsonable_encoder(new_task))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success_response(check_datas, "Successfully created task"))


@router.get("/api/read_task")
def read_all_task():
    check_datas = get_task()
    if check_datas:
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(check_datas, "Successfully retrieved task"))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=fail_response(message=f"Task not found"))


@router.get("/api/read_task/{task_id}")
def read_task_by_id(task_id: str):
    check_datas = get_task_by_id(task_id)
    if check_datas:
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(check_datas, "Successfully retrieved task by Id"))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=fail_response(message=f"Task Id {task_id} not found"))


@router.put("/api/update_task/{task_id}")
def update_task_by_id(task_id: str, data: UpdateTaskSchema = Body(...)):
    check_datas = update_task(task_id, jsonable_encoder(data))
    if check_datas:
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(check_datas, "Successfully updated task by Id"))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=fail_response(message=f"Task Id {task_id} not found"))


@router.delete("/api/delete_task/{task_id}")
def delete_task_by_id(task_id: str):
    check_datas = delete_task(task_id)
    if check_datas:
        return JSONResponse(status_code=status.HTTP_200_OK, content=success_response(check_datas, "Successfully deleted task by Id"))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=fail_response(message=f"Task Id {task_id} not found"))