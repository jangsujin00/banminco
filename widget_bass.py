import sys # 파이썬 기본 라이브러리
from PyQt5.QtWidgets import * # *주면 모든파일 import함
from PyQt5 import uic

form_window = uic.loadUiType('./mainwidget.ui')[0] # loadUiType이걸 쓰면 class로 만들어줌

class Exam(QWidget, form_window): # 다중 상속 가능 # QWidget 닫기 최소화 등 버튼 활성화
    def __init__(self):
        super().__init__()
        self.setupUi(self) # setupUi가 많은 것을 설정해줌

if __name__ == "__main__": # 나중에 모듈로 써먹기 위해서
    app = QApplication(sys.argv) # 어플이 어플을 동작하게 하는 기능
    mainWindow = Exam() # 객체는 여기서 만들어 진다.
    mainWindow.show() # 화면에 출력해라
    sys.exit(app.exec_()) # 사용자가 한 액션을 처리하는 것 # exec 무한루프 # 윈도우 종료시 exit
    # 클릭 한 후 시그널이 발생하며 받을 슬롯을 지정해준다.