# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-12-01
### Milestone: Core Engine & Title Screen
The first official pre-alpha release of the UnRPG engine. This release establishes the foundational architecture and the initial user interface.

### Added
- **Core Architecture**
    - Implemented `GameLoop` for managing the main application cycle.
    - Created `EventManager` for decoupled, event-driven communication.
    - Established `SceneManager` and abstract `Scene` base class for state management.
- **User Interface**
    - Developed `TitleScreen` with dynamic background scaling.
    - Implemented reusable `Button` class with hover states and callback support.
    - Added `MouseClickEvent` handling for UI interaction.
- **Configuration**
    - Centralized `config.py` for managing resolution, colors, and assets.
