# Modular Architecture Plan

## Vision
Transform LEARN from "Neovim + lessons" into a fully-integrated learning platform with its own identity, extensible plugin system, and seamless editor experience.

---

## Core Principles

1. **Separation of Concerns**: Core (lessons) vs Features (achievements, validations, etc.)
2. **Plugin Architecture**: Modular features that can be enabled/disabled
3. **Event-Driven**: Hook system for plugins to respond to user actions
4. **Progressive Enhancement**: Features don't break core functionality
5. **Cross-Platform**: Work consistently on Windows, macOS, Linux

---

## Proposed Architecture

```
LEARN/
├── core/                      # Core lesson system (minimal, stable)
│   ├── lessons/              # Lesson content (unchanged)
│   ├── cli/                  # Basic CLI interface
│   └── editor/               # Neovim configuration (base)
│
├── plugins/                   # Modular feature system
│   ├── achievements/         # Achievement tracking
│   ├── validation/           # LLM code validation
│   ├── difficulty/           # Easy/hard mode system
│   ├── locking/              # Level lock/unlock system
│   ├── analytics/            # Progress analytics
│   └── hints/                # Dynamic hint system
│
├── editor/                    # Custom editor wrapper
│   ├── learn-nvim/           # Branded Neovim wrapper
│   ├── ui/                   # Custom UI components
│   └── themes/               # LEARN-specific themes
│
└── api/                       # Plugin API layer
    ├── events.py             # Event bus system
    ├── hooks.lua             # Vim hook system
    └── plugins.py            # Plugin manager
```

---

## Event System Design

### Core Events

Events that plugins can hook into:

```python
# events.py

class EventType:
    # Lesson lifecycle
    LESSON_OPENED = "lesson.opened"
    LESSON_CLOSED = "lesson.closed"
    LESSON_COMPLETED = "lesson.completed"
    
    # Code execution
    CODE_RUNNING = "code.running"
    CODE_SUCCESS = "code.success"
    CODE_FAILURE = "code.failure"
    
    # Navigation
    LESSON_NEXT = "lesson.next"
    LESSON_PREVIOUS = "lesson.previous"
    STAGE_CHANGED = "stage.changed"
    
    # User actions
    USER_HINT_REQUESTED = "user.hint_requested"
    USER_SOLUTION_VIEWED = "user.solution_viewed"
    
    # Progress
    STAGE_COMPLETED = "stage.completed"
    LANGUAGE_COMPLETED = "language.completed"
```

### Plugin Registration

```python
# Example: achievements plugin

from api.events import EventBus, EventType

class AchievementsPlugin:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.register_handlers()
    
    def register_handlers(self):
        self.event_bus.on(EventType.CODE_SUCCESS, self.on_code_success)
        self.event_bus.on(EventType.STAGE_COMPLETED, self.on_stage_complete)
    
    def on_code_success(self, data):
        # Check for "First Success" achievement
        if self.is_first_success():
            self.unlock_achievement("first_success")
    
    def on_stage_complete(self, data):
        # Check for "Stage Master" achievement
        self.unlock_achievement(f"stage_{data['stage']}_master")
```

---

## Plugin System

### Plugin Structure

```
plugins/achievements/
├── __init__.py           # Plugin entry point
├── config.yaml           # Plugin configuration
├── achievements.json     # Achievement definitions
├── handlers.py           # Event handlers
└── ui.lua                # Vim UI components (optional)
```

### Plugin Configuration (config.yaml)

```yaml
name: "Achievements"
version: "1.0.0"
author: "LEARN Team"
description: "Track progress with unlockable achievements"

dependencies:
  - core: ">=1.0.0"

settings:
  enabled: true
  show_notifications: true
  celebration_effects: true

events:
  - lesson.completed
  - code.success
  - stage.completed
```

### Plugin Manager

```python
# api/plugins.py

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.event_bus = EventBus()
    
    def load_plugin(self, plugin_dir: Path):
        """Load a plugin from directory"""
        config = self.read_config(plugin_dir / "config.yaml")
        
        if not config["settings"]["enabled"]:
            return
        
        plugin_module = import_module(f"plugins.{plugin_dir.name}")
        plugin_class = plugin_module.Plugin
        
        plugin_instance = plugin_class(self.event_bus)
        self.plugins[config["name"]] = plugin_instance
    
    def emit_event(self, event_type: str, data: dict):
        """Emit event to all plugins"""
        self.event_bus.emit(event_type, data)
```

---

## Feature Implementation Roadmap

### Phase 1: Foundation (Current → Next Release)
**Goal**: Establish plugin architecture without breaking existing functionality

- [ ] Create `api/events.py` with EventBus class
- [ ] Create `api/plugins.py` with PluginManager
- [ ] Refactor existing progress tracking to use events
- [ ] Add Lua hook system in `api/hooks.lua`
- [ ] Document plugin API

