from src.libs.db import db
from src.models.item import Item
from src.types.request.item_request import ItemRequest
from src.types.response.item_response import ItemResponse
from src.libs.exceptions import NotFound, BadRequest
from pydantic import ValidationError

class ItemService:
    @staticmethod
    def create_item(payload: dict) -> ItemResponse:
        try:
            data = ItemRequest(**payload)
        except ValidationError as e:
            raise BadRequest(e.errors())

        new_item = Item(
            name=data.name,
            description=data.description,
            price=data.price
        )
        db.session.add(new_item)
        db.session.commit()

        return ItemResponse.from_orm(new_item)

    @staticmethod
    def get_all_items() -> list[ItemResponse]:
        items = Item.query.all()

        return [ItemResponse.from_orm(item) for item in items]

    @staticmethod
    def get_item_by_id(item_id: int) -> ItemResponse:
        item = Item.query.get(item_id)

        if not item:
            raise NotFound(f"Item with id {item_id} not found")

        return ItemResponse.from_orm(item)

    @staticmethod
    def update_item(item_id: int, payload: dict) -> ItemResponse:
        item = Item.query.get(item_id)

        if not item:
            raise NotFound(f"Item with id {item_id} not found")

        try:
            data = ItemRequest(**payload)
        except ValidationError as e:
            raise BadRequest(e.errors())

        item.name = data.name
        item.description = data.description
        item.price = data.price
        db.session.commit()

        return ItemResponse.from_orm(item)

    @staticmethod
    def delete_item(item_id: int) -> None:
        item = Item.query.get(item_id)

        if not item:
            raise NotFound(f"Item with id {item_id} not found")

        db.session.delete(item)
        db.session.commit()