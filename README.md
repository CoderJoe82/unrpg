# Unnamed RPG Project
A 2D text/menu-driven fantasy RPG built with Python and Pygame, featuring turn-based combat, dynamic AI-generated content, and a richly detailed eco-integration world where player identity and choices truly matter. A learning-focused project using AI as a teaching tool rather than a code generator.
## 🎮 Project Vision
This RPG combines handcrafted starting content with AI-driven emergent gameplay, creating a world where:
- Player choices genuinely impact the story through AI-generated events
- Turn-based combat emphasizes strategy over button-mashing
- Identity (race, class, stats) shapes how you perceive and interact with the world
- Nature and civilization exist in harmonious "eco-integration"
- The goddess Xanthria maintains balance through dynamic world events
## 📚 Learning Journey
This project is a personal educational endeavor. I'm using AI as a mentor to teach me professional game development practices, not to write code for me. The goal is to deeply understand:
- Object-oriented design patterns in game development
- Scalable project architecture
- Data-driven game design
- AI/LLM integration techniques
## 🗂️ Project Structure

├── docs/
│   ├── design/
│   │   ├── world_bible.md
│   │   ├── game_systems.md
│   │   ├── ai_integration_spec.md
│   │   └── balance_notes.md
│   ├── technical/
│   │   ├── architecture.md
│   │   ├── state_contracts.md
│   │   ├── event_bus_spec.md
│   │   └── class_diagrams.md
│   └── progress/
│       ├── milestones.md
│       └── changelog.md
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── game.py
│   │   ├── config.py
│   │   ├── settings.py
│   │   │
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── i_state.py
│   │   │   ├── i_entity.py
│   │   │   ├── i_component.py
│   │   │   ├── i_renderable.py
│   │   │   ├── i_updateable.py
│   │   │   ├── i_serializable.py
│   │   │   └── i_validator.py
│   │   │
│   │   └── base/
│   │       ├── __init__.py
│   │       ├── base_state.py
│   │       ├── base_entity.py
│   │       ├── base_component.py
│   │       ├── base_manager.py
│   │       ├── base_system.py
│   │       └── base_validator.py
│   │
│   ├── managers/
│   │   ├── __init__.py
│   │   ├── state_manager.py
│   │   ├── event_manager.py
│   │   ├── resource_manager.py
│   │   ├── save_manager.py
│   │   ├── ai_manager.py
│   │   ├── input_manager.py
│   │   └── validation_manager.py
│   │
│   ├── states/
│   │   ├── __init__.py
│   │   ├── title_state.py
│   │   ├── character_creation_state.py
│   │   ├── world_map_state.py
│   │   ├── exploration_state.py
│   │   ├── combat_state.py
│   │   ├── dialogue_state.py
│   │   ├── inventory_state.py
│   │   ├── merchant_state.py
│   │   ├── rest_state.py
│   │   └── settings_state.py
│   │
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── living_entity.py
│   │   ├── character.py
│   │   ├── player.py
│   │   ├── npc.py
│   │   ├── enemy.py
│   │   ├── companion.py
│   │   ├── summon.py
│   │   └── merchant.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── stats_component.py
│   │   ├── health_component.py
│   │   ├── mana_component.py
│   │   ├── inventory_component.py
│   │   ├── equipment_component.py
│   │   ├── skills_component.py
│   │   ├── status_effects_component.py
│   │   ├── identity_component.py
│   │   ├── faction_component.py
│   │   └── ai_memory_component.py
│   │
│   ├── systems/
│   │   ├── __init__.py
│   │   │
│   │   ├── combat/
│   │   │   ├── __init__.py
│   │   │   ├── combat_system.py
│   │   │   ├── turn_manager.py
│   │   │   ├── damage_calculator.py
│   │   │   ├── targeting_system.py
│   │   │   │
│   │   │   ├── actions/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base_action.py
│   │   │   │   ├── attack_action.py
│   │   │   │   ├── skill_action.py
│   │   │   │   ├── item_action.py
│   │   │   │   ├── defend_action.py
│   │   │   │   └── flee_action.py
│   │   │   │
│   │   │   └── status_effects/
│   │   │       ├── __init__.py
│   │   │       ├── base_effect.py
│   │   │       ├── bleed_effect.py
│   │   │       ├── burn_effect.py
│   │   │       ├── poison_effect.py
│   │   │       ├── stun_effect.py
│   │   │       ├── freeze_effect.py
│   │   │       └── buff_effect.py
│   │   │
│   │   ├── dialogue/
│   │   │   ├── __init__.py
│   │   │   ├── dialogue_system.py
│   │   │   ├── keyword_parser.py
│   │   │   ├── response_generator.py
│   │   │   └── context_manager.py
│   │   │
│   │   ├── progression/
│   │   │   ├── __init__.py
│   │   │   ├── experience_system.py
│   │   │   ├── leveling_system.py
│   │   │   ├── skill_tree_system.py
│   │   │   └── prestige_system.py
│   │   │
│   │   ├── perception/
│   │   │   ├── __init__.py
│   │   │   ├── identity_system.py
│   │   │   ├── passive_check_system.py
│   │   │   └── context_awareness.py
│   │   │
│   │   ├── world/
│   │   │   ├── __init__.py
│   │   │   ├── location_system.py
│   │   │   ├── encounter_system.py
│   │   │   ├── time_system.py
│   │   │   └── weather_system.py
│   │   │
│   │   ├── economy/
│   │   │   ├── __init__.py
│   │   │   ├── trading_system.py
│   │   │   ├── price_calculator.py
│   │   │   └── merchant_inventory.py
│   │   │
│   │   └── quest/
│   │       ├── __init__.py
│   │       ├── quest_system.py
│   │       ├── objective_tracker.py
│   │       └── reward_system.py
│   │
│   ├── items/
│   │   ├── __init__.py
│   │   ├── base_item.py
│   │   ├── equipment/
│   │   │   ├── __init__.py
│   │   │   ├── base_equipment.py
│   │   │   ├── weapon.py
│   │   │   ├── armor.py
│   │   │   ├── accessory.py
│   │   │   └── equipment_slots.py
│   │   ├── consumables/
│   │   │   ├── __init__.py
│   │   │   ├── base_consumable.py
│   │   │   ├── potion.py
│   │   │   ├── food.py
│   │   │   └── scroll.py
│   │   └── materials/
│   │       ├── __init__.py
│   │       ├── base_material.py
│   │       ├── crafting_material.py
│   │       └── quest_item.py
│   │
│   ├── skills/
│   │   ├── __init__.py
│   │   ├── base_skill.py
│   │   ├── physical/
│   │   │   ├── __init__.py
│   │   │   ├── warrior_skills.py
│   │   │   ├── rogue_skills.py
│   │   │   └── ranger_skills.py
│   │   ├── magic/
│   │   │   ├── __init__.py
│   │   │   ├── base_spell.py
│   │   │   ├── fire_magic.py
│   │   │   ├── ice_magic.py
│   │   │   ├── lightning_magic.py
│   │   │   ├── nature_magic.py
│   │   │   ├── holy_magic.py
│   │   │   ├── dark_magic.py
│   │   │   ├── arcane_magic.py
│   │   │   └── chaos_magic.py
│   │   └── summoning/
│   │       ├── __init__.py
│   │       ├── base_summon_skill.py
│   │       ├── elemental_summons.py
│   │       ├── beast_summons.py
│   │       └── divine_summons.py
│   │
│   ├── factories/
│   │   ├── __init__.py
│   │   ├── entity_factory.py
│   │   ├── item_factory.py
│   │   ├── skill_factory.py
│   │   ├── quest_factory.py
│   │   ├── encounter_factory.py
│   │   └── ai_content_factory.py
│   │
│   ├── validators/
│   │   ├── __init__.py
│   │   ├── schema_validator.py
│   │   ├── data_validators/
│   │   │   ├── __init__.py
│   │   │   ├── character_validator.py
│   │   │   ├── item_validator.py
│   │   │   ├── skill_validator.py
│   │   │   ├── quest_validator.py
│   │   │   └── location_validator.py
│   │   ├── ai_validators/
│   │   │   ├── __init__.py
│   │   │   ├── ai_response_validator.py
│   │   │   ├── npc_generation_validator.py
│   │   │   ├── quest_generation_validator.py
│   │   │   ├── dialogue_validator.py
│   │   │   └── encounter_validator.py
│   │   └── game_validators/
│   │       ├── __init__.py
│   │       ├── balance_validator.py
│   │       ├── lore_validator.py
│   │       ├── save_data_validator.py
│   │       └── input_validator.py
│   │
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── ai_behaviors/
│   │   │   ├── __init__.py
│   │   │   ├── base_behavior.py
│   │   │   ├── aggressive_behavior.py
│   │   │   ├── defensive_behavior.py
│   │   │   ├── tactical_behavior.py
│   │   │   ├── support_behavior.py
│   │   │   └── flee_behavior.py
│   │   └── combat_strategies/
│   │       ├── __init__.py
│   │       ├── base_strategy.py
│   │       ├── melee_strategy.py
│   │       ├── ranged_strategy.py
│   │       ├── magic_strategy.py
│   │       └── hybrid_strategy.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── base_ui.py
│   │   ├── ui_manager.py
│   │   │
│   │   ├── widgets/
│   │   │   ├── __init__.py
│   │   │   ├── base_widget.py
│   │   │   ├── button.py
│   │   │   ├── panel.py
│   │   │   ├── text_box.py
│   │   │   ├── menu.py
│   │   │   ├── dialog.py
│   │   │   ├── progress_bar.py
│   │   │   ├── stat_display.py
│   │   │   └── tooltip.py
│   │   │
│   │   ├── layouts/
│   │   │   ├── __init__.py
│   │   │   ├── base_layout.py
│   │   │   ├── combat_layout.py
│   │   │   ├── dialogue_layout.py
│   │   │   ├── inventory_layout.py
│   │   │   ├── character_sheet_layout.py
│   │   │   └── merchant_layout.py
│   │   │
│   │   └── renderers/
│   │       ├── __init__.py
│   │       ├── text_renderer.py
│   │       ├── sprite_renderer.py
│   │       └── effect_renderer.py
│   │
│   ├── events/
│   │   ├── __init__.py
│   │   ├── base_event.py
│   │   ├── game_events.py
│   │   ├── combat_events.py
│   │   ├── dialogue_events.py
│   │   └── world_events.py
│   │
│   ├── data_models/
│   │   ├── __init__.py
│   │   ├── race.py
│   │   ├── character_class.py
│   │   ├── faction.py
│   │   ├── location.py
│   │   ├── quest.py
│   │   └── save_data.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── validation.py
│       ├── math_helpers.py
│       ├── text_formatter.py
│       ├── dice_roller.py
│       └── constants.py
│
├── data/
│   ├── static/
│   │   ├── races/
│   │   │   ├── elf.json
│   │   │   ├── dwarf.json
│   │   │   ├── human.json
│   │   │   └── vargr.json
│   │   │
│   │   ├── classes/
│   │   │   ├── warrior.json
│   │   │   ├── mage.json
│   │   │   ├── rogue.json
│   │   │   └── acolyte.json
│   │   │
│   │   ├── starting_locations/
│   │   │   ├── arbor_city.json
│   │   │   ├── mountain_home.json
│   │   │   └── river_port.json
│   │   │
│   │   ├── items/
│   │   │   ├── weapons.json
│   │   │   ├── armor.json
│   │   │   ├── accessories.json
│   │   │   ├── consumables.json
│   │   │   └── materials.json
│   │   │
│   │   ├── skills/
│   │   │   ├── warrior_skills.json
│   │   │   ├── mage_skills.json
│   │   │   ├── rogue_skills.json
│   │   │   └── acolyte_skills.json
│   │   │
│   │   ├── npcs/
│   │   │   ├── starting_zone/
│   │   │   │   ├── quest_givers.json
│   │   │   │   ├── merchants.json
│   │   │   │   └── companions.json
│   │   │   └── templates/
│   │   │       └── npc_archetypes.json
│   │   │
│   │   ├── quests/
│   │   │   ├── starting_zone/
│   │   │   │   ├── main_quests.json
│   │   │   │   └── side_quests.json
│   │   │   └── templates/
│   │   │       └── quest_structures.json
│   │   │
│   │   ├── enemies/
│   │   │   ├── starting_zone_enemies.json
│   │   │   └── enemy_templates.json
│   │   │
│   │   └── encounters/
│   │       ├── starting_zone_encounters.json
│   │       └── encounter_tables.json
│   │
│   ├── templates/
│   │   ├── ai_prompts/
│   │   │   ├── npc_generation.json
│   │   │   ├── quest_generation.json
│   │   │   ├── encounter_generation.json
│   │   │   ├── dialogue_generation.json
│   │   │   └── event_generation.json
│   │   │
│   │   └── content_schemas/
│   │       ├── npc_schema.json
│   │       ├── quest_schema.json
│   │       ├── location_schema.json
│   │       └── event_schema.json
│   │
│   ├── validation_rules/
│   │   ├── stat_ranges.json
│   │   ├── item_requirements.json
│   │   ├── skill_prerequisites.json
│   │   ├── lore_constraints.json
│   │   └── balance_limits.json
│   │
│   ├── lore/
│   │   ├── world_bible.json
│   │   ├── xanthria_lore.json
│   │   ├── factions/
│   │   │   ├── mage_guild.json
│   │   │   ├── spy_covenant.json
│   │   │   └── druid_circle.json
│   │   ├── pantheon/
│   │   │   ├── xanthria.json
│   │   │   └── lesser_gods.json
│   │   └── history/
│   │       └── world_timeline.json
│   │
│   └── balance/
│       ├── stat_scaling.json
│       ├── damage_formulas.json
│       ├── experience_curves.json
│       └── economy_settings.json
│
├── assets/
│   ├── fonts/
│   │   ├── main_font.ttf
│   │   ├── title_font.ttf
│   │   └── ui_font.ttf
│   │
│   ├── images/
│   │   ├── ui/
│   │   │   ├── buttons/
│   │   │   ├── panels/
│   │   │   ├── borders/
│   │   │   └── icons/
│   │   ├── portraits/
│   │   │   ├── player/
│   │   │   ├── npcs/
│   │   │   └── enemies/
│   │   ├── backgrounds/
│   │   │   ├── locations/
│   │   │   ├── combat/
│   │   │   └── menus/
│   │   └── effects/
│   │       ├── status/
│   │       ├── skills/
│   │       └── particles/
│   │
│   ├── audio/
│   │   ├── music/
│   │   │   ├── title_theme.ogg
│   │   │   ├── exploration_theme.ogg
│   │   │   └── combat_theme.ogg
│   │   └── sfx/
│   │       ├── ui/
│   │       ├── combat/
│   │       └── ambient/
│   │
│   └── manifest.json
│
├── saves/
│   └── .gitkeep
│
├── logs/
│   ├── game_logs/
│   │   └── .gitkeep
│   ├── error_logs/
│   │   └── .gitkeep
│   └── validation_logs/
│       └── .gitkeep
│
├── tests/
│   ├── __init__.py
│   ├── test_combat_system.py
│   ├── test_state_manager.py
│   ├── test_event_manager.py
│   ├── test_entity_factory.py
│   ├── test_dialogue_system.py
│   ├── test_progression_system.py
│   ├── test_save_manager.py
│   └── test_validators/
│       ├── __init__.py
│       ├── test_ai_validators.py
│       ├── test_data_validators.py
│       └── test_game_validators.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── LICENSE

