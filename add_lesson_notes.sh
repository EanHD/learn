#!/bin/bash

# Add teacher's note to all lesson.md files
# This ensures consistent UX across all 490 lessons

echo "Adding teacher's notes to all lesson.md files..."

NOTE='> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.

'

count=0
skipped=0

# Find all lesson.md files
find . -name "lesson.md" -type f | while read -r file; do
    # Check if file already has the note
    if grep -q "LESSON NOTE" "$file"; then
        echo "✓ Skipped (already has note): $file"
        skipped=$((skipped + 1))
    else
        # Get the first line (should be a heading)
        first_line=$(head -n 1 "$file")
        
        # Create temp file with note inserted after first line
        {
            echo "$first_line"
            echo ""
            echo "$NOTE"
            tail -n +2 "$file"
        } > "$file.tmp"
        
        # Replace original
        mv "$file.tmp" "$file"
        
        echo "✅ Added note to: $file"
        count=$((count + 1))
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Complete!"
echo "   Updated: $count files"
echo "   Skipped: $skipped files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
