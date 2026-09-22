# TrackML - a lightweight experiment tracker for ML training runs
# v1: record and retrieve training runs
# 

import json
class Run:
    def __init__(self, run_id, settings, results):
        self.run_id = run_id
        self.settings = settings
        self.results = results
class Tracker:
    def __init__(self, last_run_id=0):
        self.runs = {}
        self.last_run_id = last_run_id
        self.load_from_file()  # Load existing runs from file

    def add_run(self, settings, results):
        if not isinstance(settings, dict):
            raise TypeError("Settings must be a dictionary")
        if not isinstance(results, (int, float)):
            raise TypeError("Results must be a number")
         
        self.last_run_id += 1
        run = Run(self.last_run_id, settings, results)
        self.runs[run.run_id] = run
        self.save_to_file() # Save the updated runs to file
        return run
        
    def get_run(self, run_id):
        return self.runs.get(run_id)

    def list_runs(self):
        return list(self.runs.values())

    def get_best_run(self):
        best = None
        for run in self.runs.values():
            if best is None or run.results > best.results:
                best = run
        return best

    def save_to_file(self):
        all_runs_as_dicts = {}
        for run in self.runs.values():
            all_runs_as_dicts[run.run_id] = {"id": run.run_id, "settings": run.settings, "results": run.results}
        with open("runs.json", "w") as f:
            json.dump(all_runs_as_dicts, f)

    def load_from_file(self):
        try:
            with open("runs.json", "r") as f:
                all_runs_as_dicts = json.load(f)
                for run_id, run_data in all_runs_as_dicts.items():
                    run = Run(run_data["id"], run_data["settings"], run_data["results"])
                    self.runs[run.run_id] = run
                    self.last_run_id = max(self.last_run_id, run.run_id)
        except FileNotFoundError:
            pass  # No previous runs to load

    def get_leadboards(self):
        return sorted(self.list_runs(), key=lambda run: run.results, reverse=True)    

tracker = Tracker()
run1 = tracker.add_run({"learning_rate": 0.01, "epochs": 10}, 87)
run2 = tracker.add_run({"learning_rate": 0.02, "epochs": 20}, 90)
found = tracker.get_run(2)
best_run = tracker.get_best_run()
list_of_runs = tracker.list_runs()  
print(f"Run ID: {found.run_id}, Settings: {found.settings}, Results: {found.results}")  
print(f"List of Runs: {[{'id': run.run_id, 'settings': run.settings, 'results': run.results} for run in list_of_runs]}")    
print(f"Best Run ID: {best_run.run_id}, Settings: {best_run.settings}, Results: {best_run.results}")  

leaderboard = tracker.get_leadboards()

for index, run in enumerate(leaderboard, start=1):
    print(f"Rank {index}: Run ID: {run.run_id}, Settings: {run.settings}, Results: {run.results}")