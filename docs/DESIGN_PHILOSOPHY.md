# Design Philosophy & Core Systems

> "The Game State is the Source of Truth. The AI is the Narrator."

## 0. Core Gameplay Identity
**Genre:** 2D Text-Driven / Menu-Based RPG.
**Visual Style:** UI-Heavy. No character sprites walking on a map. The "World" is navigated via menus, text descriptions, and buttons.
**Interaction:** Mouse-driven interface (Point & Click) for selecting options, managing inventory, and combat choices.
**Reference:** Think *Disco Elysium* (dialogue/text focus) meets *Darkest Dungeon* (menu-based management) but without the walking.

## 1. The "Harmony" Setting (World & Tone)
**Concept:**
Unlike traditional fantasy where civilization fights back the wilds, this world features a symbiotic relationship between nature and architecture. Cities are built *into* trees, stone keeps are wrapped in living vines by design, and technology (gadgetry) works alongside druidic magic.

**The Rules of the World:**
1.  **No "Man vs. Nature":** Conflicts arise from Factions, Ideologies, and Ancient Forces, not from "Civilization vs. The Wilds."
2.  **The AI's Voice:** When generating descriptions, the AI must always emphasize this blend. A city street shouldn't just be cobblestone; it should be "cobblestone with bioluminescent moss acting as streetlights."

**Technical Implication:**
*   The `Zone` descriptions sent to the AI must include a "Harmony" tag or context instruction to ensure it doesn't generate generic grimdark fantasy text.

---

## 2. Attribute Philosophy (The "Seven Pillars")
**Concept:**
Stats are manual, granular, and impactful. We adhere to a "Soft Cap" philosophy similar to souls-likes and ARPGs:
*   **Investment Matters:** Every point provides a tangible benefit.
*   **Diminishing Returns:** Linear scaling up to a threshold (e.g., 40 points), then logarithmic scaling. This allows min-maxing but prevents one stat from breaking the game math.

**The Core Attributes:**

| Attribute | Primary Function | Secondary Benefits |
| :--- | :--- | :--- |
| **Strength** | Melee Power (Swords, Axes, Maces) | Carry Weight, Physical Guard Breaking. |
| **Dexterity** | Ranged Power, Daggers, Polearms | Attack Speed, Critical Hit Chance, Evasion. |
| **Constitution** | Health Pool (HP) | Physical Defense, Stamina Pool, Poison Resistance. |
| **Charisma** | Social Influence & **Command Limit** | **Max number of active summons**, Merchant Prices, NPC Reaction Checks. |
| **Intellect** | Arcane Magic (Fire, Frost, Lightning, Chaos) | Mana Pool, Elemental Resistance, **Power of Arcane Summons (e.g., Elementals, Golems).** |
| **Wisdom** | Nature Magic (Druidic, Poison, DoTs) | Perception, Mana Regen, **Power of Nature Summons (e.g., Wolves, Treants).** |
| **Faith** | Divine Magic (Holy, Light, Wards) | Healing Potency, Buff Duration, **Power of Holy Summons (e.g., Spirits, Guardians).** |

**Technical Implication:**
*   *The Summoner's Synergy:* Minion builds require a dual-stat investment.
    *   **Charisma** acts as the "Bandwidth" (Can I control 3 wolves?).
    *   **Magic Stat** acts as the "Quality" (How much damage do the wolves do?).
    *   *Example:* A Necromancer needs **CHA** to raise *many* skeletons, but needs **INT/Darkness** to make them actually *strong*.

---

## 3. Progression: The Hybrid System
**Concept:**
We combine "Usage-Based Growth" (Skyrim) with "Manual Stat Allocation" (Diablo).

**The Rules of Growth:**
1.  **Usage-Based Skills:** You do not get XP for killing a rat. You get XP for *hitting* the rat with a Sword (`Sword_Skill` goes up).
2.  **Skill Milestones:** When your Skills level up enough, your **Character Level** increases.
3.  **Manual Reward:** When Character Level increases, you gain **3 Attribute Points** to manually spend on the Seven Pillars.

**The Math (Level 60 Cap):**
*   **Max Level:** 60
*   **Points per Level:** 3
*   **Total Points:** 180 (plus starting base stats).
*   **Soft Cap:** 40 points (Diminishing returns start).
*   **Hard Cap:** 99 points.

**Build Diversity:**
With 180 points, a player can:
*   **Max 2 Stats** to 99 (Pure Specialist).
*   **Soft-Cap 4 Stats** to 40 (Versatile Hybrid).

**Technical Implication:**
*   *The Event Listener:* The Combat System emits `OnDamageDealt(Source="Sword", Amount=50)`. The Player class listens, adds XP to `Sword_Skill`. If `Sword_Skill` levels up, check if `Character_Level` should also level up.