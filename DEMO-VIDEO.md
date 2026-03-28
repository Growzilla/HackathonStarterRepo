# AutoPilot Demo Video — Script & Screenshots

## Format
~2-3 minutes. Screenshots with voiceover narration. Fast-paced, show-don't-tell.

---

## Shot 1: THE HOOK (5 sec)
**Screenshot**: Full `/autopilot` page — Agents tab, all 5 agent cards visible with avatars and green action counts
**Script**: "What if your Shopify store ran itself? Meet AutoPilot — 5 AI agents that monitor, decide, and act on your store. Autonomously. 24/7."

---

## Shot 2: THE AGENTS (15 sec)
**Screenshot**: Close-up crop of the 5 agent cards (Pickle Rick, Hank, Ron, Marty, Marcus) with status indicators pulsing green
**Script**:
- "Rick watches operations — he just deactivated a product with zero stock."
- "Hank scored 25 products and created a purchase order for the Black Hoodie."
- "Ron found slow movers and created clearance discount codes."
- "Marty segmented 40 customers and launched a win-back campaign."
- "Marcus coordinates them all — he sees the big picture."

---

## Shot 3: THE DIALOGUE (20 sec)
**Screenshot**: Agent Dialogue feed showing personality-rich messages — especially Marcus coordinating and Marty pushing back
**Script**: "Every agent has a personality powered by Claude. Watch them talk — Marty pushes back on Ron's discounts: 'Before we slash prices, let me try a content play first.' Marcus mediates: 'Rick's stockout alert and Ron's discount are about the same product — I'm overriding.'"

---

## Shot 4: CLICK TO FILTER (5 sec)
**Screenshot**: Click Rick's card → dialogue filters to only Rick's actions (show the accent border on Rick's card)
**Script**: "Click any agent to see just their actions. Click again to see everyone."

---

## Shot 5: INVENTORY INTELLIGENCE (15 sec)
**Screenshot**: Inventory tab — DataTable with Score, Tier badges (Core/Strong/Slow/Exit), Days Left in red, Trend arrows
**Script**: "Hank scores every product on a composite of revenue, velocity, stock health, and trend. Core products get protected. Exit products get flagged for clearance. Hover any column header to see exactly how the score is calculated."

---

## Shot 6: PURCHASE ORDERS (10 sec)
**Screenshot**: `/purchase-orders` page showing PO-20260328-001 with line items expanded, "Advance to ordered" button visible
**Script**: "When Hank detects a product running low, he doesn't just alert you — he creates a draft purchase order. 144 units of the Black Hoodie, estimated cost $5,126. One click to advance it through the pipeline."

---

## Shot 7: INBOUND STOCK (5 sec)
**Screenshot**: Inbound Stock section on the PO page showing products with units on the way
**Script**: "And he's smart about it — if there's already a PO inbound, Hank won't double-order. Effective runway includes incoming stock."

---

## Shot 8: CUSTOMER SEGMENTS (10 sec)
**Screenshot**: `/segments` page — donut chart + customer table with Champions/Loyal/At Risk badges
**Script**: "Marty segments customers using RFM analysis. 4 Champions driving 29% of lifetime value. 4 At Risk customers with $1,700 of recoverable revenue. Each segment triggers targeted campaigns."

---

## Shot 9: REVERT AN ACTION (5 sec)
**Screenshot**: Hover over a Ron discount action → show the "↩ Revert" button, then show a reverted action with strikethrough
**Script**: "Don't agree with an agent's decision? Hover and revert. The action is undone, and the agent will re-evaluate on the next cycle."

---

## Shot 10: LIVE FEED (10 sec)
**Screenshot**: Live tab — SSE events streaming in on the left, agent reactions on the right
**Script**: "Everything is real-time. Orders stream in via SSE. Agents react within 60 seconds — checking stock, recalculating scores, triggering actions."

---

## Shot 11: ACTIONS TAB (5 sec)
**Screenshot**: Actions tab — KPI cards showing Total Actions, Discounts Created, Alerts Sent, Health Issues
**Script**: "Full audit trail. Every action logged, every decision explained."

---

## Shot 12: THE CLOSE (10 sec)
**Screenshot**: Full `/autopilot` page, zoomed out hero shot with all cards and dialogue visible
**Script**: "AutoPilot. Five agents. One command center. Your store runs itself. Built in 24 hours at the NS Shopify Hackathon."

---

## Screenshot Checklist

Take these from `http://localhost:3000` with the backend running:

1. [ ] `/autopilot` — Agents tab, full page
2. [ ] `/autopilot` — Close crop of 5 agent cards only
3. [ ] `/autopilot` — Agent Dialogue scrolled to show personality messages
4. [ ] `/autopilot` — Rick's card selected (accent border), filtered dialogue
5. [ ] `/autopilot` — Inventory tab, full DataTable
6. [ ] `/purchase-orders` — PO table + expanded line items
7. [ ] `/purchase-orders` — Inbound Stock section
8. [ ] `/segments` — Donut chart + customer table
9. [ ] `/autopilot` — Hover on action showing Revert button
10. [ ] `/autopilot` — Live tab with events + reactions
11. [ ] `/autopilot` — Actions tab with KPI cards
12. [ ] `/autopilot` — Full page hero shot (zoomed out)

## Tips
- Make sure backend has been running for at least 1 cycle so actions are populated
- The agent dialogue with Claude personalities is the money shot — make sure it's visible
- Dark theme screenshots look great — no need to change anything
