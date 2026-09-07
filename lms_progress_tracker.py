class Session:
    def __init__(self, session_id, name, phase, is_completed=False):
        self.session_id = session_id
        self.name = name
        self.phase = phase
        self.is_completed = is_completed

class StudyTracker:
    def __init__(self, student_name):
        self.student_name = student_name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def update_session_status(self, session_id, status):
        for session in self.sessions:
            if session.session_id == session_id:
                session.is_completed = status
                print(f'[UPDATE] Da cap nhat trang thai Session {session_id}: {"HOAN THANH" if status else "CHUA HOAN THANH"}')
                return True
        print(f'[ERROR] Khong tim thay Session co ID: {session_id}')
        return False

    def get_completion_percentage(self):
        if not self.sessions:
            return 0.0
        completed_count = sum(1 for s in self.sessions if s.is_completed)
        return (completed_count / len(self.sessions)) * 100

    def generate_progress_report(self):
        print('\n' + '='*60)
        print(f'BAO CAO TIEN DO HOC TAP MON IT105 - SINH VIEN: {self.student_name.upper()}')
        print('='*60)
        
        phases = {}
        for s in self.sessions:
            if s.phase not in phases:
                phases[s.phase] = []
            phases[s.phase].append(s)

        for phase_name, session_list in phases.items():
            print(f'\n* Giai doan: {phase_name}')
            completed_in_phase = sum(1 for s in session_list if s.is_completed)
            total_in_phase = len(session_list)
            phase_percent = (completed_in_phase / total_in_phase) * 100
            print(f'  Tien do: {completed_in_phase}/{total_in_phase} ({phase_percent:.1f}%)')
            
            for s in session_list:
                status_char = '[x]' if s.is_completed else '[ ]'
                print(f'    {status_char} Session {s.session_id:02d}: {s.name}')

        total_percent = self.get_completion_percentage()
        print('\n' + '='*60)
        print(f'TONG KET TIEN DO TOAN KHOA HOC: {total_percent:.2f}%')
        if total_percent >= 100.0:
            print('Chuc mung! Ban da hoan thanh xuat sac toan bo khoa hoc!')
        elif total_percent >= 50.0:
            print('Ban dang di dung huong, hay tiep tuc duy tri phong do!')
        else:
            print('Can tap trung va danh nhieu thoi gian hon de khong bi tre han!')
        print('='*60 + '\n')

def main():
    tracker = StudyTracker('Nguyen Hoang Long')

    # Giai doan 1
    tracker.add_session(Session(1, 'Dinh huong hoc tap & Khai niem HTTT', 'Khoi dong & Khao sat', True))
    tracker.add_session(Session(2, 'Tong quat phan tich & thiet ke he thong', 'Khoi dong & Khao sat', True))
    tracker.add_session(Session(3, 'Khao sat & Thu thap thong tin', 'Khoi dong & Khao sat', True))
    tracker.add_session(Session(4, 'Thuc hanh Khao sat & Thu thap thong tin', 'Khoi dong & Khao sat', True))

    # Giai doan 2
    tracker.add_session(Session(5, 'Activity & Use Case Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(6, 'Thuc hanh Activity & Use Case Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(7, 'Class Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(8, 'Thuc hanh Class Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(9, 'Sequence Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(10, 'Thuc hanh Sequence Diagram', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(11, 'Mini Project tong hop 1', 'Mo hinh hoa UML', False))
    tracker.add_session(Session(12, 'Thi Hackathon', 'Mo hinh hoa UML', False))

    # Giai doan 3
    tracker.add_session(Session(13, 'Phan tich, thiet ke UI/UX', 'Thiet ke Chi tiet', False))
    tracker.add_session(Session(14, 'Thuc hanh UI/UX', 'Thiet ke Chi tiet', False))
    tracker.add_session(Session(15, 'Phan tich, thiet ke ERD', 'Thiet ke Chi tiet', False))
    tracker.add_session(Session(16, 'Thuc hanh Thiet ke ERD', 'Thiet ke Chi tiet', False))

    # Giai doan 4
    tracker.add_session(Session(17, 'Kien truc he thong & Tai lieu SRS', 'Dong goi & Bao ve', False))
    tracker.add_session(Session(18, 'Thuc hanh SRS', 'Dong goi & Bao ve', False))
    tracker.add_session(Session(19, 'Mini Project tong hop 2', 'Dong goi & Bao ve', False))
    tracker.add_session(Session(20, 'On tap cuoi mon', 'Dong goi & Bao ve', False)) 

    # Hien thi bao cao ban dau
    tracker.generate_progress_report()

    # Mo phong sinh vien hoan thanh them cac bai hoc moi
    print('--- TIEN HANH CAP NHAT TIEN DO HOC TAP MO PHONG ---')
    tracker.update_session_status(5, True)
    tracker.update_session_status(6, True)
    
    # Hien thi lai bao cao sau khi cap nhat
    tracker.generate_progress_report()

if __name__ == '__main__':
    main()