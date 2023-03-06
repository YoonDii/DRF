import base64
from PIL import Image  # pillow라는 외부라이브러리로 이미지 보기


# 기사 이미지
f = open("news/image", "rb")
image = f.readlines()
f.close()
print(image)  # base64 인코딩 파일

# 기사본문
f = open("news/article", "rb")
article = f.readlines()
f.close()
print(article)  # base64 인코딩 파일


# base64 디코딩
# 기사 이미지 디코딩
file_base64 = image[0]  # 위의 image는 리스트형식이라서 이미지의 첫번째부분을 뜻한다.

path = "news/image.jpg"  # 이 확장자로 저장
with open(path, "wb") as f:
    decoded_data = base64.decodebytes(file_base64)
    f.write(decoded_data)
    # news폴더에 image.jpg파일이 생긴것을 볼 수 있다.

# 이미지 확인
img = Image.open(path)
print(img)
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=647x458 at 0x100EAD2B0>

# 기사본문 디코딩
file_base64 = article[0]
decoded_data = base64.decodebytes(file_base64)  # 바이트형식으로 디코딩이 됨.
article = decoded_data.decode("utf-8")  # 한번더 형식을 디코딩해줘야함.
print(article)
# 29일(현지시간) 발사 예정인 ‘우주발사시스템’(SLS)로켓이 미국 플로리다주 케네디 우주센터의 발사대 39B에 설치돼 있다. (사진=나사)
# 나사가 발표한 달 착륙 후보지. 남극 부근으로 얼어있는 물이 있어 자원 개발을 기대할 수 있다. (사진=나사 제공)
# [이데일리 정다슬 기자] 2025년 인류를 달로 보내기 위한 첫 번째 여정이 하루 앞으로 다가왔다.28일 미국 항공우주국(NASA)에 따르면 (현지시간) 27일 미국 플로리다주 케네디우주센터에서는 오리온 우주선을 탑재한 ‘우주발사시스템’(SLS) 로켓 발사를 위한 카운트다운이 시작됐다. 별다른 변수가 없으면 SLS는 29일 오전 8시 33분(한국시간 오후 9시 33분) 달을 향해 떠오른다.카운트다운에 돌입한 후, 케네디 우주 센터에는 비와 번개가 쳤다. 다만, 발사대에는 피뢰침이 설치된 상태로 SLS에는 영향은 없는 것으로 알려졌다. 기상팀은 현재 구체적인 영향을 분석 중이다. 나사는 발사 당일인 29일에는 날씨가 갤 확률이 70% 이상이라고 보고 있다.나사는 발사 8시간 전, 즉 29일 자정쯤에 SLS에 연료(액체수소)와 산화제(액체산소)를 주입하는 절차를 시작한다. 액체연료는 미리 동체에 주입하면 부식을 일으킬 염려가 있다. 이 때문에 연료 주입은 발사 직전에 실행한다.발사 10분 전에는 외부에서 들어가던 전력을 오리온과 SLS가 스스로 공급하도록 전환한다. 그리고 카운트다운이 ‘0’이 되는 29일 오전 8시33분에 아르테미스 1호는 힘차게 달을 향해 날아오른다.기술적인 문제나 날씨 등의 외부변수로 29일 발사가 이뤄지지 않을 경우 나사는 다음 발사날짜를 9월 2일과 9월 5일로 예정했다.아르테미스는 42일 동안 약 지구와 달 사이의 거리인 209만 2148km를 여행할 예정이다. 연료를 꽉 채운 SLS의 무게는 570만파운드며 최대 880만파운드의 추진력을 가진다. 아폴로 우주선을 달로 보낸 새턴 V 로켓보다는 15% 정도 추진력이 강화됐다.이번 아르테미스 1호는 메인 로켓과 사람이 타는 유인캡슐인 오리온의 성능을 시험하는데도 중요하다. 단, 이번 오리온에는 사람 대신 3개의 마네킹을 태운다. 마네킹에는 센서가 있어서 우주 비행사가 달이 오가는 과정에서 겪어야 하는 외부적 환경 영향 등을 수집한다.오리온 우주선은 SLS와 분리된 후 달 궤도에 진입해 2주가량 임무를 수행한 후 지구로 복귀한다. 오는 10월 10일쯤 미국 샌디에이고 앞 태평양으로 귀환할 예정이다.달에 착륙하는 것 자체가 목표였던 아폴로 계획과는 달리 아르테미스 계획은 달, 더 나아가 화성까지 인류를 진출시키기 위한 담대한 계획의 일환이다. 아르테미스 계획은 태양의 신 아폴로의 쌍둥이 누이인 ‘달의 여신’의 이름을 땄다.제2탄으로는 우주비행사를 태우고 달 상공을 왕복하고, 제3탄으로 남녀 2명의 우주 비행사를 달 표면에 착륙시킨다. 달의 상공을 연결하는 우주 스테이션 ‘게이트웨이’도 건설한다.물과 같은 자원도 개발한다. 물이 중요시되는 것은 물로부터 로켓 연료나 에너지원이 되는 수소나 탄소 등을 만들 수 있기 때문이다. 나사는 수자원 개발 가능성이 큰 달의 남극 부근을 우주비행사의 착륙지로 보고 최근 13개 후보지를 발표했다. 무인탐사 로봇을 활용한 조사도 한다.달에서 로켓 연료를 조달할 수 있게 되면 달은 우주개발의 전진기지가 돼 화성 등 더욱 멀리 있는 행성을 탐사하는 비용을 크게 낮출 수 있게 된다. 미국은 달기지를 기반으로 2030년대에는 화성 유인탐사를 목표로 하고 있다.다만 이 같은 담대한 계획에는 적지 않은 난관이 있을 것으로 보인다. 2012년 관료들은 SLS를 개발하는 데는 60억달러가 소요되며 SLS로켓이 2017년 발사될 것으로 봤다. 그러나 발사 시기는 5년이나 지연됐고 개발비용 역시 200억달러를 넘어섰다. 나사 내부 감사관에 따르면, 아르테미스 프로그램에는 이미 400억달러가 넘는 비용이 소요됐으며 2025년까지 930억달러의 비용이 소요될 것으로 예상된다.그럼에도 아르테미스 프로그램은 미국내 정치권의 초당적 지지를 받고 있다. 이는 전 세계 패권 다툼이 우주 전쟁으로 확대하고 있기 때문이다. 중국과 러시아는 공동으로 달탐사 계획을 세워 먼저 로봇을 이용한 무인 달탐사기지나 우주스테이션을 건설하고 2030년대 초에는 우주비행사를 보낸다는 계획이다. 2030년대 후반에는 달의 남극에 장기체류 가능한 기지를 건설한다.바바야 랄 나사 기술 전략 담당 부국장은 “우리는 달, 화성, 태양계 전체에 지속적으로 미국이 존재한다는 장기적인 전략적 비전에 기반을 두고 있다”며 “나사는 한 세대에 걸쳐 가장 중요한 탐사 임무를 시작하는 역사적 변곡점에 서 있다”고 말했다.
