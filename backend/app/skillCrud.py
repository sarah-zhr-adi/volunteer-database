from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas


def create_skill(db: Session, skill: schemas.Skill):
    db_skill = models.Skill(
        skill_name=skill.skill_name,
        category=skill.category
    )
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def get_skill_by_name(db: Session, skill_name: str) -> models.Skill:
    return db.query(models.Skill).filter(models.Skill.skill_name == skill_name).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100) -> List[models.Skill]:
    return db.query(models.Skill).offset(skip).limit(limit).all()


def get_skill_by_id(db: Session, skill_id: int) -> models.Skill:
    return db.query(models.Skill).filter(models.Skill.skill_id == skill_id).first()


def update_skill(db: Session, old_skill_id: int, patch_object: schemas.Skill) -> models.Skill:
    db.query(models.Skill).filter(models.Skill.skill_id == old_skill_id).update(patch_object, synchronize_session='fetch')
    db.commit()
    return patch_object


def delete_skill(db: Session, del_skill_id: int) -> int:
    data = db.query(models.Skill).get(del_skill_id)
    if data:
        db.delete(data)
        db.commit()
        return del_skill_id
    else:
        return 0
