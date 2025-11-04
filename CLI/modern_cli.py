"""
Modernized Learn CLI with subcommands.
This module provides the new command-line interface with better structure.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

try:
    from . import languages
    from . import utils
    from . import config as cfg
except ImportError:
    # Fallback for direct execution
    import languages
    import utils
    import config as cfg


class ModernCLI:
    """Modernized CLI with subcommands"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.config = cfg.get_config()

    def create_parser(self) -> argparse.ArgumentParser:
        """Create argument parser with subcommands"""
        parser = argparse.ArgumentParser(
            prog="learn",
            description="🎓 LEARN — The all-in-one coding mentor",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  learn                    # Interactive menu (default)
  learn browse             # Browse languages by category
  learn browse --category web  # Explore web languages
  learn tip                # Get a random programming tip

  learn list               # List all available lessons
  learn next               # Get next recommended lesson
  learn progress           # View your progress

  learn open python 1 1    # Open Python Stage 1, Level 1
  learn open rust 2 3      # Open Rust Stage 2, Level 3
  learn open cpp 1 1 --vim # Open C++ Stage 1, Level 1 in Vim

  learn run python 1 1     # Run code for Python Stage 1, Level 1
  learn complete cpp 1 1   # Mark C++ Stage 1, Level 1 as complete

  learn doctor             # Check system dependencies
  learn init               # First-time setup wizard
  learn config --editor vim  # Set default editor

Legacy (still works, auto-translated):
  learn --list             # → list
  learn --progress         # → progress
  learn python 1 --stage 2 --vim  # → open python 2 1 --vim
  learn --run c++ 1 1      # → run c++ 1 1

For more help: learn <subcommand> --help
"""
        )

        # Global options
        parser.add_argument(
            "--version",
            action="version",
            version="Learn CLI v2.0.0"
        )

        # Create subcommands
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Subcommand: init
        init_parser = subparsers.add_parser(
            "init",
            help="Run first-time setup wizard",
            description="Interactive setup to configure your learning environment"
        )

        # Subcommand: doctor
        doctor_parser = subparsers.add_parser(
            "doctor",
            help="Check system dependencies",
            description="Verify compilers, interpreters, and tools are installed"
        )
        doctor_parser.add_argument(
            "--fix",
            action="store_true",
            help="Show install commands (doesn't auto-install)"
        )
        doctor_parser.add_argument(
            "--language",
            help="Check specific language only"
        )

        # Subcommand: list
        list_parser = subparsers.add_parser(
            "list",
            help="List all available lessons",
            description="Show all lessons across all languages and stages"
        )
        list_parser.add_argument(
            "--language",
            help="Filter by language"
        )
        list_parser.add_argument(
            "--stage",
            type=int,
            help="Filter by stage (1-5)"
        )

        # Subcommand: browse (NEW - Category browser)
        browse_parser = subparsers.add_parser(
            "browse",
            help="Browse languages by category",
            description="Explore programming languages organized by purpose and use case"
        )
        browse_parser.add_argument(
            "--category",
            help="Jump directly to a category (core, web, mobile, data, scripting, enterprise)"
        )
        browse_parser.add_argument(
            "--guided",
            action="store_true",
            help="Enable guided mode with extra tips and context"
        )

        # Subcommand: tips (NEW - Show random tips)
        tips_parser = subparsers.add_parser(
            "tip",
            help="Get a random programming tip or fact",
            description="Learn something interesting about programming"
        )

        # Subcommand: next
        next_parser = subparsers.add_parser(
            "next",
            help="Get next recommended lesson",
            description="Suggests next lesson based on your progress"
        )
        next_parser.add_argument(
            "--language",
            help="Get next lesson in specific language"
        )

        # Subcommand: progress
        progress_parser = subparsers.add_parser(
            "progress",
            help="View your progress",
            description="Show completion status across all languages"
        )
        progress_parser.add_argument(
            "--language",
            help="Show progress for specific language"
        )
        progress_parser.add_argument(
            "--export",
            metavar="FILE",
            help="Export progress to JSON file"
        )
        progress_parser.add_argument(
            "--reset",
            action="store_true",
            help="Reset all progress (requires confirmation)"
        )

        # Subcommand: open
        open_parser = subparsers.add_parser(
            "open",
            help="Open a lesson",
            description="Open lesson in your preferred editor",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  learn open python 1 1      # Python Stage 1, Level 1 (default editor)
  learn open rust 2 3        # Rust Stage 2, Level 3
  learn open cpp 1 1 --vim   # C++ Stage 1, Level 1 in Vim
  learn open js 5 4 --vscode # JavaScript Stage 5, Level 4 in VS Code
"""
        )
        open_parser.add_argument(
            "language",
            help="Language (python, rust, cpp, js, go, lua, dart, etc.)"
        )
        open_parser.add_argument(
            "stage",
            type=int,
            help="Stage number (1-5)"
        )
        open_parser.add_argument(
            "level",
            type=int,
            help="Level number (1-7)"
        )
        open_parser.add_argument(
            "--vim",
            action="store_true",
            help="Open in Vim/Neovim"
        )
        open_parser.add_argument(
            "--vscode",
            action="store_true",
            help="Open in VS Code"
        )
        open_parser.add_argument(
            "--terminal",
            action="store_true",
            help="Open in terminal (read-only)"
        )

        # Subcommand: run
        run_parser = subparsers.add_parser(
            "run",
            help="Compile and run code",
            description="Run code in a lesson workspace"
        )
        run_parser.add_argument("language", help="Language")
        run_parser.add_argument("stage", type=int, help="Stage (1-5)")
        run_parser.add_argument("level", type=int, help="Level (1-7)")

        # Subcommand: complete
        complete_parser = subparsers.add_parser(
            "complete",
            help="Mark lesson as complete",
            description="Update progress for a completed lesson"
        )
        complete_parser.add_argument("language", help="Language")
        complete_parser.add_argument("stage", type=int, help="Stage (1-5)")
        complete_parser.add_argument("level", type=int, help="Level (1-7)")

        # Subcommand: config
        config_parser = subparsers.add_parser(
            "config",
            help="Manage configuration",
            description="View or update CLI configuration"
        )
        config_parser.add_argument(
            "--editor",
            choices=["vim", "vscode", "terminal"],
            help="Set default editor"
        )
        config_parser.add_argument(
            "--language",
            help="Set default language"
        )
        config_parser.add_argument(
            "--show",
            action="store_true",
            help="Show current configuration"
        )
        config_parser.add_argument(
            "--reset",
            action="store_true",
            help="Reset to default configuration"
        )

        return parser

    def run(self, args: Optional[list] = None):
        """Run CLI with given arguments"""
        parser = self.create_parser()

        # If no arguments, show interactive menu
        if not args and len(sys.argv) == 1:
            self.run_interactive()
            return

        parsed = parser.parse_args(args)

        # Handle no subcommand (backwards compatibility)
        if not parsed.command:
            # Check if old-style positional args
            if hasattr(parsed, 'language') and parsed.language:
                self.handle_legacy_args(parsed)
            else:
                self.run_interactive()
            return

        # Route to command handlers
        command_map = {
            "init": self.cmd_init,
            "doctor": self.cmd_doctor,
            "browse": self.cmd_browse,
            "tip": self.cmd_tip,
            "list": self.cmd_list,
            "next": self.cmd_next,
            "progress": self.cmd_progress,
            "open": self.cmd_open,
            "run": self.cmd_run,
            "complete": self.cmd_complete,
            "config": self.cmd_config,
        }

        handler = command_map.get(parsed.command)
        if handler:
            try:
                handler(parsed)
            except KeyboardInterrupt:
                print("\n\nInterrupted by user")
                sys.exit(130)
            except Exception as e:
                print(f"Error: {e}")
                if "--debug" in sys.argv:
                    raise
                sys.exit(1)
        else:
            parser.print_help()

    def run_interactive(self):
        """Run interactive menu"""
        # Import the existing InteractiveCLI
        try:
            from .learn_cli import InteractiveCLI
        except ImportError:
            from learn_cli import InteractiveCLI
        cli = InteractiveCLI(self.learn_dir)
        cli.run_interactive_mode()

    def cmd_init(self, args):
        """Handle init command"""
        try:
            from .learn_cli import InitWizard
        except ImportError:
            from learn_cli import InitWizard
        wizard = InitWizard(self.learn_dir)
        wizard.run()

    def cmd_doctor(self, args):
        """Handle doctor command"""
        try:
            from .learn_cli import SystemChecker
        except ImportError:
            from learn_cli import SystemChecker
        checker = SystemChecker()

        if args.language:
            # Check specific language
            lang_config = languages.get_language(args.language)
            if not lang_config:
                print(f"Unknown language: {args.language}")
                return

            self._check_language(lang_config, show_fix=args.fix)
        else:
            # Check all
            checker.check_all()
            checker.print_report()

            if args.fix:
                print("\n" + "="*70)
                print("Install Commands by Platform:")
                print("="*70)
                self._print_install_commands()

    def cmd_browse(self, args):
        """Handle browse command - show categories"""
        try:
            from .categories import CategoryManager
        except ImportError:
            from categories import CategoryManager

        cat_mgr = CategoryManager(self.learn_dir)

        # If specific category requested, show it
        if args.category:
            category = cat_mgr.get_category(args.category)
            if not category:
                print(f"Unknown category: {args.category}")
                print(f"Available: {', '.join([c.id for c in cat_mgr.get_all_categories()])}")
                return
            self._display_category_detail(category, guided=args.guided)
        else:
            # Show category menu
            self._display_category_browser(cat_mgr, guided=args.guided)

    def _display_category_browser(self, cat_mgr, guided=False):
        """Display the interactive category browser"""
        if guided:
            print("\n🎯 Guided Tip:")
            print("If you're just starting out, begin with Python or JavaScript.")
            print("They'll teach you the thinking that transfers to C++ or Rust later.\n")

        cat_mgr.display_categories_menu()
        print("\nEnter a category number to explore →")
        print("Or use: learn browse --category <id>")
        print("Example: learn browse --category web\n")

    def _display_category_detail(self, category, guided=False):
        """Display detailed view of a category"""
        print(f"\n{category.emoji} {category.title.upper()}")
        print("=" * 60)
        print(f"{category.description}\n")

        if guided:
            print("💡 About this category:")
            if category.id == "core":
                print("These languages teach you how computers work at a fundamental level.")
                print("Start here if you want deep understanding and performance.\n")
            elif category.id == "web":
                print("These are the most beginner-friendly and have huge ecosystems.")
                print("Start here if you want to build things quickly.\n")
            elif category.id == "mobile":
                print("These are specialized for mobile app development.")
                print("Start here if your goal is iOS/Android apps.\n")

        for i, lang_name in enumerate(category.languages, 1):
            if lang_name in category.language_details:
                info = category.language_details[lang_name]
                print(f"\n{i}. {info.display_name}")
                print(f"   {info.summary}")

                print(f"\n   📚 Learning Resources:")
                for read in info.reads[:2]:  # Show first 2
                    print(f"      • {read}")

                print(f"\n   💡 Tips:")
                for tip in info.tips[:2]:  # Show first 2
                    print(f"      • {tip}")

                print(f"\n   🔧 Tools:")
                for tool in info.tools:
                    print(f"      • {tool}")

                print(f"\n   ▶️  Start learning: learn open {lang_name} 1 1")
                print()

        print("=" * 60)

    def cmd_tip(self, args):
        """Handle tip command - show random tip"""
        try:
            from .categories import CategoryManager
        except ImportError:
            from categories import CategoryManager

        cat_mgr = CategoryManager(self.learn_dir)
        tip = cat_mgr.get_random_tip()
        print(f"\n{tip}\n")

    def cmd_list(self, args):
        """Handle list command"""
        try:
            from .learn_cli import LessonManager
        except ImportError:
            from learn_cli import LessonManager

        lesson_mgr = LessonManager(self.learn_dir)

        if args.language:
            # Filter by language
            lang_config = languages.get_language(args.language)
            if not lang_config:
                print(f"Unknown language: {args.language}")
                return
            # Show lessons for that language
            print(f"\nLessons for {lang_config.display_name}:")
            lessons = lesson_mgr.list_all_lessons()
            if lang_config.name in lessons:
                for stage, levels in lessons[lang_config.name].items():
                    print(f"  {stage}: Levels {', '.join(map(str, levels))}")
        else:
            # Show all lessons
            lessons = lesson_mgr.list_all_lessons()
            print("\n📚 ALL AVAILABLE LESSONS\n")
            for lang_name, stages in lessons.items():
                lang_display = lang_name.replace("-", "/").title()
                print(f"\n{lang_display}")
                print("="*70)
                for stage, levels in stages.items():
                    print(f"  {stage}: Levels {', '.join(map(str, levels))}")
            print(f"\n\nTotal: {len(lessons)} languages × 5 stages × 7 levels = 490 lessons")

    def cmd_next(self, args):
        """Handle next command"""
        try:
            from .learn_cli import ProgressTracker
        except ImportError:
            from learn_cli import ProgressTracker

        progress = ProgressTracker(self.learn_dir)

        # Get next lesson for specified language or default
        lang = args.language if hasattr(args, 'language') and args.language else None

        if lang:
            lang_config = languages.get_language(lang)
            if not lang_config:
                print(f"Unknown language: {lang}")
                return
            next_lesson = progress.get_next_lesson(lang_config.name)
            if next_lesson:
                stage, level = next_lesson
                print(f"\n✨ Next lesson: {lang_config.display_name} - Stage {stage}, Level {level}")
            else:
                print(f"🎉 All lessons complete for {lang_config.display_name}!")
        else:
            # Find first incomplete lesson across all languages
            print("\n✨ Suggested next lesson:")
            print("\nRun: learn open <language> <level> <stage>")
            print("Example: learn open python 1 1")

    def cmd_progress(self, args):
        """Handle progress command"""
        try:
            from .learn_cli import ProgressTracker
        except ImportError:
            from learn_cli import ProgressTracker

        progress = ProgressTracker(self.learn_dir)

        if args.export:
            # Export progress to JSON file
            import json
            with open(args.export, 'w') as f:
                json.dump(progress.data, f, indent=2)
            print(f"✓ Progress exported to: {args.export}")
        elif args.reset:
            # Reset progress
            confirm = input("Are you sure you want to reset ALL progress? (yes/no): ")
            if confirm.lower() == "yes":
                progress.data = {}
                progress.save()
                print("✓ Progress reset successfully")
            else:
                print("Cancelled")
        else:
            # Show progress
            print("\n📊 LEARNING PROGRESS\n")
            if not progress.data.get("languages"):
                print("No lessons started yet. Start with: learn open python 1 1")
            else:
                for lang_name, stages in progress.data["languages"].items():
                    lang_display = lang_name.replace("-", "/").title()

                    # Count opened and completed lessons
                    opened = 0
                    completed = 0
                    for stage_key, levels in stages.items():
                        for level_key, level_data in levels.items():
                            opened += 1
                            if level_data.get("completed", False):
                                completed += 1

                    print(f"{lang_display}: {opened} opened, {completed} completed")
                    for stage_key in sorted(stages.keys()):
                        levels = stages[stage_key]
                        stage_num = stage_key.replace("stage_", "")
                        level_nums = [l.replace("level_", "") for l in sorted(levels.keys())]
                        print(f"  Stage {stage_num}: Levels {', '.join(level_nums)}")

                print(f"\n\nKeep learning! Run: learn next")

    def cmd_open(self, args):
        """Handle open command"""
        try:
            from .learn_cli import LessonManager, LessonExecutor, ProgressTracker
        except ImportError:
            from learn_cli import LessonManager, LessonExecutor, ProgressTracker

        # Get language config
        lang_config = languages.get_language(args.language)
        if not lang_config:
            print(f"Unknown language: {args.language}")
            print(f"Available: {', '.join(languages.get_all_language_names())}")
            return

        # Find lesson path
        lesson_mgr = LessonManager(self.learn_dir)
        lesson_path = lesson_mgr.find_lesson(lang_config.name, args.stage, args.level)

        if not lesson_path:
            print(f"\n❌ Lesson not found: {lang_config.display_name} Stage {args.stage}, Level {args.level}")
            return

        # Determine editor mode
        if args.vim:
            mode = "vim"
        elif args.vscode:
            mode = "vscode"
        elif args.terminal:
            mode = "terminal"
        else:
            mode = self.config.get("default_editor", "vim")

        # Mark lesson as opened
        progress = ProgressTracker(self.learn_dir)
        progress.mark_lesson_opened(lang_config.name, args.stage, args.level, mode)

        # Open lesson in appropriate mode
        executor = LessonExecutor(lesson_mgr)
        if mode == "vim":
            executor.open_vim(lesson_path, lang_config.name)
        elif mode == "vscode":
            executor.open_vscode(lesson_path, lang_config.name)
        elif mode == "terminal":
            executor.open_terminal(lesson_path)

    def cmd_run(self, args):
        """Handle run command"""
        import subprocess
        import os
        try:
            from .learn_cli import LessonExecutor
        except ImportError:
            from learn_cli import LessonExecutor

        lang_config = languages.get_language(args.language)
        if not lang_config:
            print(f"Unknown language: {args.language}")
            return

        # Find workspace
        executor = LessonExecutor(None)
        lang_short = executor._get_lang_short_name(lang_config.name)
        workspace_dir = executor.workspace_root / lang_short / f"stage-{args.stage}" / f"level-{args.level}"

        if not workspace_dir.exists():
            print(f"❌ Workspace not found: {workspace_dir}")
            print(f"Open the lesson first: learn open {args.language} {args.stage} {args.level}")
            return

        print(f"🚀 Running workspace: {workspace_dir}\n")

        # Run based on language
        if lang_config.name == "c-c++":
            os.chdir(workspace_dir)
            print("Compiling...")
            result = subprocess.run(["make"], capture_output=False)
            if result.returncode == 0:
                print("\nRunning...")
                subprocess.run(["./main"])
        elif lang_config.name == "rust":
            os.chdir(workspace_dir)
            subprocess.run(["cargo", "run"])
        elif lang_config.name == "python":
            main_file = workspace_dir / "main.py"
            subprocess.run(["python3", str(main_file)])
        elif lang_config.name == "javascript":
            main_file = workspace_dir / "main.js"
            subprocess.run(["node", str(main_file)])
        elif lang_config.name == "go":
            os.chdir(workspace_dir)
            subprocess.run(["go", "run", "."])
        else:
            print(f"⚠ Run command not configured for {lang_config.display_name}")

    def cmd_complete(self, args):
        """Handle complete command"""
        try:
            from .learn_cli import ProgressTracker
        except ImportError:
            from learn_cli import ProgressTracker

        lang_config = languages.get_language(args.language)
        if not lang_config:
            print(f"Unknown language: {args.language}")
            return

        progress = ProgressTracker(self.learn_dir)
        success = progress.mark_lesson_completed(
            lang_config.name,
            args.stage,
            args.level
        )
        if success:
            print(f"✓ Marked {lang_config.display_name} Stage {args.stage}, Level {args.level} as complete")
        else:
            print(f"⚠ Lesson not found in progress. Open it first: learn open {args.language} {args.stage} {args.level}")

    def cmd_config(self, args):
        """Handle config command"""
        if args.show:
            print("Current Configuration:")
            print("="*50)
            for key, value in self.config.config.to_dict().items():
                print(f"  {key}: {value}")
            print(f"\nConfig file: {self.config.config_file}")
            print(f"\nTo change settings:")
            print("  learn config --editor vim|vscode|terminal")
            print("  learn config --language <language>")
        elif args.reset:
            confirm = input("Reset configuration to defaults? (yes/no): ")
            if confirm.lower() == "yes":
                self.config.reset()
                print(f"Configuration reset to defaults")
                print(f"Config file: {self.config.config_file}")
            else:
                print("Cancelled")
        elif args.editor:
            self.config.set("default_editor", args.editor)
            self.config.save()
            print(f"✓ Default editor set to: {args.editor}")
            print(f"  Config file: {self.config.config_file}")
        elif args.language:
            lang_config = languages.get_language(args.language)
            if lang_config:
                self.config.set("default_language", lang_config.name)
                self.config.save()
                print(f"✓ Default language set to: {lang_config.display_name}")
                print(f"  Config file: {self.config.config_file}")
            else:
                print(f"Unknown language: {args.language}")
                print(f"Available: {', '.join(languages.get_all_language_names())}")
        else:
            print("Use --show to view configuration")
            print("Use --editor or --language to set options")

    def handle_legacy_args(self, args):
        """Handle old-style positional arguments for backwards compatibility"""
        # Convert old style to new style
        print("Note: Using legacy syntax. Try 'learn open' for new syntax.")

        # Map old arguments to open command
        self.cmd_open(args)

    def _check_language(self, lang_config: languages.LanguageConfig, show_fix: bool = False):
        """Check if a specific language is installed"""
        installed = utils.check_command(lang_config.compiler_check, "--version")

        status = "✓ OK" if installed else "✗ MISSING"
        print(f"{lang_config.display_name}: {status}")

        if not installed and show_fix:
            platform = utils.get_platform()
            install_cmd = lang_config.compiler_install.get(platform, "Not available")
            print(f"  Install: {install_cmd}")

    def _print_install_commands(self):
        """Print install commands for all languages"""
        platform = utils.get_platform()

        print(f"\nPlatform: {platform}")
        print("\nLanguage Dependencies:")
        print("-" * 70)

        for lang_name, lang_config in languages.LANGUAGES.items():
            install_cmd = lang_config.compiler_install.get(platform, "Not available")
            print(f"\n{lang_config.display_name}:")
            print(f"  {install_cmd}")


def main():
    """Entry point for modernized CLI"""
    learn_dir = Path(__file__).parent.parent
    cli = ModernCLI(learn_dir)
    cli.run()


if __name__ == "__main__":
    main()
