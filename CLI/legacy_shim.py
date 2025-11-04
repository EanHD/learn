"""
Legacy compatibility shim
Translates old command patterns to modern subcommands
"""

def translate_legacy_argv(argv):
    """
    Translate legacy invocations to modern subcommands.

    Legacy patterns supported:
      learn                      -> interactive menu
      learn --list               -> list
      learn --progress           -> progress
      learn --next               -> next
      learn python 1 --stage 2   -> open python 2 1
      learn --run python 1 1     -> run python 1 1
      learn --complete c++ 1 1   -> complete c++ 1 1
      learn --doctor             -> doctor
      learn --init               -> init
      --vim / --vscode / --terminal -> editor mode flags
    """

    if len(argv) == 1:  # no args -> interactive
        return argv

    # Check if already using modern subcommands
    MODERN_CMDS = {"init", "doctor", "list", "browse", "tip", "next", "progress", "open", "run", "complete", "config"}
    if len(argv) > 1 and argv[1] in MODERN_CMDS:
        return argv

    out = [argv[0]]
    args = argv[1:]

    # Simple flag translations
    if "--list" in args:
        return out + ["list"]
    if "--progress" in args:
        return out + ["progress"]
    if "--next" in args:
        return out + ["next"]
    if "--doctor" in args:
        return out + ["doctor"]
    if "--init" in args:
        return out + ["init"]
    if "--interactive" in args or "-i" in args:
        return out  # Just run without subcommand -> interactive

    # --complete LANG STAGE LEVEL
    if "--complete" in args:
        i = args.index("--complete")
        if len(args) > i + 3:
            lang = args[i + 1]
            stage = args[i + 2]
            level = args[i + 3]
            return out + ["complete", lang, stage, level]

    # --run LANG STAGE LEVEL
    if "--run" in args:
        i = args.index("--run")
        if len(args) > i + 3:
            lang = args[i + 1]
            stage = args[i + 2]
            level = args[i + 3]
            return out + ["run", lang, stage, level]

    # Detect editor mode flags
    mode = None
    if "--vim" in args:
        mode = "vim"
    elif "--vscode" in args:
        mode = "vscode"
    elif "--terminal" in args:
        mode = "terminal"

    # Legacy positional open: learn <lang> <level> [--stage N]
    if len(args) >= 2 and not args[0].startswith("-"):
        lang = args[0]
        level = args[1]
        stage = "1"

        if "--stage" in args:
            j = args.index("--stage")
            if len(args) > j + 1:
                stage = str(args[j + 1])

        cmd = ["open", lang, stage, level]
        if mode:
            cmd.append("--" + mode)

        return out + cmd

    # Default: pass through (modern parser will handle/error nicely)
    return argv


def show_legacy_notice_once():
    """Show a gentle deprecation notice for legacy flag usage (optional)"""
    import os
    from pathlib import Path

    # Check if notice has been shown
    try:
        config_dir = Path.home() / ".config" / "learn"
        notice_file = config_dir / ".legacy_notice_shown"

        if notice_file.exists():
            return  # Already shown

        print("ℹ️  Legacy flags detected; using unified CLI.")
        print("   Try the new syntax: learn open python 1 1")
        print()

        # Mark as shown
        config_dir.mkdir(parents=True, exist_ok=True)
        notice_file.touch()
    except Exception:
        pass  # Silently fail if we can't create the file
