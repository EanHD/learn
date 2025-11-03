# Contributing to Learn

Thank you for your interest in contributing! This document provides guidelines for contributing to the Learn project.

## Getting Started

1. Fork and clone the repository
2. Install development dependencies:

```bash
pip install pre-commit ruff black
pre-commit install
```

3. Test your setup:

```bash
./CLI/learn --doctor
./CLI/learn --help
```

## Development Workflow

### Branching Strategy

- `main` - stable releases
- `develop` - integration branch
- `feature/*` - new features
- `fix/*` - bug fixes
- `docs/*` - documentation updates

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Python language support
fix: resolve workspace path issue
docs: update CLI usage examples
chore: update dependencies
test: add lesson autograder tests
```

### Code Style

- **Python**: Follow PEP 8, use `ruff` and `black`
- **Shell**: Use `shellcheck` and `shfmt`
- **Markdown**: Use `markdownlint`, no trailing whitespace
- **Line length**: 100 characters for code, unlimited for markdown

## Adding New Content

### Adding a Lesson

1. Create lesson directory: `<language>/stage-<N>/level-<M>/`
2. Add `lesson.md` with clear instructions
3. Add solution file template
4. Add test cases in `tests/` (optional)
5. Update language TOC

### Adding a New Language

Read `INSTRUCTIONS.md` for detailed guidance on:

- Directory structure requirements
- Lesson format specifications
- Metadata and configuration
- Integration with CLI

## Testing

### Manual Testing

```bash
# Test CLI features
./CLI/learn --doctor
./CLI/learn --init
./CLI/learn c++ 1

# Test workspace scaffolding
./CLI/learn --run c++ 1 1
```

### Automated Testing

```bash
# Run linters
pre-commit run --all-files

# Run CI locally (if using act)
act -j lint-and-test
```

## Pull Request Process

1. Ensure all tests pass and code is formatted
2. Update relevant documentation (README, docs/, CHANGELOG.md)
3. Add your changes to `CHANGELOG.md` under `[Unreleased]`
4. Fill out the PR template completely
5. Link any related issues
6. Request review from maintainers

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests added/updated (if applicable)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Commit messages follow Conventional Commits
- [ ] No merge conflicts

## Code Review Guidelines

Reviewers will check:

- Code quality and style
- Test coverage
- Documentation completeness
- Security considerations
- Performance impact
- Backwards compatibility

## Community

- **Issues**: Report bugs or request features
- **Discussions**: Ask questions and share ideas
- **Code of Conduct**: See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Recognition

Contributors are automatically added to the project's contributors list. Significant contributions
may be highlighted in release notes.

## Questions?

Open a [GitHub Discussion](https://github.com/YOUR_ORG/learn/discussions) or reach out to maintainers.

Thank you for contributing!
