from common.fengzhuangdingwei import Base
from pageses.allpage.pages import homePage
class Home():
    click_xytk = Base.click(homePage.首页协议弹框)
    click_ty = Base.click(homePage.发现)