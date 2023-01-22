from __future__ import annotations

# import model
from domain.model import OrderLine, allocate as _allocate
from adapters.repository import AbstractRepository


class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def allocate(line: OrderLine, repository: AbstractRepository, session) -> str:
    batches = repository.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku(f"Invalid sku {line.sku}")
    # batchref = model.allocate(line, batches)
    batchref = _allocate(line, batches)

    session.commit()
    return batchref
