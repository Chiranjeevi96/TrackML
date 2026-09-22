# TrackML - a lightweight experiment tracker for ML training runs
# v1: record and retrieve training runs
class Run:
    def __init__(self, ID, Settings, results):
        self.ID = ID
        self.Settings = Settings
        self.results = results
class Tracker:
    def __init__(self, last_run_ID=0):
        self.runs = {}
        self.last_run_ID = last_run_ID

    def add_run(self, Settings, results):
        self.last_run_ID += 1
        run = Run(self.last_run_ID, Settings, results)
        self.runs[run.ID] = run
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
        
    

tracker = Tracker()
run1 = tracker.add_run({"learning_rate": 0.01, "epochs": 10}, 87)
run2 = tracker.add_run({"learning_rate": 0.02, "epochs": 20}, 90)
found = tracker.get_run(1)
best_run = tracker.get_best_run()
list_of_runs = tracker.list_runs()  
print(f"Run ID: {found.ID}, Settings: {found.Settings}, Results: {found.results}")  
print(f"List of Runs: {[{'ID': run.ID, 'Settings': run.Settings, 'Results': run.results} for run in list_of_runs]}")    
print(f"Best Run ID: {best_run.ID}, Settings: {best_run.Settings}, Results: {best_run.results}")  