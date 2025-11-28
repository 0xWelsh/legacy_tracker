#!/bin/bash
# legacy-search-helper.sh

echo "=== Legacy Code Investigation Checklist ==="
echo ""
echo "[ ] Search for function/variable usage: grep -r 'term' ."
echo "[ ] Check configuration files: find . -name '*.conf' -o -name '*.ini' -o -name '*.properties'"
echo "[ ] Find database queries: grep -r 'SELECT\|INSERT\|UPDATE\|DELETE' ."
echo "[ ] Look for API endpoints: grep -r 'route\|endpoint\|@RequestMapping' ."
echo "[ ] Check logs directory: ls -la logs/ /var/log/"
echo "[ ] Review build files: find . -name 'Makefile' -o -name 'pom.xml' -o -name 'build.gradle'"
echo "[ ] Find documentation: find . -name '*.md' -o -name '*.txt' -o -name 'README*'"
echo "[ ] Check for tests: find . -path '*/test/*' -o -name '*test*'"
echo "[ ] Look for dependencies: find . -name 'package.json' -o -name 'requirements.txt' -o -name 'Gemfile'"