**Deliverables**:
- Working event system
- Plugin loading mechanism
- Example "hello world" plugin
- Developer documentation

---

### Phase 2: Core Plugins (2-3 weeks)
**Goal**: Implement high-value features as plugins

#### 2.1: Achievements Plugin
```
plugins/achievements/
├── achievements.json      # All achievement definitions
├── tracker.py            # Progress tracking logic
└── notifications.lua     # Vim notifications

Example achievements:
- "Hello World": Complete first lesson
- "Bug Squasher": Fix 10 errors
- "Night Owl": Code at midnight
- "Perfectionist": 10 lessons without errors
- "Speed Demon": Complete lesson in < 5 minutes
```

#### 2.2: Validation Plugin
```
plugins/validation/
├── llm_validator.py      # LLM-based code validation
├── test_runner.py        # Automated test execution
└── feedback.py           # Structured feedback generation

Features:
- Call OpenAI/Anthropic API with code + requirements
- Generate feedback on approach, style, correctness
- Suggest improvements without giving solutions
- Support offline mode (fallback to simple checks)
```

#### 2.3: Difficulty Plugin
```
plugins/difficulty/
├── modes.py              # Easy/Normal/Hard implementations
├── guidance.py           # Context-aware hints
└── scaffolding.py        # Auto-generated starter code

Modes:
- Easy: More hints, starter code, frequent checkpoints
- Normal: Current experience
- Hard: Minimal guidance, challenge problems, time pressure
```

---

### Phase 3: Enhanced Editor (4-6 weeks)
**Goal**: Make Neovim feel like LEARN's integrated editor

#### 3.1: Custom Branding
```
editor/learn-nvim/
├── splash.lua            # Custom startup screen
├── statusline.lua        # LEARN-branded status line
├── theme.lua             # Signature LEARN theme
└── dashboard.lua         # Progress dashboard (startup)

Features:
- Custom `:Learn` commands (`:LearnNext`, `:LearnProgress`)
- Branded color scheme (cyber minimal aesthetic)
- Dashboard showing progress, achievements, streaks
- Integration with CLI state
```

#### 3.2: Enhanced UI Components
```
editor/ui/
├── lesson_preview.lua    # Hoverable lesson preview
├── hint_panel.lua        # Collapsible hint sidebar
├── progress_bar.lua      # Visual progress indicator
└── solution_compare.lua  # Side-by-side solution comparison

Features:
- Floating window for quick hints
- Progress bar in lesson window
- Inline syntax highlighting for explanations
- Diff view between user solution and reference
```

---

### Phase 4: Level Locking (2-3 weeks)
**Goal**: Progressive unlocking system

#### 4.1: Lock System Plugin
```
plugins/locking/
├── lock_manager.py       # Tracks locked/unlocked lessons
├── requirements.py       # Unlock requirements (complete previous, pass quiz)
├── ui.lua                # Visual locked indicators

Features:
- Lessons locked until prerequisites met
- Optional "skip lock" for testing
- Visual indicators (🔒/🔓) in CLI and Vim
- Configurable unlock conditions
```

#### 4.2: Prerequisites System
```yaml
# Example: lesson prerequisites
c-c++/stage-2/level-1:
  requires:
    - c-c++/stage-1/level-7: complete
  
c-c++/stage-3/level-1:
  requires:
    - c-c++/stage-2/level-7: complete
    - quiz: "c-c++/stage-2/quiz"
```

---

### Phase 5: Executables & Distribution (4-6 weeks)
**Goal**: Easy installation and distribution

#### 5.1: Packaging
```
packaging/
├── windows/
│   ├── installer.nsi      # NSIS installer script
│   ├── bundle.ps1         # PowerShell bundling script
│   └── learn.exe          # Compiled executable
├── macos/
│   ├── learn.app          # macOS application bundle
│   └── dmg_builder.sh     # DMG creation script
└── linux/
    ├── learn.AppImage     # Universal Linux package
    ├── deb/               # Debian package
    └── rpm/               # RPM package

Tools:
- PyInstaller for Python CLI → executable
- Neovim AppImage bundled
- Self-contained runtime environments
```

#### 5.2: Distribution Channels
- **Windows**: Winget, Chocolatey, direct download
- **macOS**: Homebrew cask, direct DMG
- **Linux**: apt repository, Snap, Flatpak, AppImage

---

## Technical Decisions

### 1. Plugin Language Choice
**Decision**: Python for logic, Lua for UI
**Rationale**:
- CLI already in Python (consistency)
- Lua native to Neovim (performance, integration)
- Python for complex logic (LLM API calls, analytics)
- Lua for editor interactions (keybindings, UI)

### 2. State Management
**Decision**: SQLite database + JSON for simple data
**Rationale**:
- SQLite for complex queries (analytics, achievements)
- JSON for simple data (progress, settings)
- Easy to backup/restore
- Works offline

