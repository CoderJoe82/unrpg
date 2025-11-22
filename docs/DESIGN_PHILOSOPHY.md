# Design Philosophy & Core Systems

> "The Game State is the Source of Truth. The AI is the Narrator."

## 1. The "Harmony" Setting (World & Tone)
**Concept:**
Unlike traditional fantasy where civilization fights back the wilds, this world features a symbiotic relationship between nature and architecture. Cities are built *into* trees, stone keeps are wrapped in living vines by design, and technology (gadgetry) works alongside druidic magic.

**The Rules of the World:**
1.  **No "Man vs. Nature":** Conflicts arise from Factions, Ideologies, and Ancient Forces, not from "Civilization vs. The Wilds."
2.  **The AI's Voice:** When generating descriptions, the AI must always emphasize this blend. A city street shouldn't just be cobblestone; it should be "cobblestone with bioluminescent moss acting as streetlights."

**Technical Implication:**
*   The `Zone` descriptions sent to the AI must include a "Harmony" tag or context instruction to ensure it doesn't generate generic grimdark fantasy text.

---

## 2. Attribute Philosophy (The "Diablo" Approach)
**Concept:**
Stats are manual, granular, and impactful. 
*   **No "Dead" Stats:** Every point allocated provides a tangible benefit.
*   **Soft Caps, Not Hard Walls:** We want to encourage specialization (min-maxing), but ensure that a "Jack of all Trades" is still viable.
*   **Respec Friendly:** Builds are investments, but players shouldn't feel paralyzed by fear of "ruining" a character.

**The Core Attributes:**
*   **Strength:** Physical Damage, Carry Weight.
*   **Agility:** Attack Speed, Crit Chance, Evasion.
*   **Intellect:** Magic Damage, Mana Pool.
*   **Willpower:** Stamina/Mana Regen, Status Resistance, Healing Potency.
*   **Vitality:** Health Pool, Physical Defense.

**Technical Implication:**
*   *Math:* Use linear scaling for the first 50 points, then diminishing returns (logarithmic) afterwards to prevent game-breaking numbers while still rewarding investment.

---

## 3. Progression: "You Are What You Do" (Elder Scrolls Style)
**Concept:**
Character levels differ from Skill levels. You do not magically get better at Swords by killing a rat with a Fireball.
*   **Usage-Based Growth:** Dealing damage with a Sword grants XP toward the `Sword_Skill`.
*   **Skill Milestones:** Reaching Level 25/50/75 in a skill unlocks specific perks (Active Abilities or Passive Buffs).

**Technical Implication:**
*   *The Event Listener:* The Combat System needs to emit events like `OnDamageDealt(Source="Sword", Amount=50)`. The Player class listens for this and adds XP to the relevant skill.

---

## 4. The Combat Triangle (Weapons)
**Concept:**
Weapons are defined by their *utility*, not just their damage numbers.

| Weapon Type | Core Identity | Special Mechanic |
| :--- | :--- | :--- |
| **Swords** | Consistency | **Crit & Parry:** Balanced offense/defense. |
| **Axes** | Attrition | **Bleeds & Trauma:** High top-end damage, stacking DoTs. |
| **Maces** | Control | **Stun & Stamina Drain:** Punishment for enemies with high armor. |
| **Daggers** | Burst | **Backstab & Poison:** Multipliers on unaware/debuffed targets. |
| **Bows** | Mobility | **Kiting:** High damage but requires distance management. |
| **Crossbows/Gadgets** | Tech/Pierce | **Armor Pen:** Slower, mechanical, ignores % of defense. |
| **Polearms** | Zone Control | **Reach & Sweeps:** Hit multiple enemies (Cleave) or prevent enemies from closing distance. |
| **Staves** | Magic Focus | **Spell Weaving:** Buffs magical output/efficiency. |

---

## 5. The Magic System (The 8 Schools)
**Concept:**
Magic is categorized by "Source," and each has a distinct playstyle.

*   **Fire:** Burst Damage, AoE, Burning.
*   **Frost:** Slows, Freezing, Shatter combos.
*   **Lightning:** Stuns, Chain Damage (jumps targets), Speed.
*   **Nature:** HoTs (Heal over Time), Poison, Rooting/Thorns.
*   **Darkness:** Curses, Debuffs (Weaken), Fear. (Not necessarily "Evil").
*   **Light:** Holy Damage (Smites), Blinding.
*   **Holy:** Pure Restoration, Wards, Protection buffs.
*   **Chaos:** The Wild Card.
    *   *Mechanic:* Has a chance to trigger effects from *any* other school, or unique "Wild Magic" surges.
    *   *Resistance:* Chaos Damage bypasses standard resistances but checks against a specific "Luck/Fate" stat.

---

## 6. Social & Reputation (Reactive World)
**Concept:**
Alignment is a *result* of actions, not a restriction on them.
*   **Reputation Vectors:** Instead of "Good/Evil," track "Order/Chaos" and "Benevolence/Cruelty."
*   **Faction Standing:** Every NPC belongs to a faction (Kingdom, Guild, Nature Spirit, Bandit Clan).
*   **Reactivity:** 
    *   A "Cruel" player might intimidate a merchant into lower prices but will be hunted by Guards.
    *   A "Nature Friend" might be attacked by Bandits but protected by Wolves in the forest.

**Technical Implication:**
*   *The Reaction Check:* When generating an interaction, the AI is fed the Player's Reputation Matrix.
*   *Prompt:* "The player approaches the Sacred Grove. Player Reputation: {Nature: -50 (Enemy)}. Describe the trees attacking them."

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