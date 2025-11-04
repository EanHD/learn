"""
Category system for organizing programming languages
Provides structured learning paths with descriptions and tips
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from pathlib import Path


@dataclass
class LanguageInfo:
    """Information about a specific language"""
    name: str
    display_name: str
    summary: str
    tips: List[str]
    reads: List[str]
    tools: List[str]


@dataclass
class Category:
    """A category of programming languages"""
    id: str
    title: str
    emoji: str
    description: str
    languages: List[str]
    language_details: Dict[str, LanguageInfo]


class CategoryManager:
    """Manages programming language categories"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.categories_dir = learn_dir / "categories"
        self.categories = self._load_categories()

    def _load_categories(self) -> List[Category]:
        """Load all category definitions"""
        # Built-in categories if JSON files don't exist
        return [
            Category(
                id="core",
                title="Core Languages",
                emoji="🧠",
                description="Build fundamentals, performance, and systems thinking.",
                languages=["c-c++", "rust", "go", "zig"],
                language_details={
                    "c-c++": LanguageInfo(
                        name="c-c++",
                        display_name="C / C++",
                        summary="Learn how computers really work. Everything from pointers to game engines.",
                        tips=[
                            "Don't fear the compiler. It's your best teacher.",
                            "Understand what memory leaks are early—it'll save your sanity later.",
                            "Start with C basics, then move to C++ features gradually."
                        ],
                        reads=[
                            "'The C Programming Language' by Kernighan and Ritchie",
                            "'Effective C++' by Scott Meyers",
                            "'What Every Programmer Should Know About Memory'"
                        ],
                        tools=[
                            "GCC/Clang compiler",
                            "Valgrind for memory debugging",
                            "GDB debugger"
                        ]
                    ),
                    "rust": LanguageInfo(
                        name="rust",
                        display_name="Rust",
                        summary="Safe systems programming with modern features.",
                        tips=[
                            "Borrow checker errors are your friend, not your enemy.",
                            "Clippy gives great feedback—treat it like a mentor.",
                            "Don't try to fight the borrow checker—learn to work with it."
                        ],
                        reads=[
                            "'The Rust Book' (free online at doc.rust-lang.org)",
                            "'Rustlings' practice repo",
                            "'Rust By Example' for hands-on learning"
                        ],
                        tools=[
                            "cargo (built-in package manager)",
                            "rustfmt for code formatting",
                            "clippy for linting"
                        ]
                    ),
                    "go": LanguageInfo(
                        name="go",
                        display_name="Go",
                        summary="Simple, fast, and built for modern cloud infrastructure.",
                        tips=[
                            "Embrace simplicity—Go intentionally avoids 'clever' features.",
                            "Goroutines make concurrency easy—learn them early.",
                            "Use gofmt—never argue about style again."
                        ],
                        reads=[
                            "'The Go Programming Language' by Donovan and Kernighan",
                            "'Effective Go' (free on golang.org)",
                            "'Go Concurrency Patterns' talks by Rob Pike"
                        ],
                        tools=[
                            "go fmt for formatting",
                            "go test for testing",
                            "delve for debugging"
                        ]
                    ),
                    "zig": LanguageInfo(
                        name="zig",
                        display_name="Zig",
                        summary="A modern C replacement. Simple, fast, and explicit.",
                        tips=[
                            "Zig has no hidden control flow—what you see is what you get.",
                            "Compile-time code execution is powerful—use it.",
                            "Error handling is explicit—embrace it."
                        ],
                        reads=[
                            "Official Zig Documentation (ziglang.org)",
                            "'Zig Learn' interactive guide",
                            "Zig community resources"
                        ],
                        tools=[
                            "zig compiler (build, test, fmt all built-in)",
                            "zls (language server)",
                            "zig fmt (built-in formatter)"
                        ]
                    )
                }
            ),
            Category(
                id="web",
                title="Web & Scripting",
                emoji="💻",
                description="Learn how to build websites, apps, and automation tools.",
                languages=["javascript", "typescript", "python", "php"],
                language_details={
                    "javascript": LanguageInfo(
                        name="javascript",
                        display_name="JavaScript",
                        summary="The language of the web. Powers both frontend and backend.",
                        tips=[
                            "Learn async/await—it's how modern JS works.",
                            "Understand 'this' and closures—they're everywhere.",
                            "Use the browser console to experiment constantly."
                        ],
                        reads=[
                            "'You Don't Know JS' series (free on GitHub)",
                            "'Eloquent JavaScript' by Marijn Haverbeke",
                            "MDN Web Docs (developer.mozilla.org)"
                        ],
                        tools=[
                            "Node.js runtime",
                            "npm/yarn package managers",
                            "ESLint for code quality"
                        ]
                    ),
                    "typescript": LanguageInfo(
                        name="typescript",
                        display_name="TypeScript",
                        summary="JavaScript with types. Catch errors before runtime.",
                        tips=[
                            "Start with loose types, tighten as you learn.",
                            "Type inference is your friend—don't over-annotate.",
                            "Use 'any' sparingly—it defeats the purpose."
                        ],
                        reads=[
                            "'TypeScript Deep Dive' (free online)",
                            "Official TypeScript Handbook",
                            "'Programming TypeScript' by Boris Cherny"
                        ],
                        tools=[
                            "tsc (TypeScript compiler)",
                            "ts-node for running TS directly",
                            "TypeScript ESLint"
                        ]
                    ),
                    "python": LanguageInfo(
                        name="python",
                        display_name="Python",
                        summary="Simple syntax, powerful libraries. From scripts to machine learning.",
                        tips=[
                            "Read PEP 8—Python has strong style conventions.",
                            "Use virtual environments (venv) for every project.",
                            "List comprehensions are powerful—learn them early."
                        ],
                        reads=[
                            "'Automate the Boring Stuff' by Al Sweigart (free online)",
                            "'Fluent Python' by Luciano Ramalho",
                            "'Python Tricks' by Dan Bader"
                        ],
                        tools=[
                            "pip package manager",
                            "black for formatting",
                            "pylint/flake8 for linting"
                        ]
                    ),
                    "php": LanguageInfo(
                        name="php",
                        display_name="PHP",
                        summary="Server-side scripting. Powers WordPress, Laravel, and millions of websites.",
                        tips=[
                            "Modern PHP (8+) is very different from old PHP—start fresh.",
                            "Composer is essential—it's PHP's package manager.",
                            "Learn a framework (Laravel/Symfony) after basics."
                        ],
                        reads=[
                            "'PHP: The Right Way' (free online guide)",
                            "'Modern PHP' by Josh Lockhart",
                            "Laravel documentation (best PHP framework)"
                        ],
                        tools=[
                            "Composer package manager",
                            "PHP-CS-Fixer for code style",
                            "PHPStan for static analysis"
                        ]
                    )
                }
            ),
            Category(
                id="mobile",
                title="Mobile Development",
                emoji="📱",
                description="Build native iOS, Android, and Flutter apps.",
                languages=["swift", "kotlin", "dart"],
                language_details={
                    "swift": LanguageInfo(
                        name="swift",
                        display_name="Swift",
                        summary="Apple's modern language for iOS, macOS, and beyond.",
                        tips=[
                            "Optionals are different from null—understand them deeply.",
                            "SwiftUI is the future—start there for new projects.",
                            "Playground is great for experimenting."
                        ],
                        reads=[
                            "'Swift Programming Language' by Apple (free)",
                            "'Hacking with Swift' tutorials",
                            "'iOS Programming: The Big Nerd Ranch Guide'"
                        ],
                        tools=[
                            "Xcode IDE",
                            "Swift Package Manager",
                            "Instruments for profiling"
                        ]
                    ),
                    "kotlin": LanguageInfo(
                        name="kotlin",
                        display_name="Kotlin",
                        summary="Modern Android development. Java, but better.",
                        tips=[
                            "Null safety is built-in—use it.",
                            "Extension functions keep code clean.",
                            "Coroutines make async code readable."
                        ],
                        reads=[
                            "'Kotlin in Action' by Jemerov and Isakova",
                            "Official Kotlin Docs (kotlinlang.org)",
                            "'Atomic Kotlin' by Bruce Eckel"
                        ],
                        tools=[
                            "Android Studio",
                            "Gradle build system",
                            "ktlint for code style"
                        ]
                    ),
                    "dart": LanguageInfo(
                        name="dart",
                        display_name="Dart",
                        summary="Powers Flutter. Build apps for iOS, Android, and web from one codebase.",
                        tips=[
                            "Learn Flutter widgets—everything is a widget.",
                            "Hot reload is amazing—use it constantly.",
                            "async/await syntax is similar to JavaScript."
                        ],
                        reads=[
                            "'Flutter in Action' by Eric Windmill",
                            "Official Flutter Docs (flutter.dev)",
                            "'Beginning Flutter' by Marco Napoli"
                        ],
                        tools=[
                            "Flutter SDK",
                            "Dart DevTools",
                            "Android Studio/VS Code with Flutter plugin"
                        ]
                    )
                }
            ),
            Category(
                id="data",
                title="Data & Databases",
                emoji="🧮",
                description="Learn to store, query, and analyze data.",
                languages=["sql", "nosql", "r", "julia"],
                language_details={
                    "sql": LanguageInfo(
                        name="sql",
                        display_name="SQL",
                        summary="The language of databases. Essential for any developer.",
                        tips=[
                            "Master JOINs—they're the heart of relational databases.",
                            "Learn indexes—they make or break performance.",
                            "Start with SQLite for practice—it's simple and portable."
                        ],
                        reads=[
                            "'SQL Queries for Mere Mortals' by Viescas",
                            "'Learning SQL' by Alan Beaulieu",
                            "PostgreSQL documentation (best DB docs)"
                        ],
                        tools=[
                            "SQLite for learning",
                            "PostgreSQL for production",
                            "MySQL/MariaDB alternatives"
                        ]
                    ),
                    "nosql": LanguageInfo(
                        name="nosql",
                        display_name="NoSQL",
                        summary="Document database. Store JSON-like data with flexible schemas (MongoDB example).",
                        tips=[
                            "Think in documents, not rows and columns.",
                            "Embedding vs referencing—learn when to use each.",
                            "Indexes are just as important in NoSQL."
                        ],
                        reads=[
                            "MongoDB University (free courses)",
                            "'MongoDB: The Definitive Guide'",
                            "Official NoSQL Database Documentation"
                        ],
                        tools=[
                            "MongoDB Compass (GUI)",
                            "mongosh (shell)",
                            "Atlas (cloud hosting)"
                        ]
                    ),
                    "r": LanguageInfo(
                        name="r",
                        display_name="R",
                        summary="Statistical programming. The language of data science and academia.",
                        tips=[
                            "Learn ggplot2 for beautiful visualizations.",
                            "dplyr makes data manipulation intuitive.",
                            "RStudio is the best IDE—use it."
                        ],
                        reads=[
                            "'R for Data Science' by Hadley Wickham (free online)",
                            "'The Art of R Programming' by Norman Matloff",
                            "R Documentation and CRAN packages"
                        ],
                        tools=[
                            "RStudio IDE",
                            "tidyverse packages",
                            "knitr for reports"
                        ]
                    ),
                    "julia": LanguageInfo(
                        name="julia",
                        display_name="Julia",
                        summary="High-performance computing. Fast as C, easy as Python.",
                        tips=[
                            "Multiple dispatch is Julia's superpower—embrace it.",
                            "Type annotations help performance—use them wisely.",
                            "The REPL is powerful—experiment interactively."
                        ],
                        reads=[
                            "'Julia High Performance' by Avik Sengupta",
                            "Official Julia Documentation",
                            "'Think Julia' (free online)"
                        ],
                        tools=[
                            "Julia REPL",
                            "Pluto.jl for notebooks",
                            "VS Code Julia extension"
                        ]
                    )
                }
            ),
            Category(
                id="scripting",
                title="Scripting & Automation",
                emoji="⚙️",
                description="Automate your environment and become a power user.",
                languages=["shell", "powershell", "lua"],
                language_details={
                    "shell": LanguageInfo(
                        name="shell",
                        display_name="Shell / Bash",
                        summary="Control Unix/Linux systems. Automate everything.",
                        tips=[
                            "Learn pipes (|) and redirection—they're powerful.",
                            "Use shellcheck to avoid common mistakes.",
                            "Start simple—complex scripts can be brittle."
                        ],
                        reads=[
                            "'The Linux Command Line' by William Shotts (free)",
                            "'Bash Cookbook' by Carl Albing",
                            "GNU Bash manual"
                        ],
                        tools=[
                            "bash shell",
                            "shellcheck linter",
                            "man pages (your best friend)"
                        ]
                    ),
                    "powershell": LanguageInfo(
                        name="powershell",
                        display_name="PowerShell",
                        summary="Windows automation. Object-based shell scripting.",
                        tips=[
                            "It's object-based, not text-based like Bash.",
                            "Get-Help is incredibly detailed—use it.",
                            "Aliases help, but learn the full cmdlet names."
                        ],
                        reads=[
                            "'Learn PowerShell in a Month of Lunches'",
                            "PowerShell documentation (docs.microsoft.com)",
                            "'Windows PowerShell Cookbook'"
                        ],
                        tools=[
                            "PowerShell Core (cross-platform)",
                            "VS Code PowerShell extension",
                            "PSScriptAnalyzer"
                        ]
                    ),
                    "lua": LanguageInfo(
                        name="lua",
                        display_name="Lua",
                        summary="Lightweight scripting. Embedded in games and apps.",
                        tips=[
                            "Tables are everything—arrays, objects, modules.",
                            "1-indexed arrays take getting used to.",
                            "Great for game modding and Neovim configs."
                        ],
                        reads=[
                            "'Programming in Lua' by Roberto Ierusalimschy",
                            "Lua 5.4 Reference Manual",
                            "Love2D for game development"
                        ],
                        tools=[
                            "Lua interpreter",
                            "LuaRocks package manager",
                            "Neovim (best Lua integration)"
                        ]
                    )
                }
            ),
            Category(
                id="enterprise",
                title="Enterprise & Systems",
                emoji="🏢",
                description="Build scalable, maintainable enterprise applications.",
                languages=["java", "csharp"],
                language_details={
                    "java": LanguageInfo(
                        name="java",
                        display_name="Java",
                        summary="Enterprise workhorse. Powers Android, servers, and everything in between.",
                        tips=[
                            "Learn OOP principles deeply—Java enforces them.",
                            "Spring Framework dominates enterprise—learn it after basics.",
                            "Streams API (Java 8+) makes collections powerful."
                        ],
                        reads=[
                            "'Effective Java' by Joshua Bloch",
                            "'Head First Java' for beginners",
                            "Official Oracle Java Tutorials"
                        ],
                        tools=[
                            "Maven/Gradle build tools",
                            "IntelliJ IDEA (best Java IDE)",
                            "JUnit for testing"
                        ]
                    ),
                    "csharp": LanguageInfo(
                        name="csharp",
                        display_name="C#",
                        summary="Microsoft's flagship language. From games to enterprise apps.",
                        tips=[
                            "LINQ is powerful—learn it to write cleaner code.",
                            "async/await in C# is well-designed—use it.",
                            "Unity uses C# for game development."
                        ],
                        reads=[
                            "'C# in Depth' by Jon Skeet",
                            "'Pro C# 10' by Andrew Troelsen",
                            "Microsoft C# documentation"
                        ],
                        tools=[
                            "Visual Studio / VS Code",
                            ".NET SDK",
                            "ReSharper for refactoring"
                        ]
                    )
                }
            )
        ]

    def get_all_categories(self) -> List[Category]:
        """Get all categories"""
        return self.categories

    def get_category(self, category_id: str) -> Optional[Category]:
        """Get a specific category by ID"""
        for cat in self.categories:
            if cat.id == category_id:
                return cat
        return None

    def get_category_for_language(self, language: str) -> Optional[Category]:
        """Find which category a language belongs to"""
        for cat in self.categories:
            if language in cat.languages:
                return cat
        return None

    def display_categories_menu(self) -> None:
        """Display the main categories menu"""
        print("\n" + "=" * 50)
        print("📚 LEARN PROGRAMMING")
        print("=" * 50 + "\n")

        for i, cat in enumerate(self.categories, 1):
            # Display languages in this category
            lang_names = []
            for lang in cat.languages:
                if lang in cat.language_details:
                    lang_names.append(cat.language_details[lang].display_name)

            print(f"{i}. {cat.emoji} {cat.title}")
            print(f"   → {', '.join(lang_names)}")
            print(f"   {cat.description}\n")

        print("=" * 50)

    def get_random_tip(self) -> str:
        """Get a random programming tip"""
        import random

        tips = [
            "💬 Did you know?\nThe first version of Python was written over Christmas break in 1989.\nGuido wanted an 'easy-to-read ABC successor.'",
            "💬 Fun Fact:\nRust was started by Mozilla employee Graydon Hoare as a side project\nto solve memory safety issues in Firefox.",
            "💬 Programming Wisdom:\nThe best way to learn a language is to build something with it.\nStart small, iterate often.",
            "💬 Did you know?\nLinus Torvalds created Git in just a few days because he was frustrated\nwith existing version control systems.",
            "💬 Learning Tip:\nDon't try to memorize syntax. Focus on understanding concepts.\nThe syntax will come naturally with practice.",
            "💬 Fun Fact:\nJavaScript was created in just 10 days by Brendan Eich at Netscape.\nDespite this, it's now one of the most popular languages.",
            "💬 Career Advice:\nLearn the fundamentals deeply. Languages come and go,\nbut core concepts like algorithms and data structures are timeless.",
            "💬 Did you know?\nThe name 'C++' is a pun—the ++ operator increments a value.\nSo C++ means 'one better than C.'",
            "💬 Debugging Wisdom:\nHalf of programming is writing code.\nThe other half is figuring out why it doesn't work.",
            "💬 Learning Philosophy:\nImposter syndrome is real. Every expert was once a beginner.\nThe struggle you feel means you're learning."
        ]

        return random.choice(tips)
