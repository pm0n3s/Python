class Patient(object):
    patient_count = 0
    def __init__(self, uid, pname, allergies):
        self.uid = Patient.patient_count
        self.pname = pname
        self.allergies = allergies
        self.bednum = None
        Patient.patient_count += 1

class Hospital(object):
    def __init__(self, hname, capacity):
        self.patients = []
        self.hname = hname
        self.capacity = capacity
        self.beds = self.initialize()

    def initialize(self):
        self.beds= []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["available"]:
                    patient.bednum = self.beds[i]["bed_id"]
                    self.beds[i]["available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.uid, patient.bednum)
        else:
            print "Hospital is at capacity"

    def discharge(self, patient):
        for p in self.patients:
            if patient == patient.uid:
                for b in self.beds:
                    if bed["bed_id"] == patient.bednum:
                        bed["available"] = True
                        break
                self.patients.remove(patient)
                print "Patient #{} successfully didscharged. Bed #{} available",format(patient.uid, patient.bednum)
            else:
                print "Patient not found"


