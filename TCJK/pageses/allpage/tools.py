#读取所有yaml文件
import os
import yaml
import jinja2
#当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
def parseryaml(yamlPagesPath=basepath):
    #定义空字典存储所有页面元素
    pageElements = {}
    for fpath,dirname,fnames in os.walk(yamlPagesPath):
        #yaml文件路径=当前脚本路径+yaml文件名称
        for fname in fnames:
            yamlfilepath = os.path.join(fpath, fname)
            if ".yaml" in str(yamlfilepath):
                with open(yamlfilepath,'r',encoding="utf-8") as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements

def get_page_list(yamlpage):
    page_object={}
    for page,names in yamlpage.items():
        loc_names = []
        #获取locators定位方法
        locs = names['locators']
        #添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

#创建模板文件
def creat_pages_py(page_list):
    """
    function:用jinja2把templetpage模板生成pages.py文件
        args:传get_page_list返回的内容
    """
    print(os.path.join(basepath,"templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)
    templateVars={
        'page_list':page_list
    }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath,"pages.py"),'w',encoding='utf-8') as f:
        f.write(template.render(templateVars))

if __name__=='__main__':
    all = parseryaml(yamlPagesPath=basepath)
    page_list = get_page_list(all)
    print(page_list)
    creat_pages_py(page_list)







