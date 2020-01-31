class ReportQueue:
    reports = []

    def submit_all(self):
        for i in range(len(self.reports)):
            print(i)
            # TYPE REPORT
            # RESET FORM
    
    def add_report(self, report):
        self.reports.append(report)

