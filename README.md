# Legacy Software Investigation Tracker

A GUI tool to track your progress when investigating and maintaining legacy software projects. Maintains separate checklists and notes for each project with persistent history.

## Features

- **Per-project tracking**: Each software project gets its own checklist
- **Persistent storage**: All progress saved automatically to `~/.legacy_tracker.json`
- **Investigation checklist**: 15 common tasks for exploring legacy codebases
- **Notes section**: Document findings, gotchas, and important details per project
- **Auto-save**: Changes saved immediately as you check items or type notes

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Usage

Run the tracker:
```bash
python3 legacy_tracker.py
```

### Getting Started

1. Click **New Project** and enter the software name you're investigating
2. Work through the checklist, checking items as you complete them
3. Add notes about your findings in the text area
4. Switch between projects using the dropdown menu
5. Each project maintains its own state independently

### Managing Projects

- **Create**: Click "New Project" button
- **Switch**: Select from dropdown menu
- **Delete**: Select project, then click "Delete Project"

## Checklist Items

The tool includes these investigation tasks:

- Search for main entry point
- Find configuration files
- Locate database connection strings
- Identify API endpoints/routes
- Check build system
- Find and review documentation
- Locate test files
- Map external dependencies
- Check logging configuration
- Find deployment scripts
- Review database schema/migrations
- Identify authentication/authorization logic
- Locate error handling patterns
- Find scheduled jobs/cron tasks
- Check for environment-specific configs

## Data Storage

All data is stored in `~/.legacy_tracker.json` in JSON format. You can:
- Back up this file to preserve your investigation history
- Edit it manually if needed
- Share it with team members

## Tips

- Start a new project for each legacy system you investigate
- Use the notes section to document file paths, key functions, and gotchas
- Keep the tracker open while exploring code
- Review your checklist periodically to ensure thorough coverage
