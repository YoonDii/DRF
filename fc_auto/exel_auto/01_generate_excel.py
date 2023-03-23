from openpyxl import Workbook


class WeeklyWorkPlan:
    wb = None
    ws = None
    manager = "매니저 이름을 입력 해주세요."

    def __init__(self, manager, sheet_no=0):  # sheet_no로 시트번호바꾸기
        self.wb = Workbook()
        self.ws = self.wb.worksheets[sheet_no]
        self.manager = manager
        self.set_title()

    def save(self, filename):
        self.wb.save(filename)
        print("엑셀파일 생성 완료")

    def set_title(self):
        self.ws["B2"] = "담당자"
        self.ws["C2"] = self.manager


if __name__ == "__main__":
    wwp = WeeklyWorkPlan("yoondii")
    wwp.save("주간업무계획표.xlsx")
