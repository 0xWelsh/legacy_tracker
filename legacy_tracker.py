#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class LegacyTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Legacy Software Investigation Tracker")
        self.root.geometry("700x600")
        
        self.data_file = os.path.expanduser("~/.legacy_tracker.json")
        self.projects = self.load_data()
        self.current_project = None
        
        self.checklist_items = [
            "Search for main entry point (main(), index, etc.)",
            "Find configuration files (.conf, .ini, .properties)",
            "Locate database connection strings",
            "Identify API endpoints/routes",
            "Check build system (Makefile, pom.xml, etc.)",
            "Find and review README/documentation",
            "Locate test files and test data",
            "Map external dependencies",
            "Check logging configuration",
            "Find deployment scripts",
            "Review database schema/migrations",
            "Identify authentication/authorization logic",
            "Locate error handling patterns",
            "Find scheduled jobs/cron tasks",
            "Check for environment-specific configs"
        ]
        
        self.setup_ui()
        
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.projects, f, indent=2)
    
    def setup_ui(self):
        # Project selection frame
        proj_frame = ttk.Frame(self.root, padding="10")
        proj_frame.pack(fill=tk.X)
        
        ttk.Label(proj_frame, text="Project:").pack(side=tk.LEFT)
        
        self.project_var = tk.StringVar()
        self.project_combo = ttk.Combobox(proj_frame, textvariable=self.project_var, width=30)
        self.project_combo['values'] = list(self.projects.keys())
        self.project_combo.pack(side=tk.LEFT, padx=5)
        self.project_combo.bind('<<ComboboxSelected>>', self.load_project)
        
        ttk.Button(proj_frame, text="New Project", command=self.new_project).pack(side=tk.LEFT, padx=5)
        ttk.Button(proj_frame, text="Delete Project", command=self.delete_project).pack(side=tk.LEFT)
        
        # Checklist frame
        check_frame = ttk.LabelFrame(self.root, text="Investigation Checklist", padding="10")
        check_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollable checklist
        canvas = tk.Canvas(check_frame)
        scrollbar = ttk.Scrollbar(check_frame, orient="vertical", command=canvas.yview)
        self.checklist_frame = ttk.Frame(canvas)
        
        self.checklist_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.checklist_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.check_vars = []
        
        # Notes frame
        notes_frame = ttk.LabelFrame(self.root, text="Notes", padding="10")
        notes_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.notes_text = tk.Text(notes_frame, height=8, wrap=tk.WORD)
        self.notes_text.pack(fill=tk.BOTH, expand=True)
        self.notes_text.bind('<KeyRelease>', self.save_notes)
        
    def new_project(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("New Project")
        dialog.geometry("300x100")
        
        ttk.Label(dialog, text="Project Name:").pack(pady=10)
        name_entry = ttk.Entry(dialog, width=30)
        name_entry.pack(pady=5)
        name_entry.focus()
        
        def create():
            name = name_entry.get().strip()
            if not name:
                messagebox.showwarning("Warning", "Project name cannot be empty")
                return
            if name in self.projects:
                messagebox.showwarning("Warning", "Project already exists")
                return
            
            self.projects[name] = {
                "created": datetime.now().isoformat(),
                "checklist": {item: False for item in self.checklist_items},
                "notes": ""
            }
            self.save_data()
            self.project_combo['values'] = list(self.projects.keys())
            self.project_var.set(name)
            self.load_project()
            dialog.destroy()
        
        ttk.Button(dialog, text="Create", command=create).pack(pady=5)
    
    def delete_project(self):
        project = self.project_var.get()
        if not project:
            messagebox.showwarning("Warning", "No project selected")
            return
        
        if messagebox.askyesno("Confirm", f"Delete project '{project}'?"):
            del self.projects[project]
            self.save_data()
            self.project_combo['values'] = list(self.projects.keys())
            self.project_var.set('')
            self.clear_checklist()
    
    def load_project(self, event=None):
        project = self.project_var.get()
        if not project or project not in self.projects:
            return
        
        self.current_project = project
        self.clear_checklist()
        
        # Load checklist
        for widget in self.checklist_frame.winfo_children():
            widget.destroy()
        
        self.check_vars = []
        project_data = self.projects[project]
        
        for item in self.checklist_items:
            var = tk.BooleanVar(value=project_data["checklist"].get(item, False))
            cb = ttk.Checkbutton(self.checklist_frame, text=item, variable=var, 
                                command=lambda: self.save_checklist())
            cb.pack(anchor=tk.W, pady=2)
            self.check_vars.append((item, var))
        
        # Load notes
        self.notes_text.delete('1.0', tk.END)
        self.notes_text.insert('1.0', project_data.get("notes", ""))
    
    def clear_checklist(self):
        for widget in self.checklist_frame.winfo_children():
            widget.destroy()
        self.check_vars = []
        self.notes_text.delete('1.0', tk.END)
    
    def save_checklist(self):
        if not self.current_project:
            return
        
        for item, var in self.check_vars:
            self.projects[self.current_project]["checklist"][item] = var.get()
        
        self.save_data()
    
    def save_notes(self, event=None):
        if not self.current_project:
            return
        
        self.projects[self.current_project]["notes"] = self.notes_text.get('1.0', tk.END).strip()
        self.save_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = LegacyTracker(root)
    root.mainloop()
