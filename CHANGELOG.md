# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Nothing yet

## [0.1.0] - 2025-11-01

### Added

- Initial release with C++ and Rust support
- Interactive CLI with menu system (`learn`)
- First-time setup wizard (`learn init`)
- System verification tool (`learn doctor`)
- Workspace scaffolding with language-specific templates
- Vim mode with stable split-screen (nvim -O)
- VS Code and terminal modes
- Compile and run integration (`learn --run`)
- Progress tracking system
- Interactive tutorial (option 8 in menu)
- 70+ lessons across 5 stages for C++ and Rust

### Features

- **CLI Commands**:
  - `learn` - Interactive menu
  - `learn init` - Setup wizard
  - `learn doctor` - System check
  - `learn c++ 1` - Open lesson
  - `learn --run c++ 1 1` - Compile and run
  - `learn --list` - Browse lessons
  - `learn --progress` - View progress
  - `learn --next` - Next lesson suggestion

- **Workspace Scaffolding**:
  - C++: main.cpp, Makefile, .clang-format
  - Rust: main.rs, Cargo.toml
  - Python: main.py with structure
  - JavaScript: main.js, package.json

- **Vim Integration**:
  - Split-screen: lesson (left) + code (right)
  - Full LazyVim/Kickstart support
  - LSP autocomplete and diagnostics
  - Auto-formatting on save
  - Quick compile commands (`:!make run`, `:!cargo run`)

### Fixed

- Stable Neovim launch without decoration crashes
- Idempotent install.sh with robust shell detection
- Professional error messages without emojis

### Documentation

- README.md with quick start
- START_HERE.md for 5-minute onboarding
- INSTRUCTIONS.md for AI agents and maintainers
- CLI feature documentation in CLI/FEATURES.md
- Setup guides for development environment

[unreleased]: https://github.com/YOUR_ORG/learn/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/YOUR_ORG/learn/releases/tag/v0.1.0
