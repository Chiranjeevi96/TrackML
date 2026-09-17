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

tracker = Tracker()
run1 = tracker.add_run({"learning_rate": 0.01, "epochs": 10}, 87)
run2 = tracker.add_run({"learning_rate": 0.02, "epochs": 20}, 90)
found = tracker.get_run(2)
print(f"Run ID: {found.ID}, Settings: {found.Settings}, Results: {found.results}")  