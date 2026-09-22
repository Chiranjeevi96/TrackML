# TrackML

A lightweight, from-scratch experiment tracker for ML training runs.

TrackML solves a problem every ML practitioner runs into: after training a
model multiple times with different settings, it's easy to lose track of
what was tried and what actually worked. TrackML records every run — its
settings and its result — so you can always look back and compare.

## Features

- Record training runs with flexible settings (any key-value pairs) and a numeric result
- Retrieve any run by its ID
- List all recorded runs
- Automatically find the best-performing run
- Input validation — rejects malformed settings or results
- Persistence — runs are saved to disk (`runs.json`) and reloaded automatically between sessions
- Ranked leaderboard view of all runs, best to worst

## How to run

1. Clone the repo

git clone https://github.com/Chiranjeevi96/TrackML.git
cd TrackML


2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\Activate.ps1 # Windows PowerShell


3. Run it

python trackml.py


## Example output

Run ID: 2, Settings: {'learning_rate': 0.02, 'epochs': 20}, Results: 90
Best Run ID: 2, Settings: {'learning_rate': 0.02, 'epochs': 20}, Results: 90
Rank 1: Run ID: 2, Settings: {'learning_rate': 0.02, 'epochs': 20}, Results: 90
Rank 2: Run ID: 1, Settings: {'learning_rate': 0.01, 'epochs': 10}, Results: 87


## Design

- `Run` represents a single training attempt — a small, fixed-shape object holding an ID, its settings, and its result.
- `Tracker` owns the collection of runs and all the logic around them: recording, retrieving, comparing, validating, and persisting. Keeping `Run` and `Tracker` separate follows a single-responsibility principle — one class defines what a run *is*, the other manages the collection.
- Data persists as JSON on disk, so runs survive between program restarts.

## Possible next steps

- CLI interface for interactive use
- Filtering/searching runs by setting values
- Export to CSV
- Delete a run