## 🚀 Current Version: 0.0.1 - Initial Setup
**Release Date:** [Add date when you commit this]
### What's Included:
- ✅ Complete folder structure established
- ✅ Professional OOP-oriented architecture planned
- ✅ Core design documents created
- ✅ Repository initialized with README and .gitignore
### What's NOT Included (Yet):
- ❌ No executable code
- ❌ No game loop or state management
- ❌ No assets or data files
- ❌ No playable features
**This is purely a structural foundation.**
## 🛠️ Technology Stack
- **Language:** Python 3.x
- **Game Engine:** Pygame
- **AI Integration:** [TBD - will be determined during development]
- **Data Format:** JSON for all game content
- **Version Control:** Git/GitHub
## 🎯 Development Roadmap
### Phase 1: Core Foundation (Current)
- [x] Project structure
- [ ] Base classes and interfaces
- [ ] State manager implementation
- [ ] Event bus system
- [ ] Resource manager
- [ ] Basic UI widgets
### Phase 2: Character Creation
- [ ] Race and class selection
- [ ] Starting location choice
- [ ] Character sheet display
- [ ] Data-driven character creation
### Phase 3: Combat System
- [ ] Turn-based combat engine
- [ ] Action system (attack, skill, item, defend, flee)
- [ ] Status effects
- [ ] Damage calculation
- [ ] Enemy AI behaviors
### Phase 4: World & Exploration
- [ ] Location system
- [ ] Handcrafted starting zone
- [ ] Basic NPC interactions
- [ ] Scripted dialogue system
### Phase 5: Progression Systems
- [ ] Experience and leveling
- [ ] Skill trees
- [ ] Inventory and equipment
- [ ] Save/load functionality
### Phase 6: AI Integration
- [ ] AI manager setup
- [ ] Dynamic NPC generation
- [ ] Emergent quest creation
- [ ] AI-driven dialogue
- [ ] World event generation
### Phase 7: Polish & Balance
- [ ] UI/UX improvements
- [ ] Audio integration
- [ ] Game balance tuning
- [ ] Bug fixes and optimization
## 📋 Prerequisites
```bash
Python 3.8 or higher
Pygame 2.x
[Additional dependencies will be added to requirements.txt]

---
"All of this is purposefully included for my own personal education/reminders/workflow so that I can remember how to maintain and update this."
---

🔧 Installation
# Clone the repository
git clone [your-repo-url]
# Navigate to project directory
cd rpg_project
# Install dependencies (when available)
pip install -r requirements.txt
# Run the game (when implemented)
python src/main.py

📖 Documentation
Detailed design documents can be found in the /docs folder:

design/world_bible.md - Complete world lore and setting
design/game_systems.md - Core gameplay mechanics
technical/architecture.md - System architecture details
technical/state_contracts.md - State management contracts
🤝 Contributing
This is a personal learning project and is not currently accepting contributions. However, feel free to fork it for your own learning purposes!

📝 License
[Choose your license - MIT, GPL, etc.]

🙏 Acknowledgments
AI mentorship for teaching me professional game development practices
The Pygame community for excellent documentation
Classic JRPGs (Final Fantasy series) for combat inspiration
Version History
v0.0.1 - Initial Setup (YYYY-MM-DD)
Created project structure
Established folder hierarchy
Initialized repository
Added documentation framework
Note: This project is in very early development. Check back regularly for updates!

---
## 📝 How to Maintain This README
### When You Complete a Task:
1. **Find the task in the roadmap** (under `🎯 Development Roadmap`)
2. **Change `[ ]` to `[x]`** to mark it complete
3. **Update the "Current Version" section** if you're ready to bump versions
### When You Add a New Version:
1. **Update the version number** at the top (e.g., `0.0.1` → `0.1.0`)
2. **Update the release date**
3. **Update "What's Included" and "What's NOT Included"**
4. **Add a new entry** to "Version History" at the bottom
### Version Numbering Guide:
- **0.0.x** - Setup and planning (no playable code)
- **0.x.0** - Major system implementations (e.g., 0.1.0 = state manager working)
- **0.x.y** - Minor updates and bug fixes (e.g., 0.1.1 = fixed state manager bug)
- **1.0.0** - First fully playable version with all core features
### Quick Update Template:
```markdown
### v0.1.0 - [Feature Name] (YYYY-MM-DD)
- Added [feature 1]
- Implemented [feature 2]
- Fixed [bug]
- Updated [system]

What to Update When:
Every commit: Nothing! (Unless it's a milestone)
Every milestone: Version number, version history, roadmap checkboxes
New dependencies: Update prerequisites and installation sections
Major changes: Update project structure if folders change
Documentation added: Update documentation section
Keep it simple—only update when you hit meaningful milestones, not every single commit!

