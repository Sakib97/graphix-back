from fastapi import APIRouter, HTTPException, Depends, status, Request, Response, Header, BackgroundTasks


kb_router = APIRouter(
    prefix="/kb", 
    tags=["Knowledge_Base"])

@kb_router.get("/parse-repo")
async def parse_repository(repo_url: str):

    parsed_data = {
        "repo_url": repo_url,
        "commit_history": [],
        "branches": [],
        "files": []
    }

    return parsed_data