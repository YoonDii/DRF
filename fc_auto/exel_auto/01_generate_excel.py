from openpyxl import Workbook


class WeeklyWorkPlan:
    wb = None
    ws = None

    def __init__(self, sheet_no=0):  # sheet_no로 시트번호바꾸기
        self.wb = Workbook()
        self.ws = self.wb.worksheets[sheet_no]
        self.set_title()

    def save(self, filename):
        self.wb.save(filename)
        print("엑셀파일 생성 완료")

    def set_title(self):
        self.ws["B2"] = "담당자"


if __name__ == "__main__":
    wwp = WeeklyWorkPlan()

    wwp.save("주간업무계획표.xlsx")
