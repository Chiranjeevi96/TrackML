# TrackML - a lightweight experiment tracker for ML training runs
# v1: record and retrieve training runs
# 

import json
class Run:
    def __init__(self, ID, Settings, results):
        self.ID = ID
        self.Settings = Settings
        self.results = results
class Tracker:
    def __init__(self, last_run_ID=0):
        self.runs = {}
        self.last_run_ID = last_run_ID
        self.load_from_file()  # Load existing runs from file

    def add_run(self, Settings, results):
        if not isinstance(Settings, dict):
            raise TypeError("Settings must be a dictionary")
        if not isinstance(results, (int, float)):
            raise TypeError("Results must be a number")
         
        self.last_run_ID += 1
        run = Run(self.last_run_ID, Settings, results)
        self.runs[run.ID] = run
        self.save_to_file() # Save the updated runs to file
        return run
        
    def get_run(self, run_ID):
        return self.runs.get(run_ID)

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
            all_runs_as_dicts[run.ID] = {"ID": run.ID, "Settings": run.Settings, "results": run.results}
        with open("runs.json", "w") as f:
            json.dump(all_runs_as_dicts, f)

    def load_from_file(self):
        try:
            with open("runs.json", "r") as f:
                all_runs_as_dicts = json.load(f)
                for run_ID, run_data in all_runs_as_dicts.items():
                    run = Run(run_data["ID"], run_data["Settings"], run_data["results"])
                    self.runs[run.ID] = run
                    self.last_run_ID = max(self.last_run_ID, run.ID)
        except FileNotFoundError:
            pass  # No previous runs to load
    

tracker = Tracker()
run1 = tracker.add_run({"learning_rate": 0.01, "epochs": 10}, 87)
run2 = tracker.add_run({"learning_rate": 0.02, "epochs": 20}, 90)
# run3 = tracker.add_run("Text", 85)
# run4 = tracker.add_run({"learning_rate": 0.03, "epochs": 30}, "hello")
found = tracker.get_run(2)
best_run = tracker.get_best_run()
list_of_runs = tracker.list_runs()  
print(f"Run ID: {found.ID}, Settings: {found.Settings}, Results: {found.results}")  
print(f"List of Runs: {[{'ID': run.ID, 'Settings': run.Settings, 'Results': run.results} for run in list_of_runs]}")    
print(f"Best Run ID: {best_run.ID}, Settings: {best_run.Settings}, Results: {best_run.results}")  