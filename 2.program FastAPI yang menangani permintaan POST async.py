from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import httpx
from typing import Optional, List
import json

app = FastAPI(title="Async POST API", version="1.0.0")

# Pydantic models untuk request bodies
class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"

class DataProcessing(BaseModel):
    items: List[str]
    operation: str

# Simulasi database (dalam aplikasi nyata, gunakan database)
users_db = []
tasks_db = []

@app.get("/")
async def root():
    return {"message": "FastAPI Async POST Handler - Server Running!"}

# 1. POST sederhana untuk membuat user
@app.post("/users")
async def create_user(user: UserCreate):
    """Membuat user baru secara async"""
    # Simulasi operasi async (misalnya validasi email)
    await asyncio.sleep(0.1)  # Simulasi delay
    
    # Cek apakah email sudah ada
    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    new_user = {
        "id": len(users_db) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    users_db.append(new_user)
    
    return {"message": "User created successfully", "user": new_user}

# 2. POST dengan operasi async eksternal (simulasi API call)
@app.post("/tasks")
async def create_task(task: TaskCreate):
    """Membuat task dan mengirim notifikasi async"""
    
    # Simulasi pembuatan task
    new_task = {
        "id": len(tasks_db) + 1,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": "pending"
    }
    tasks_db.append(new_task)
    
    # Simulasi pengiriman notifikasi async
    await send_notification(new_task)
    
    return {"message": "Task created and notification sent", "task": new_task}

async def send_notification(task: dict):
    """Simulasi pengiriman notifikasi async"""
    await asyncio.sleep(0.2)  # Simulasi delay network
    print(f"Notification sent for task: {task['title']}")

# 3. POST dengan multiple async operations
@app.post("/process-data")
async def process_data(data: DataProcessing):
    """Memproses data dengan multiple operasi async"""
    
    if data.operation not in ["uppercase", "lowercase", "reverse"]:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    # Proses setiap item secara concurrent
    processed_items = await asyncio.gather(
        *[process_item(item, data.operation) for item in data.items]
    )
    
    return {
        "message": "Data processed successfully",
        "original_count": len(data.items),
        "processed_items": processed_items,
        "operation": data.operation
    }

async def process_item(item: str, operation: str) -> str:
    """Memproses satu item secara async"""
    await asyncio.sleep(0.05)  # Simulasi processing time
    
    if operation == "uppercase":
        return item.upper()
    elif operation == "lowercase":
        return item.lower()
    elif operation == "reverse":
        return item[::-1]
    
    return item

# 4. POST dengan HTTP client async
@app.post("/external-api")
async def call_external_api(data: dict):
    """Memanggil API eksternal secara async"""
    
    async with httpx.AsyncClient() as client:
        try:
            # Contoh call ke JSONPlaceholder API
            response = await client.post(
                "https://jsonplaceholder.typicode.com/posts",
                json={
                    "title": data.get("title", "Default Title"),
                    "body": data.get("body", "Default Body"),
                    "userId": data.get("userId", 1)
                }
            )
            
            if response.status_code == 201:
                return {
                    "message": "External API call successful",
                    "response": response.json()
                }
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail="External API call failed")
                
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, 
                              detail=f"Request error: {str(e)}")

# 5. POST dengan file processing async
@app.post("/batch-process")
async def batch_process(batch_data: dict):
    """Memproses batch data secara async"""
    
    items = batch_data.get("items", [])
    if not items:
        raise HTTPException(status_code=400, detail="No items to process")
    
    # Proses dalam chunks untuk efisiensi
    chunk_size = 5
    chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
    
    results = []
    for chunk in chunks:
        chunk_results = await process_chunk(chunk)
        results.extend(chunk_results)
    
    return {
        "message": "Batch processing completed",
        "total_items": len(items),
        "processed_items": len(results),
        "results": results
    }

async def process_chunk(chunk: List[str]) -> List[dict]:
    """Memproses chunk data secara async"""
    await asyncio.sleep(0.1)  # Simulasi processing
    
    return [
        {
            "original": item,
            "processed": f"processed_{item}",
            "length": len(item)
        }
        for item in chunk
    ]

# Endpoint untuk melihat data (GET)
@app.get("/users")
async def get_users():
    return {"users": users_db}

@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks_db}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
