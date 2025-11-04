#!/usr/bin/env python3
"""
Audit all lesson.md files across language folders.
Check for: missing sections, placeholders, incorrect code fences, etc.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Define required sections based on c-c++ gold standard
REQUIRED_SECTIONS = [
    "Your Task",
    "How to",  # "How to Run", "How to Compile and Run", etc.
    "Answer Key"
]

PLACEHOLDER_PATTERNS = [
    r'\bTODO\b',
    r'\bTKTK\b',
    r'\bfill me\b',
    r'\bcoming soon\b',
    r'\bNEEDS_AUTHOR\b',
    r'\.\.\.',
    r'XXX',
]

# Language-specific execution command patterns from INSTRUCTIONS.md
EXECUTION_COMMANDS = {
    'python': ['python3', 'python'],
    'javascript': ['node', 'npm', 'yarn'],
    'typescript': ['ts-node', 'tsc', 'npm', 'yarn'],
    'rust': ['cargo', 'rustc'],
    'go': ['go run', 'go build'],
    'lua': ['lua'],
    'java': ['javac', 'java'],
    'julia': ['julia'],
    'dart': ['dart'],
    'swift': ['swift', 'swiftc'],
    'kotlin': ['kotlinc', 'kotlin'],
    'sql': ['sqlite3', 'mysql', 'psql'],
    'csharp': ['csc', 'dotnet', 'mono'],
    'shell': ['bash', 'sh'],
    'powershell': ['powershell', 'pwsh'],
    'zig': ['zig'],
}

class LessonAuditor:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.issues = defaultdict(list)
        self.stats = {
            'total': 0,
            'missing_task': 0,
            'missing_execution': 0,
            'missing_answer_key': 0,
            'has_placeholders': 0,
            'missing_code_fences': 0,
            'no_final_newline': 0,
            'perfect': 0,
        }

    def get_language_from_path(self, filepath):
        """Extract language from file path."""
        parts = filepath.parts
        for part in parts:
            if part in EXECUTION_COMMANDS:
                return part
        return None

    def check_required_sections(self, content, filepath):
        """Check for required sections."""
        issues = []

        # Check for "Your Task" or similar
        if not re.search(r'(Your Task|Today\'s Mission)', content, re.IGNORECASE):
            issues.append("Missing 'Your Task' section")
            self.stats['missing_task'] += 1

        # Check for execution instructions
        if not re.search(r'How to (Run|Compile|Execute)', content, re.IGNORECASE):
            issues.append("Missing 'How to Run/Compile' section")
            self.stats['missing_execution'] += 1

        # Check for Answer Key
        if not re.search(r'Answer Key', content, re.IGNORECASE):
            issues.append("Missing 'Answer Key' section")
            self.stats['missing_answer_key'] += 1

        return issues

    def check_placeholders(self, content):
        """Check for placeholder text."""
        issues = []
        for pattern in PLACEHOLDER_PATTERNS:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # Get line number
                line_num = content[:match.start()].count('\n') + 1
                issues.append(f"Placeholder '{match.group()}' at line {line_num}")

        if issues:
            self.stats['has_placeholders'] += 1
        return issues

    def check_code_fences(self, content, language):
        """Check if code fences have proper language tags."""
        issues = []

        # Find all code fences
        fence_pattern = r'```(\w*)\n'
        fences = re.findall(fence_pattern, content)

        if not fences:
            return issues

        # Check if any fences are missing language tags
        empty_fences = [i for i, f in enumerate(fences) if not f]
        if empty_fences:
            issues.append(f"Found {len(empty_fences)} code fence(s) without language tag")
            self.stats['missing_code_fences'] += 1

        # Check if language-specific fences exist
        if language:
            expected_langs = EXECUTION_COMMANDS.get(language, [])
            # Also check for common alternatives
            if language == 'javascript':
                expected_langs.extend(['js', 'javascript'])
            elif language == 'typescript':
                expected_langs.extend(['ts', 'typescript'])
            elif language == 'python':
                expected_langs.extend(['py', 'python', 'python3'])
            elif language == 'csharp':
                expected_langs.extend(['cs', 'csharp', 'c#'])

            has_lang_fence = any(f in expected_langs for f in fences if f)
            if not has_lang_fence and 'bash' not in fences and 'sh' not in fences:
                issues.append(f"No {language}-specific code fences found")

        return issues

    def check_final_newline(self, content):
        """Check if file ends with newline."""
        if not content.endswith('\n'):
            self.stats['no_final_newline'] += 1
            return ["Missing final newline"]
        return []

    def audit_file(self, filepath):
        """Audit a single lesson.md file."""
        self.stats['total'] += 1

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.issues[str(filepath)].append(f"Error reading file: {e}")
            return

        language = self.get_language_from_path(filepath)
        file_issues = []

        # Run all checks
        file_issues.extend(self.check_required_sections(content, filepath))
        file_issues.extend(self.check_placeholders(content))
        file_issues.extend(self.check_code_fences(content, language))
        file_issues.extend(self.check_final_newline(content))

        if file_issues:
            self.issues[str(filepath)] = file_issues
        else:
            self.stats['perfect'] += 1

    def find_all_lessons(self):
        """Find all lesson.md files excluding c-c++."""
        lessons = []
        for lang_dir in self.root_dir.iterdir():
            if not lang_dir.is_dir():
                continue
            if lang_dir.name == 'c-c++':
                continue
            if lang_dir.name.startswith('.'):
                continue

            # Find lesson.md files
            for lesson in lang_dir.rglob('lesson.md'):
                lessons.append(lesson)

        return sorted(lessons)

    def generate_report(self):
        """Generate audit report."""
        report = []
        report.append("=" * 80)
        report.append("LESSON AUDIT REPORT")
        report.append("=" * 80)
        report.append("")

        # Statistics
        report.append("STATISTICS")
        report.append("-" * 80)
        report.append(f"Total lessons audited: {self.stats['total']}")
        report.append(f"Perfect lessons: {self.stats['perfect']} ({self.stats['perfect']/self.stats['total']*100:.1f}%)")
        report.append(f"Lessons with issues: {len(self.issues)}")
        report.append("")
        report.append("COMMON ISSUES:")
        report.append(f"  - Missing 'Your Task': {self.stats['missing_task']}")
        report.append(f"  - Missing execution instructions: {self.stats['missing_execution']}")
        report.append(f"  - Missing Answer Key: {self.stats['missing_answer_key']}")
        report.append(f"  - Contains placeholders: {self.stats['has_placeholders']}")
        report.append(f"  - Missing code fence languages: {self.stats['missing_code_fences']}")
        report.append(f"  - Missing final newline: {self.stats['no_final_newline']}")
        report.append("")

        # Group by language
        by_language = defaultdict(list)
        for filepath, issues in self.issues.items():
            lang = None
            for l in EXECUTION_COMMANDS.keys():
                if f'/{l}/' in filepath:
                    lang = l
                    break
            by_language[lang or 'unknown'].append((filepath, issues))

        report.append("ISSUES BY LANGUAGE")
        report.append("-" * 80)
        for lang in sorted(by_language.keys()):
            files = by_language[lang]
            report.append(f"\n{lang.upper()}: {len(files)} files with issues")
            report.append("")

            # Show first 5 files with issues
            for filepath, issues in files[:5]:
                report.append(f"  {Path(filepath).relative_to(self.root_dir)}")
                for issue in issues[:3]:  # Show first 3 issues
                    report.append(f"    • {issue}")
                if len(issues) > 3:
                    report.append(f"    ... and {len(issues) - 3} more issues")
                report.append("")

            if len(files) > 5:
                report.append(f"  ... and {len(files) - 5} more files\n")

        return "\n".join(report)

def main():
    """Main execution."""
    root_dir = Path(__file__).parent
    auditor = LessonAuditor(root_dir)

    print("Finding lesson.md files...")
    lessons = auditor.find_all_lessons()
    print(f"Found {len(lessons)} lessons to audit (excluding c-c++)")

    print("\nAuditing lessons...")
    for i, lesson in enumerate(lessons, 1):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(lessons)}")
        auditor.audit_file(lesson)

    print("\nGenerating report...")
    report = auditor.generate_report()
    print(report)

    # Save report to file
    report_path = root_dir / 'audit_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\nDetailed report saved to: {report_path}")

    # Create issue breakdown by severity
    print("\n" + "=" * 80)
    print("PRIORITY FIXES NEEDED:")
    print("=" * 80)
    print(f"HIGH: {auditor.stats['missing_task'] + auditor.stats['missing_execution'] + auditor.stats['missing_answer_key']} lessons missing critical sections")
    print(f"MEDIUM: {auditor.stats['has_placeholders']} lessons with placeholders")
    print(f"LOW: {auditor.stats['missing_code_fences'] + auditor.stats['no_final_newline']} lessons with formatting issues")

if __name__ == '__main__':
    main()
