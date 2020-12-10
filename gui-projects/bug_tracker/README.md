# Bug Tracker Application

![](media/demo.gif)

## Completed
##### Security
- [x] Employee login with ID number and password
- [x] Popup login window instead of in-tab technician login
- [x] Create a separate file location for MongoDB connection data
##### Networking/Upload/Download
- [x] Connect with MongoDB
- [x] Technician login verification
##### Compatibility
- [x] Available on Windows/Mac/Linux
##### Functionality
- [x] Checkboxes to mark what information to send (with defaults)
- [x] Questionaire with urgency level
- [x] Generate and attach a screenshot
- [x] Text boxes to optionally write in more details
- [x] Preview of bug report with all selected information shown
- [x] Report sorting by time reported, severity, issue type, questionaire

## TODO
##### Security
- [ ] Secure Login Authentication through MongoDB
##### Networking/Upload/Download
- [ ] Reliable connection method without confidential code in data
##### Compatibility
- [ ] Create executables/packages for each OS
##### Functionality
- [ ] Update button functionality
    - [ ] Takes text from textbox
    - [ ] Takes case status text
    - [ ] Updates selected report with new info
- [ ] Report filtering based on case status (default=open)
- [ ] Search accounts functionality
    - [ ] Hides non-matching results from the table
- [ ] Search reports functionality
    - [ ] Searches filtered reports' submitter names and report details
    - [ ] Hides non-matching results from the table
