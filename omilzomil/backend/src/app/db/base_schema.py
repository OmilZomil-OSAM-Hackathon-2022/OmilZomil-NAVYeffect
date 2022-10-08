from pydantic import BaseModel, Field
from pydantic.main import ModelMetaclass
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Response(BaseModel):
    success: Optional[bool] = Field(None, description="result")
    message: Optional[str] = Field(None, description="message")

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "success",
            }
        }


class AllOptional(ModelMetaclass):
    # 모든 맴버 변수들을 optional로 변경
    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
        namespaces["__annotations__"] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)


class Omit(ModelMetaclass):
    """
    class OmittedTaxPrice(BaseItem, metaclass=Omit):
        class Config:
            omit_fields = {'tax', 'price'}
    이렇게 class Config에 omit_fields를 선언해놓으면 해당 필드를 제거한 새로운 schema를 얻을 수 있다.
    """

    def __new__(self, name, bases, namespaces, **kwargs):
        omit_fields = getattr(namespaces.get("Config", {}), "omit_fields", {})
        fields = namespaces.get("__fields__", {})
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            fields.update(base.__fields__)
            annotations.update(base.__annotations__)
        merged_keys = fields.keys() & annotations.keys()
        [merged_keys.add(field) for field in fields]
        new_fields = {}
        new_annotations = {}
        for field in merged_keys:
            if not field.startswith("__") and field not in omit_fields:
                new_annotations[field] = annotations.get(field, fields[field].type_)
                new_fields[field] = fields[field]
        namespaces["__annotations__"] = new_annotations
        namespaces["__fields__"] = new_fields
        return super().__new__(self, name, bases, namespaces, **kwargs)
