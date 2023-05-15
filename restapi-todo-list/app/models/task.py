from shortuuid import uuid
from pydantic import BaseModel, Field, ValidationError, validator
from datetime import date, datetime

class CreateTaskSchema(BaseModel):
    task_id: str = Field(default_factory=uuid)
    task_name: str = Field(...)
    task_description: str = Field(...)
    task_status: str = Field(...)
    created_at: date = Field(default_factory=datetime.now)

    @validator('task_name')
    def task_name_must_not_be_blank(cls, v):
        if v == '':
            raise ValueError('task_name must not be blank')
        return v
    
    @validator('task_description')
    def task_description_must_not_be_blank(cls, v):
        if v == '':
            raise ValueError('task_description must not be blank')
        return v
    
    @validator('task_status')
    def task_status_must_be_valid(cls, v):
        if v not in ['todo', 'doing', 'done']:
            raise ValueError('task_status must be todo, doing or done')
        return v

class UpdateTaskSchema(BaseModel):
    task_name: str = Field(...)
    task_description: str = Field(...)
    task_status: str = Field(...)
    updated_at: date = Field(default_factory=datetime.now)

class DeleteTaskSchema(BaseModel):
    task_id: str = Field(default_factory=uuid)
