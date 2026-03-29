"""Load pre-generated agent actions, states, POs, and discounts from fixture files."""
import json
import logging
from pathlib import Path

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.models import AgentAction, AgentState, PurchaseOrder, POLineItem, Discount

logger = logging.getLogger(__name__)

FIXTURE_DIR = Path(__file__).parent


async def load_fixtures(db: AsyncSession) -> bool:
    """Load fixture data if agent_actions table is empty. Returns True if loaded."""
    result = await db.execute(select(func.count()).select_from(AgentAction))
    if (result.scalar() or 0) > 0:
        return False

    # Load actions
    actions_file = FIXTURE_DIR / "fixture_actions.json"
    if actions_file.exists():
        actions = json.loads(actions_file.read_text())
        for i, a in enumerate(actions):
            db.add(AgentAction(
                action_id=a["id"],
                timestamp=a["timestamp"],
                agent=a["agent"],
                action_type=a["type"],
                title=a["title"],
                details=a.get("details", ""),
                commentary=a.get("commentary", ""),
                status=a.get("status", "success"),
                product_id=a.get("productId"),
                cycle=a.get("cycle", 1),
            ))
        logger.info("Loaded %d agent actions from fixture", len(actions))

    # Load states
    states_file = FIXTURE_DIR / "fixture_states.json"
    if states_file.exists():
        states = json.loads(states_file.read_text())
        for s in states:
            db.add(AgentState(
                name=s["name"],
                status=s.get("status", "active"),
                last_action=s.get("lastAction"),
                action_count=s.get("actionCount", 0),
                last_cycle_at=s.get("lastCycleAt"),
            ))
        logger.info("Loaded %d agent states from fixture", len(states))

    # Load POs
    pos_file = FIXTURE_DIR / "fixture_pos.json"
    if pos_file.exists():
        pos = json.loads(pos_file.read_text())
        for p in pos:
            po = PurchaseOrder(
                po_number=p["poNumber"],
                status=p.get("status", "draft"),
                total_qty=p.get("totalQty", 0),
                total_cost=p.get("totalCost", 0),
                notes=p.get("notes", ""),
                created_by=p.get("createdBy", "Hank"),
                created_at=p.get("createdAt", ""),
                updated_at=p.get("updatedAt", ""),
            )
            db.add(po)
            await db.flush()
            for item in p.get("lineItems", []):
                db.add(POLineItem(
                    po_id=po.id,
                    product_id=item.get("productId", ""),
                    product_title=item.get("productTitle", ""),
                    qty=item.get("qty", 0),
                    cost_per_unit=item.get("costPerUnit", 0),
                    total_cost=item.get("totalCost", 0),
                ))
        logger.info("Loaded %d purchase orders from fixture", len(pos))

    # Load discounts
    discounts_file = FIXTURE_DIR / "fixture_discounts.json"
    if discounts_file.exists():
        discounts = json.loads(discounts_file.read_text())
        for d in discounts:
            db.add(Discount(
                code=d["code"],
                percentage=d.get("percentage", 0),
                product_id=d.get("productId"),
                product_title=d.get("productTitle", ""),
                created_by=d.get("createdBy", "Ron"),
                status=d.get("status", "active"),
                created_at=d.get("createdAt", ""),
            ))
        logger.info("Loaded %d discounts from fixture", len(discounts))

    await db.commit()
    return True