### 3. Configuration Format
**Decision**: YAML for plugins, JSON for data
**Rationale**:
- YAML human-readable (good for config)
- JSON machine-friendly (good for data)
- Both widely supported

### 4. LLM Integration
**Decision**: Optional, with local fallback
**Rationale**:
- Not everyone has API keys
- Privacy concerns (some users won't want to send code)
- Expensive for heavy usage
- Provide simple rule-based validation as fallback

---

## Migration Strategy

### Backward Compatibility
1. Existing lessons work without changes
2. Current CLI commands continue to work
3. Progress data preserved
4. Opt-in plugin system (disabled by default initially)

### Gradual Rollout
1. **v1.1**: Event system (behind the scenes, no user-facing changes)
2. **v1.2**: First plugin (achievements, opt-in beta)
3. **v1.3**: Editor enhancements, custom branding
4. **v1.4**: Validation plugin, difficulty modes
5. **v2.0**: Full plugin ecosystem, executables

---

## User-Facing Changes

### Settings File
```yaml
# ~/.config/learn/settings.yaml

plugins:
  achievements:
    enabled: true
    show_notifications: true
  
  validation:
    enabled: false  # Requires API key
    provider: "openai"
    api_key: "sk-..."
  
  difficulty:
    default_mode: "normal"
  
  locking:
    enabled: false  # For power users who want full access

editor:
  theme: "cyber-minimal"
  auto_save: true
  show_progress_bar: true
```

### New CLI Commands
```bash
learn plugins list                    # List available plugins
learn plugins enable achievements     # Enable plugin
learn plugins disable locking         # Disable plugin

learn config set editor.theme cyber   # Change theme
learn config get                      # Show all settings

learn achievements list               # Show achievements
learn stats                           # Show detailed analytics
```

---

## API Documentation (for Plugin Developers)

### Creating a Plugin

```python
# plugins/my_plugin/__init__.py

from api.events import EventBus, EventType

class Plugin:
    """Every plugin must have a 'Plugin' class"""
    
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.name = "My Plugin"
        self.register()
    
    def register(self):
        """Register event handlers"""
        self.event_bus.on(EventType.LESSON_OPENED, self.on_lesson_open)
    
    def on_lesson_open(self, data):
        """Handle lesson open event"""
        print(f"Lesson opened: {data['language']} Stage {data['stage']} Level {data['level']}")
```

### Available Events

Full documentation in `api/EVENTS.md`:
- Event types
- Data structures
- Example handlers
- Best practices

---

## Performance Considerations

1. **Lazy Loading**: Plugins loaded only when needed
2. **Event Debouncing**: Prevent excessive event firing
3. **Async Operations**: LLM calls don't block editor
4. **Caching**: Cache validation results, achievements state
5. **Opt-Out**: Heavy plugins disabled by default

---

## Security Considerations

1. **Plugin Sandboxing**: Plugins can't access arbitrary files
2. **API Key Storage**: Encrypted local storage for LLM keys
3. **Code Validation**: Validate plugin code before loading
4. **Permission System**: Plugins declare required permissions

---

## Testing Strategy

1. **Unit Tests**: Each plugin independently tested
2. **Integration Tests**: Event system with multiple plugins
3. **E2E Tests**: Full user workflows
4. **Cross-Platform**: Test on Windows, macOS, Linux
5. **Performance**: Monitor event processing overhead

---

## Documentation Plan

### For Users
- `PLUGINS.md`: How to enable/disable plugins
- `ACHIEVEMENTS.md`: List of all achievements
- `SETTINGS.md`: All configuration options

### For Developers
- `PLUGIN_API.md`: How to create plugins
- `EVENTS.md`: Event system reference
- `EXAMPLES/`: Example plugins with detailed comments

---

## Timeline Estimate

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Phase 1: Foundation | 1-2 weeks | Working event system |
| Phase 2: Core Plugins | 2-3 weeks | Achievements + Validation |
| Phase 3: Enhanced Editor | 4-6 weeks | Branded experience |
| Phase 4: Level Locking | 2-3 weeks | Progressive system |
| Phase 5: Executables | 4-6 weeks | Packaged distribution |
| **TOTAL** | **13-20 weeks** | **Full ecosystem** |

---

## Open Questions

1. **Plugin Marketplace**: Should we have a plugin marketplace/registry?
2. **Cloud Sync**: Sync progress/achievements across devices?
3. **Social Features**: Leaderboards, compare progress with friends?
4. **Web Dashboard**: Companion web app for analytics?
5. **Mobile Companion**: Mobile app for reviewing lessons?

---

## Next Steps

1. Review and approve architecture
2. Create GitHub issues for Phase 1 tasks
3. Set up project board for tracking
4. Begin with event system implementation
5. Write plugin developer documentation

---

**Last Updated**: January 2025
**Status**: Proposal Draft
**Feedback**: Welcome via GitHub issues or discussions
