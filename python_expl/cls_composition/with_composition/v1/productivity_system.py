class ProductivitySystem:

    def trace_productivity(self, employees):
        print("Tracking Productivity Starts...")
        print("Total Employees Found: ", {len(employees)})
        for e in employees:
            e.work(40)
