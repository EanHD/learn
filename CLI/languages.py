"""
Language definitions for the Learn platform.
Centralizes all language-specific configuration.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class LanguageConfig:
    """Configuration for a programming language"""
    name: str
    display_name: str
    aliases: List[str]
    file_extension: str
    main_file: str
    solution_file: str
    run_command: List[str]
    compile_command: Optional[List[str]]
    vim_run_command: str
    help_comment: str
    compiler_check: str
    compiler_install: Dict[str, str]  # platform -> install command
    lsp_server: Optional[str] = None
    formatter: Optional[str] = None


# Language definitions
LANGUAGES: Dict[str, LanguageConfig] = {
    "c-c++": LanguageConfig(
        name="c-c++",
        display_name="C/C++",
        aliases=["cpp", "c++", "c"],
        file_extension="cpp",
        main_file="main.cpp",
        solution_file="solution.cpp",
        compile_command=["g++", "{file}", "-o", "main"],
        run_command=["./main"],
        vim_run_command="<Space>r or :!g++ % -o main && ./main",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="g++",
        compiler_install={
            "linux": "sudo apt install build-essential",
            "mac": "xcode-select --install",
            "windows": "Install MinGW or Visual Studio"
        },
        lsp_server="clangd",
        formatter="clang-format"
    ),

    "rust": LanguageConfig(
        name="rust",
        display_name="Rust",
        aliases=["rs"],
        file_extension="rs",
        main_file="main.rs",
        solution_file="solution.rs",
        compile_command=["rustc", "{file}", "-o", "main"],
        run_command=["./main"],
        vim_run_command="<Space>r or :!rustc % -o main && ./main",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="rustc",
        compiler_install={
            "linux": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "mac": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            "windows": "Download from https://rustup.rs"
        },
        lsp_server="rust-analyzer",
        formatter="rustfmt"
    ),

    "python": LanguageConfig(
        name="python",
        display_name="Python",
        aliases=["py"],
        file_extension="py",
        main_file="main.py",
        solution_file="solution.py",
        compile_command=None,
        run_command=["python3", "{file}"],
        vim_run_command="<Space>r or :!python3 %",
        help_comment="# Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="python3",
        compiler_install={
            "linux": "sudo apt install python3 python3-pip",
            "mac": "brew install python3",
            "windows": "Download from https://python.org"
        },
        lsp_server="pyright",
        formatter="black"
    ),

    "javascript": LanguageConfig(
        name="javascript",
        display_name="JavaScript",
        aliases=["js"],
        file_extension="js",
        main_file="main.js",
        solution_file="solution.js",
        compile_command=None,
        run_command=["node", "{file}"],
        vim_run_command="<Space>r or :!node %",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="node",
        compiler_install={
            "linux": "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs",
            "mac": "brew install node",
            "windows": "Download from https://nodejs.org"
        },
        lsp_server="typescript-language-server",
        formatter="prettier"
    ),

    "typescript": LanguageConfig(
        name="typescript",
        display_name="TypeScript",
        aliases=["ts"],
        file_extension="ts",
        main_file="main.ts",
        solution_file="solution.ts",
        compile_command=None,
        run_command=["ts-node", "{file}"],
        vim_run_command="<Space>r or :!ts-node %",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="ts-node",
        compiler_install={
            "linux": "npm install -g typescript ts-node",
            "mac": "npm install -g typescript ts-node",
            "windows": "npm install -g typescript ts-node"
        },
        lsp_server="typescript-language-server",
        formatter="prettier"
    ),

    "go": LanguageConfig(
        name="go",
        display_name="Go",
        aliases=[],
        file_extension="go",
        main_file="main.go",
        solution_file="solution.go",
        compile_command=None,
        run_command=["go", "run", "{file}"],
        vim_run_command="<Space>r or :!go run %",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="go",
        compiler_install={
            "linux": "sudo apt install golang",
            "mac": "brew install go",
            "windows": "Download from https://golang.org"
        },
        lsp_server="gopls",
        formatter="gofmt"
    ),

    "lua": LanguageConfig(
        name="lua",
        display_name="Lua",
        aliases=[],
        file_extension="lua",
        main_file="main.lua",
        solution_file="solution.lua",
        compile_command=None,
        run_command=["lua", "{file}"],
        vim_run_command="<Space>r or :!lua %",
        help_comment="-- Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="lua",
        compiler_install={
            "linux": "sudo apt install lua5.4",
            "mac": "brew install lua",
            "windows": "Download from https://luabinaries.sourceforge.net"
        },
        lsp_server="lua-language-server",
        formatter=None
    ),

    "dart": LanguageConfig(
        name="dart",
        display_name="Dart",
        aliases=[],
        file_extension="dart",
        main_file="main.dart",
        solution_file="solution.dart",
        compile_command=None,
        run_command=["dart", "{file}"],
        vim_run_command="<Space>r or :!dart %",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="dart",
        compiler_install={
            "linux": "sudo apt install dart",
            "mac": "brew tap dart-lang/dart && brew install dart",
            "windows": "choco install dart-sdk"
        },
        lsp_server="dart",
        formatter="dart format"
    ),

    "swift": LanguageConfig(
        name="swift",
        display_name="Swift",
        aliases=[],
        file_extension="swift",
        main_file="main.swift",
        solution_file="solution.swift",
        compile_command=None,
        run_command=["swift", "{file}"],
        vim_run_command="<Space>r or :!swift %",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="swift",
        compiler_install={
            "linux": "Download from https://swift.org/download",
            "mac": "xcode-select --install",
            "windows": "Download from https://swift.org/download"
        },
        lsp_server="sourcekit-lsp",
        formatter=None
    ),

    "kotlin": LanguageConfig(
        name="kotlin",
        display_name="Kotlin",
        aliases=["kt"],
        file_extension="kt",
        main_file="main.kt",
        solution_file="solution.kt",
        compile_command=["kotlinc", "{file}", "-include-runtime", "-d", "main.jar"],
        run_command=["java", "-jar", "main.jar"],
        vim_run_command="<Space>r or :!kotlinc % -include-runtime -d main.jar && java -jar main.jar",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="kotlinc",
        compiler_install={
            "linux": "sudo snap install --classic kotlin",
            "mac": "brew install kotlin",
            "windows": "choco install kotlinc"
        },
        lsp_server="kotlin-language-server",
        formatter="ktlint"
    ),

    "sql": LanguageConfig(
        name="sql",
        display_name="SQL",
        aliases=[],
        file_extension="sql",
        main_file="main.sql",
        solution_file="solution.sql",
        compile_command=None,
        run_command=["sqlite3"],
        vim_run_command="<Space>r or :!sqlite3 < %",
        help_comment="-- Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="sqlite3",
        compiler_install={
            "linux": "sudo apt install sqlite3",
            "mac": "brew install sqlite3",
            "windows": "choco install sqlite"
        },
        lsp_server="sqls",
        formatter=None
    ),

    "csharp": LanguageConfig(
        name="csharp",
        display_name="C#",
        aliases=["cs", "c#"],
        file_extension="cs",
        main_file="main.cs",
        solution_file="solution.cs",
        compile_command=["csc", "{file}"],
        run_command=["mono", "{file}.exe"],
        vim_run_command="<Space>r or :!csc % && mono %.exe",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="csc",
        compiler_install={
            "linux": "sudo apt install mono-complete",
            "mac": "brew install mono",
            "windows": "Install Visual Studio"
        },
        lsp_server="omnisharp",
        formatter=None
    ),

    "shell": LanguageConfig(
        name="shell",
        display_name="Shell",
        aliases=["bash", "sh"],
        file_extension="sh",
        main_file="main.sh",
        solution_file="solution.sh",
        compile_command=None,
        run_command=["bash", "{file}"],
        vim_run_command="<Space>r or :!bash %",
        help_comment="# Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="bash",
        compiler_install={
            "linux": "Pre-installed",
            "mac": "Pre-installed",
            "windows": "Install Git Bash or WSL"
        },
        lsp_server="bash-language-server",
        formatter="shfmt"
    ),

    "powershell": LanguageConfig(
        name="powershell",
        display_name="PowerShell",
        aliases=["ps1", "pwsh"],
        file_extension="ps1",
        main_file="main.ps1",
        solution_file="solution.ps1",
        compile_command=None,
        run_command=["powershell", "-File", "{file}"],
        vim_run_command="<Space>r or :!powershell -File %",
        help_comment="# Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="powershell",
        compiler_install={
            "linux": "sudo apt install powershell",
            "mac": "brew install powershell",
            "windows": "Pre-installed"
        },
        lsp_server="powershell-editor-services",
        formatter=None
    ),

    "java": LanguageConfig(
        name="java",
        display_name="Java",
        aliases=[],
        file_extension="java",
        main_file="Main.java",
        solution_file="Solution.java",
        compile_command=["javac", "{file}"],
        run_command=["java", "Main"],
        vim_run_command="<Space>r or :!javac % && java Main",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="javac",
        compiler_install={
            "linux": "sudo apt install default-jdk",
            "mac": "brew install openjdk",
            "windows": "Download from https://adoptium.net"
        },
        lsp_server="jdtls",
        formatter="google-java-format"
    ),

    "php": LanguageConfig(
        name="php",
        display_name="PHP",
        aliases=[],
        file_extension="php",
        main_file="main.php",
        solution_file="solution.php",
        compile_command=None,
        run_command=["php", "{file}"],
        vim_run_command="<Space>r or :!php %",
        help_comment="<?php\n// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="php",
        compiler_install={
            "linux": "sudo apt install php-cli",
            "mac": "brew install php",
            "windows": "Download from https://windows.php.net"
        },
        lsp_server="intelephense",
        formatter="php-cs-fixer"
    ),

    "r": LanguageConfig(
        name="r",
        display_name="R",
        aliases=[],
        file_extension="R",
        main_file="main.R",
        solution_file="solution.R",
        compile_command=None,
        run_command=["Rscript", "{file}"],
        vim_run_command="<Space>r or :!Rscript %",
        help_comment="# Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="Rscript",
        compiler_install={
            "linux": "sudo apt install r-base",
            "mac": "brew install r",
            "windows": "Download from https://cran.r-project.org"
        },
        lsp_server="r-languageserver",
        formatter="styler"
    ),

    "julia": LanguageConfig(
        name="julia",
        display_name="Julia",
        aliases=["jl"],
        file_extension="jl",
        main_file="main.jl",
        solution_file="solution.jl",
        compile_command=None,
        run_command=["julia", "{file}"],
        vim_run_command="<Space>r or :!julia %",
        help_comment="# Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="julia",
        compiler_install={
            "linux": "Download from https://julialang.org/downloads/",
            "mac": "brew install julia",
            "windows": "Download from https://julialang.org/downloads/"
        },
        lsp_server="julia-language-server",
        formatter="JuliaFormatter"
    ),

    "zig": LanguageConfig(
        name="zig",
        display_name="Zig",
        aliases=[],
        file_extension="zig",
        main_file="main.zig",
        solution_file="solution.zig",
        compile_command=["zig", "build-exe", "{file}"],
        run_command=["./main"],
        vim_run_command="<Space>r or :!zig build-exe % && ./main",
        help_comment="// Press <Esc> <Space> h for help.\n\n\n",
        compiler_check="zig",
        compiler_install={
            "linux": "Download from https://ziglang.org/download/",
            "mac": "brew install zig",
            "windows": "Download from https://ziglang.org/download/"
        },
        lsp_server="zls",
        formatter="zig fmt"
    ),

    "nosql": LanguageConfig(
        name="nosql",
        display_name="NoSQL",
        aliases=["mongodb", "mongo"],
        file_extension="js",
        main_file="main.js",
        solution_file="solution.js",
        compile_command=None,
        run_command=["mongosh", "{file}"],
        vim_run_command="<Space>r or :!mongosh %",
        help_comment="// Press <Esc> <Space> h for help.\n// NoSQL / MongoDB shell JavaScript\n\n\n",
        compiler_check="mongosh",
        compiler_install={
            "linux": "Follow: https://www.mongodb.com/docs/manual/installation/",
            "mac": "brew install mongodb-community-shell",
            "windows": "Download from https://www.mongodb.com/try/download/shell"
        },
        lsp_server=None,
        formatter=None
    ),
}


def get_language(name: str) -> Optional[LanguageConfig]:
    """Get language config by name or alias"""
    name = name.lower()

    # Direct match
    if name in LANGUAGES:
        return LANGUAGES[name]

    # Check aliases
    for lang_config in LANGUAGES.values():
        if name in lang_config.aliases:
            return lang_config

    return None


def get_all_language_names() -> List[str]:
    """Get all language names"""
    return list(LANGUAGES.keys())


def get_language_display_names() -> Dict[str, str]:
    """Get mapping of language name to display name"""
    return {name: config.display_name for name, config in LANGUAGES.items()}
