from typing import List

import src.crud.notes as crud
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.notes import NoteOutSchema, NoteInSchema, UpdateNote
from src.schemas.token import Status
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

router = APIRouter(prefix="/api")


@router.get(
    "/notes",
    response_model=List[NoteOutSchema],
)
async def get_notes():
    return await crud.get_notes()


@router.get(
    "/note/{note_id}",
    response_model=NoteOutSchema,
)
async def get_note(note_id: int) -> NoteOutSchema:
    try:
        return await crud.get_note(note_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )


@router.post(
    "/notes", response_model=NoteOutSchema
)
async def create_note(
    note: NoteInSchema
) -> NoteOutSchema:
    return await crud.create_note(note)


@router.patch(
    "/note/{note_id}",
    response_model=NoteOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_note(
    note_id: int,
    note: UpdateNote,
) -> NoteOutSchema:
    return await crud.update_note(note_id, note)


@router.delete(
    "/note/{note_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_note(
    note_id: int
):
    return await crud.delete_note(note_id)
